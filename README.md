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
## Running the script
Ruleaza beer_generator.py in Spyder sau orice IDE. Script-ul ruleaza folosind selenium si chrome driver instalat cu webdriver manager.
Nu am testat inca cu alt browser dar banuiesc ca functioneaza la fel.

Parametrii configurabili:
 - username (in cazul in care nu vrei sa rulezi programul cu default user beergenerator2@gmail.com)
 - password (in cazul in care nu vrei sa rulezi programul cu default user)
 - ora_rezervarii --> Ora de la care o sa fie facuta rezervarea
 

## To do
- E-mail cu link-ul dupa ce programul completeaza rezervarea
- Optiune de a pre-configura paramaterii si un batch script care poate fi utilizat la automatizare (In stadiul curent poate fi rulat doar local)
- Optiune de a selecta alte sporturi inafara de fotbal (se poate face daca se modifica link-ul de la linia 27 (browser.get("https://www.calendis.ro/cluj-napoca/....") 
