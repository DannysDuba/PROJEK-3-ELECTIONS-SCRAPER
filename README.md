# PROJEKT-3-ELECTIONS-SCRAPER

Vítám Vás u třetího python projektu do Engeto akademie. :wave:

### POPIS PROJEKTU

Projekt election srapcer slouží k extrahování a třídění dat z parlamentních voleb České republiky z okresu:
[Jihlava](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102)


### INSTALACE KNIHOVEN

Použité knihovny pro tento projekt najdete v souboru `requirements.txt`. 
Aby jste mohli nainstalovat použité knihovny vytvořte si virtuální prostředí a nainstalujte balíčky:

`$ pip3 --version`  # ověření verze manažera 

`$ pip3 install -r requirements.txt` # instalace knihoven

### SPUŠTĚNÍ PROJEKTU

Aby jste mohli spustit soubor election.py, potřebujete k tomu 2 povinné argumenty.

`python election.py <"url uzemního celku"> <"soubor.csv">`


### UKÁZKA PROJEKTU

Výsledky pro hlasování pro okres Jihlava:

1. Argument: `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102`

2. Argument: `election_data.csv`

**SPUŠTĚNÍ PROGRAMU**

`python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102" "election_data.csv"`


**PRŮBĚH STAHOVÁNÍ**

`Downloading data from: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102`

`Saving data to: election_data.csv`

`Data was saved. Exiting program`


**UKÁZKA VÝSTUPU**

`Code,Location,Registered,Envelopers,Valid...
586854,Arnolec,133,96,96,13,0,0,9,0,2,9,0,1,1,0,0,5,0,0,37,0,9,2,0,2,0,6,0
586862,Batelov,1925,1244,1238,88,0,0,83,3,23,127,11,18,8,0,0,137,0,37,397,8,129,1,21,6,2,135,4`

**UKÁZKA ŠPATNĚ ZADANÝCH ARGUMENTŮ**

``

