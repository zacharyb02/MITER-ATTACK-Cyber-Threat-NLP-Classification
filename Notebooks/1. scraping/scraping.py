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
    for tag1 in matrix_table_parser(content_page):
        bag_technique = []
        absolute_link = urljoin(BASE_URL, f"/tactics/{pars_Tactic(tag1)[1]}")
        tactic_data = get_matrixe_techniques(session, absolute_link)

        # pprint([tag.text for tag in get_tactic_description(tactic_data)])
        print("=======================================")
        # bag_tactic.append([tag.text for tag in get_technique_name_id(tactic_data)])
        for tag2 in get_technique_id(tactic_data):
            
            technique_absolute_link = urljoin(BASE_URL, f"/techniques/{tag2.text.strip()}/")
            technique_data = get_matrixe_techniques(session,technique_absolute_link)
            
            bag_sub_technique = []
            print('==========')
            for tag3 in get_sub_technique_id(technique_data):
                slug = tag3.text.strip().split(".")[1]
                sub_tech_absolute_link = urljoin(technique_absolute_link, f"{slug}")
                sub_tech_data = get_matrixe_techniques(session, sub_tech_absolute_link)
                
                bag_sub_technique.append([{
                    "number": slug,
                    "sub-technique-name": get_name(sub_tech_data).split(":")[1].strip(),
                    "sub-technique-description": [tag.text for tag in get_description(sub_tech_data)]
                }])

            pprint(bag_sub_technique)
            print('==========')
            bag_technique.append([{
                    "technique-name": get_name(technique_data),
                    "technique-ID": tag2.text.strip(),
                    "technique-description":[tag.text for tag in get_description(technique_data)],
                    "sub-technique":bag_sub_technique
                }])
        print('==========')
        pprint(bag_technique)
        bag_tactic.append(
                {
            "tactic-name": pars_Tactic(tag1)[0],
            "ID":pars_Tactic(tag1)[1],
            "tactic": [tag.text for tag in get_description(tactic_data)],
            "technique" : bag_technique
        })

        
        
    return bag_tactic

with requests.Session() as session :
    a = get_matrixe_techniques(session, BASE_URL)
    
    
    with open("tactic.json", 'w', encoding='utf-8') as f:
            json.dump(matrix_data(a), f, indent=4)
    
    