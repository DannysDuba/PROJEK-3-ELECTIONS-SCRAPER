"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Daniel Duba
email: duba.danny@gmail.com
discord: DannysDuba#3102
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys

base_url = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=10&xobec="


def response_server(url):
    """Tato funkce získává a parsuje data z požadovaného url"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def location(soup):
    """Tato funkce získává všechny názvy měst z vybraného okresu"""
    city_names = soup.find_all("td", {"class": "overflow_name"})
    cities = [city.text for city in city_names]
    return cities


def codes(soup):
    """Tato funkce získává všechny kódy měst z vybraného okresu"""
    city_codes = soup.find_all("td", {"class": "cislo"})
    code_text = [code.text for code in city_codes]
    return code_text


def parties(soup, code_text):
    """Tato funkce vytáhne všechny názvy volebních stran"""

    for code in code_text:
        url = base_url + code
        soup = response_server(url)
        parties_name = soup.find_all("td", {"class": "overflow_name", "headers": ["t1sa1 t1sb2", "t2sa1 t2sb2"]})
        parties_text = [party.text for party in parties_name]
        return parties_text


def csv_table(parties_text, datas, file_name):
    """Tato funkce zapíše požadované údaje do csv tabulky"""

    fields = ['Code', 'Location', 'Registered', 'Envelopers', 'Valid'] + parties_text
    with open(file_name, 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, dialect="excel",)
        print(f"Saving data to: {file_name}")
        writer.writeheader()
        for row in datas:
            writer.writerow(row)


def arguments():
    """Tato funkce kontroluje platné argumenty, aby mohl být program spuštěn."""

    if len(sys.argv) != 3:
        print(f"Program need 2 arguments to run. URL, CSV file. Exiting program.")
        sys.exit()

    if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print(f"First argument  is not correct. Exiting program.")
        sys.exit()

    if not sys.argv[2].endswith(".csv"):
        print(f"Second argument  is not correct. Exiting program.")
        sys.exit()

    else:
        print(f"Downloading data from: {sys.argv[1]} ")


def data(code_text, cities, parties_text):
    """Tato funkce stahuje a třídí data (registered, envelopers, valid a hlasy stran) do hlavní tabulky."""

    data_all = []
    for code, party in zip(code_text, cities):
        url = base_url + code
        soup = response_server(url)
        registered = int(soup.find("td", {"class": "cislo", "headers": "sa2"}).
                         text.replace(" ", "").replace('\xa0', ''))
        envelopers = int(soup.find("td", {"class": "cislo", "headers": "sa3"}).
                         text.replace(" ", "").replace('\xa0', ''))
        valid = int(soup.find("td", {"class": "cislo", "headers": "sa6"}).text.replace(" ", "").replace('\xa0', ''))
        votes = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        votes_text = [vote.text.replace(" ", "").replace('\xa0', '') for vote in votes]

        row = {'Code': code, 'Location': party, 'Registered': registered, 'Envelopers': envelopers, 'Valid': valid}
        for partys, vote in zip(parties_text, votes_text):
            row[partys] = vote
        data_all.append(row)
    return data_all


def main():
    """Hlavní funkce pro spuštění skriptu."""
    arguments()
    url = sys.argv[1]
    csv_file = sys.argv[2]
    soup = response_server(url)
    cities = location(soup)
    code_text = codes(soup)
    parties_text = parties(soup, code_text)
    data_main = data(code_text, cities, parties_text)
    csv_table(parties_text, data_main, csv_file)

    print(f"""Data was saved. Exiting program""")


if __name__ == '__main__':
    main()
