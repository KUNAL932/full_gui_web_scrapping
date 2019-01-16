from bs4 import BeautifulSoup
import requests
import pandas as pd

def startScrapping():

    website_address="http://books.toscrape.com"
    result=requests.get(website_address,verify=False)
    name_list=[]
    price_list=[]
    book_id=[]
    book_dict={}


    soup=BeautifulSoup(result.text,"html.parser")
    books=soup.findAll("article",{"class":"product_pod"})
    i=1
    for book in books:
        name=book.findAll("a")[1].attrs['title']
        # print(name)
        name_list.append(name)
        price=book.find("p",{"class":"price_color"}).text[2:]
        # print(price)
        price_list.append(price)
        book_id.append(i)
        i=i+1
        # displayedlabel=book.find("h1").text
        # print(displayedlabel)
        # for i in book:


        #     name=i.findAll("a")[1].attrs['title']
    #     #     print(name)
    # single_book = soup.find("div", {"class":"image_container"})
    # book_link = single_book.find("a").get("href")
    # address = website_address+"/"+book_link
    #
    # book_result=requests.get(address,verify=False)
    #
    # book_soup=BeautifulSoup(book_result.text,"html.parser")
    #
    # list_var = book_soup.find("ul", {"class":"breadcrumb"})
    # # link = list_var.findAll("li")

    book_dict["Book Name"]=name_list
    book_dict["Book Price"]=price_list
    book_dict["BOOK_ID"]=book_id


    data=pd.DataFrame(data=book_dict)
    data=data.set_index("BOOK_ID")
    data=data.to_csv("poetry_book.csv")
    print(data)








