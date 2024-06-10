import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint
import json

from constantes import BASE_URL

def get_matrixe_techniques(session, url):
    response = session.get(url)  
    if response.status_code == 200:
        print("opéraion réussi")
        return response.text
    return None

def matrix_table_parser(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.select("table.matrix.side thead tr td.name a")

def pars_Tactic(tag):
    return [tag.text, tag.get("title")]
    
def get_description(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.select(".description-body p") 

def get_technique_id(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.select('tr.technique td[colspan="2"] a')

def get_name(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.select('.container-fluid h1')[0].text.strip()

def get_sub_technique_id(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.select('.card-body .row div')[3].select("a")





def matrix_data(content_page):
    bag_tactic = []
    bag_technique = []
    bag_sub_technique = []
    
    for tag1 in matrix_table_parser(content_page):
        absolute_link = urljoin(BASE_URL, f"/tactics/{pars_Tactic(tag1)[1]}")
        tactic_data = get_matrixe_techniques(session, absolute_link)

        tactic_description = [tag.text for tag in get_description(tactic_data)]
        bag_tactic.append({
            "tactic-name": pars_Tactic(tag1)[0],
            "tactic-ID": pars_Tactic(tag1)[1],
            "tactic": tactic_description,
        })

        technique_data_dict = {}
        for tag2 in get_technique_id(tactic_data):
            technique_absolute_link = urljoin(BASE_URL, f"/techniques/{tag2.text.strip()}/")
            technique_data = get_matrixe_techniques(session, technique_absolute_link)

            technique_description = [tag.text for tag in get_description(technique_data)]
            technique_data_dict[tag2.text.strip()] = {
                "technique-name": get_name(technique_data),
                "technique-ID": tag2.text.strip(),
                "technique-description": technique_description,
                "tactic-ID": pars_Tactic(tag1)[1]
            }

            sub_technique_data_dict = {}
            for tag3 in get_sub_technique_id(technique_data):
                slug = tag3.text.strip().split(".")[1]
                sub_tech_absolute_link = urljoin(technique_absolute_link, f"{slug}")
                sub_tech_data = get_matrixe_techniques(session, sub_tech_absolute_link)

                sub_technique_data_dict[slug] = {
                    "number": slug,
                    "sub-technique-name": get_name(sub_tech_data).split(":")[1].strip(),
                    "sub-technique-description": [tag.text for tag in get_description(sub_tech_data)],
                    "technique-ID": tag2.text.strip()
                }

            bag_sub_technique.extend(sub_technique_data_dict.values())

        bag_technique.extend(technique_data_dict.values())

    return (bag_tactic, bag_technique, bag_sub_technique)

with requests.Session() as session:
    a = get_matrixe_techniques(session, BASE_URL)
    tactic_data, technique_data, sub_technique_data = matrix_data(a)

    with open("tactic.json", 'w', encoding='utf-8') as f:
        json.dump(tactic_data, f, indent=4)

    with open("technique.json", 'w', encoding='utf-8') as f:
        json.dump(technique_data, f, indent=4)

    with open("sub-technique.json", "w", encoding='utf-8') as f:
        json.dump(sub_technique_data, f, indent=4)
