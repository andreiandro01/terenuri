# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 01:33:00 2022

@author: Andrei
"""
import time
import re
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


from datetime import date,datetime,timedelta





start = time.time()
browser = webdriver.Chrome(ChromeDriverManager().install()) #Initializes / installs chrome driver    
browser.get("https://www.calendis.ro/cluj-napoca/baza-sportiva-la-terenuri-1/fotbal-1/s") 



def login(username="",password=""):
    browser.find_element_by_id("forEmail").send_keys(username)
    browser.find_element_by_id("forPassword").send_keys(password)
    browser.find_element_by_xpath('//*[@id="accounts-modal"]/div/div[1]/div[2]/div[3]/form/button').click()
    sleep(0.2)
    
    
    
while True:
    login_condition = input("Login with default user ? (y/n):")

    
    if login_condition == "y":
        username = "beergenerator2@gmail.com"
        password = "Sc8UD9ipJ56@iRd"
        break
    if login_condition =="n":
        username = input ("Enter your username: ")
        password = input("Enter your password: ")
        break
    
    if login_condition != "y" or "n":
        print("Use 'y' or 'n' as parameters")


    
login(username=username, password=password)  
print('Login succesful')
dt = datetime.now()
zi = dt.isoweekday() #Ziua in care e rulat programul in valoare numerica (luni-duminica = 1-7)

current = date.today()
day = (current + timedelta(weeks=2)) #Calculeaza care e valoarea numerica a zilei de peste 2 saptamani (Ex. 27 ian + 14 zile = 10 Feb)
decimal = (day.strftime("%d")).lstrip("0")
print(f'Day of reservation (two weeks from now) : {day}')


date = ""


while date != decimal:    #Scroll prin calendar pana cand gaseste ziua cu 2 saptamani in fata de ziua curenta (by default e ziua in care e rulat programul)
    sleep(1)
    calendis_day = []
    browser.find_element_by_css_selector('#appointment-calendar > div.calendis-days > div.calendar-arrow.right-arrow').click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="appointment-calendar"]/div[2]/div[2]/div[{zi}]'))).click()
    current_date = browser.find_element_by_xpath(f'//*[@id="appointment-calendar"]/div[2]/div[2]/div[{zi}]').text
    calendis_day.append(current_date)
    date_split = [x.split("\n") for x in calendis_day]
    date = date_split[0][1]
    
print(f"Selected date : {date_split[0][0]} {date_split[0][1]}")



WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="appointment-calendar"]/div[2]/div[2]/div[{zi}]'))).click() #Double-check la selectarea zilei

sleep(1) # Buffer time, altfel loop-ul ce urmeaza o sa dea fail fiindca orele nu sunt incarcate.
         # Nu aftecteaza performanta fiindca tot ce e pana aici ruleaza inainte de HH:55 (preferabil la HH:54 sau chiar HH:53)
end = time.time()
total_time = end - start
print("\n"+ str(total_time))

    
while True:   
    ora_rezervarii = input("Ora de la care sa fie facuta rezervarea (format HH:00, ex: 20:00, 17:00): ")
    pattern = '\d{1,2}\:\d{1,2}' 
    match = re.match(pattern, ora_rezervarii)
    if not match:
        print('Format invalid, mai baga o fisa')
    elif match:
        print(f'Ora aleasa : {ora_rezervarii}')
        break
#Loop-ul propriu-zis care face rezervarea: 
"""
Listeaza toate orele disponibile folosind index-ul elementelui. Ora rezervarii va fi mereu ultimul index din lista 
deci practic, indexul orei rezervarii = len(lista_elemente)
        
"""
    
while True: 
    try:
        start = time.time()
        elm = browser.find_elements_by_css_selector('#appointment-slots') #orele disponibile
        count = []
        for e in elm:
            count.append(e.text)
            
        split = [x.split("\n") for x in count]
        index = len(split[0]) #indexul ultimei ore
        sleep(0.1)
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
        hour = WebDriverWait(browser, 20,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="appointment-slots"]/div[{index}]/div'))).text
        hour_list2 = browser.find_elements_by_xpath(f'//*[@id="appointment-slots"]/div[{index}]/div')
        for h in hour_list2: #Fiindca orele sunt intr-un inner window, trebuie adaugat si for loop-ul asta care scrolleaza pana la ultimul element. 
            browser.execute_script("arguments[0].scrollIntoView();", h)    
    except StaleElementReferenceException:
        pass

    if hour == f"{ora_rezervarii}":
        print(f"Rezervare in curs, ora rezervata: '{hour}'")
        while True:
            try:
                hour_list2 = browser.find_elements_by_xpath(f'//*[@id="appointment-slots"]/div[{index}]/div') #Extra loop, in cazul in care ora inca nu s-a incarcat 
                for h in hour_list2:
                    browser.execute_script("arguments[0].scrollIntoView();", h)
            except StaleElementReferenceException:
                continue
            break
            
        options = WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="appointment-slots"]/div[{index}]/div')))
        WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="appointment-slots"]/div[{index}]/div'))).click()
        is_selected = options.is_enabled()
        
        if is_selected == True: 
            submit = browser.find_elements_by_xpath('//*[@id="submit-appointment"]')
            for s in submit :
                browser.execute_script("arguments[0].scrollIntoView();", s)
            WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-appointment"]'))).click()
            WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regulations-checkbox"]'))).click()
            WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirm-appointment"]'))).click()
            
            end = time.time()
            total_time = end - start
            print("\n"+ str(total_time))
        break
    elif hour != f"{ora_rezervarii}":
        arrow = browser.find_elements_by_xpath('//*[@id="specialists-select"]')
        for a in arrow:                                                                     #Acelasi lucru ca primul for loop doar ca da scroll inapoi daca nu gaseste ora
            browser.execute_script("arguments[0].scrollIntoView();", a)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="appointment-calendar"]/div[2]/div[3]'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="appointment-calendar"]/div[2]/div[1]'))).click()

        sleep(0.2)
        print(f'Last available hour {split[0][index-1]}')
        end = time.time()
        total_time = end - start
        print("Refresh time: "+ str(total_time) + " s")
    