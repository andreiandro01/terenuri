# Terenuri footbal

### About

Beats the humans every time...  
### Requirements
- [Python 3.8.16](https://www.python.org/downloads/)
- [Spyder IDE (preffered)](https://www.spyder-ide.org/) 
- ~~Orice fel de Python script server (Raspberry Pi sau online)~~ sau Windows Task Scheduler daca e pornit local pe windows (**momentan merge doar local**)

## Required libraries
- Selenium 3.141.0 or higher :

         pip install selenium

- Webdriver manager 3.8.5 or higher:

          pip install webdriver-manager
          
- PySimpleGui: 
         
         pip install pysimplegui

- Apscheduler:
         
         pip install apscheduler
         
## Running the script
Ruleaza booker.py in Spyder sau orice IDE. Script-ul ruleaza folosind selenium si chrome driver instalat cu webdriver manager.
Nu am testat inca cu alt browser dar banuiesc ca functioneaza la fel.
GUI-ul e destul de simplu, trebuie introdus doar username, password si ora rezervarii si script-ul isi va creea un scheduled job
cu 6 min inainte de ora rezervarii (Ex. ora rezervarii 20:00, scriptul v-a porni la 19:54) dar **IDE-ul prin care e rulat script-ul trebuie sa 
ramana pornit** momentan.

 

## To do
- E-mail cu link-ul dupa ce programul completeaza rezervarea
- Optiune de a selecta alte sporturi inafara de fotbal (se poate face daca se modifica link-ul de la linia 27 (browser.get("https://www.calendis.ro/cluj-napoca/....")

## Known bugs
- Atunci cand toate orele din ziua in care se face rezervare sunt disponibile si script-ul incearca sa faca o rezervare la o ora din intervalul 18-20:00, butonul de confirmare a rezervarii se va bloca timp de cateva milisecunde. Script-ul va da fail daca incearca sa continue rezervarea in acel interval in care butonul este inactiv.
