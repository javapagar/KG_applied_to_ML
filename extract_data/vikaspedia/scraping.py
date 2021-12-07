import requests
from bs4 import BeautifulSoup
import os


def write_diseases(main_title,sub_title,content,data_path):
    start = 0
    end = 3
    with open(os.path.join(data_path,'disease.txt'),'w',encoding='utf8') as f:
        for index,title in enumerate(main_title[1:]):
            print (title)
            f.write(title+"\n")
            for i in range(start,end):
                print(sub_title[i])
                f.write(sub_title[i]+"\n")
                print(content[i])
                f.write(content[i]+"\n")
            
            start+=3
            end+=3
            if end > len(sub_title) : end = len(sub_title)

def write_pest_insects(main_title,sub_title,content,data_path):
    i_main=0
    with open(os.path.join(data_path,'pest.txt'),'w',encoding='utf8') as f:
        for index,item in enumerate(sub_title):
            if item == "Biology":
                print(main_title[i_main])
                f.write(main_title[i_main]+"\n")
                i_main+=1
            print(item)
            f.write(item+"\n")
            print(content[index])
            f.write(content[index]+"\n")

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
    return content

def create_pest_file(data_path):
    url_pests ="https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-insect-pests-management"

    response = requests.get(url_pests)

    bsoup = BeautifulSoup(response.text, 'html.parser')

    main_title = get_main_titl_list(bsoup)

    sub_title = get_sub_title_list(bsoup)

    content = get_content_list(bsoup)

    write_pest_insects(main_title,sub_title,content,data_path)

def create_diseases_file(data_path):
    url_diseases="https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-diseases-and-symptoms"
    
    response = requests.get(url_diseases)

    bsoup = BeautifulSoup(response.text, 'html.parser')

    main_title = get_main_titl_list(bsoup)

    sub_title = get_sub_title_list(bsoup)

    content = get_content_list(bsoup)

    write_diseases(main_title,sub_title,content,data_path)


if __name__ == "__main__":
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_path,"data")
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    create_diseases_file(data_path)
    create_pest_file(data_path)