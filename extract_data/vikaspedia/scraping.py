import requests
from bs4 import BeautifulSoup


def get_diseases(main_title,sub_title,content):
    start = 0
    end = 3
    for index,title in enumerate(main_title[1:]):
        print (title)
        for i in range(start,end):
            print(sub_title[i])
            print(content[i])
        
        start+=3
        end+=3
        if end > len(sub_title) : end = len(sub_title)

def get_pest_insects(main_title,sub_title,content):
    i_main=0
    for index,item in enumerate(sub_title):
        if item == "Biology":
            print(main_title[i_main])
            i_main+=1
        print(item)
        print(content[index])

def get_main_titl_list(bsoup):
    main_title = bsoup.find_all("h3")
    main_title =[item.text.strip() for item in main_title[1:]]
    return main_title

def get_sub_title_list(bsoup):
    sub_title = bsoup.find_all("strong")
    sub_title = [item.text.strip() for item in sub_title if ":" not in item.get_text(strip=True)]
    return sub_title

def get_content_list(bsoup):
    content = bsoup.find_all("ul")
    content = [content_item.text.strip() for content_item in content if content_item.text.strip() !='']

url_diseases="https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-diseases-and-symptoms"
url_pests ="https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-insect-pests-management"

response = requests.get(url_pests)

bsoup = BeautifulSoup(response.text, 'html.parser')

main_title = get_main_titl_list(bsoup)

sub_title = get_sub_title_list(bsoup)

content = get_content_list(bsoup)

get_pest_insects(main_title,sub_title,content)


