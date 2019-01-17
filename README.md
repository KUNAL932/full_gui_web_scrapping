# Web scrapping + SQLITE3 database connectivity + GUI in Tkinter 

a gui program used to scrap a particular website and adding the required data to a CSV file with actions of buttons 

## Screenshots

#### Homepage
![alt homepage](https://kunal932.github.io/full_gui_web_scrapping/Home%20Page.png)

#### Scrapping Data
![alt scrapping](https://kunal932.github.io/full_gui_web_scrapping/Scrapping%20Data.png)

#### Load Data into database
![alt load-data](https://kunal932.github.io/full_gui_web_scrapping/Loading%20Data.png)

#### Show Data into Tree View
![alt show-data](https://kunal932.github.io/full_gui_web_scrapping/Loading%20Data.png)

#### Database
![alt database](https://kunal932.github.io/full_gui_web_scrapping/Database.png)

## Coding Snippets

#### Web Scrapping using BeautifulSoup
```
website_address="http://books.toscrape.com"
result=requests.get(website_address,verify=False)
soup=BeautifulSoup(result.text,"html.parser")
books=soup.findAll("article",{"class":"product_pod"})
```

#### Database using SQLite
```
table_query="CREATE TABLE IF NOT EXISTS "+TABLE_NAME+" \
                 ("+TABLE_ID+" INTEGER PRIMARY KEY AUTOINCREMENT, "+BOOK_NAME+" TEXT, "+BOOK_PRICE+" TEXT); "
database.execute(table_query)
```

#### GUI using Tkinter
```
root=tk.Tk()
root.title("web_scrapp_gui")

displayLabel=tk.Label(root,text="web scrapper",font=("Helvetica", 16))
displayLabel.pack()
```

#### Load and Fetch data to/from database performed using Thread
```
ThreadTask("load").start()

Class ThreadTask(Thread):
    def __init__(self,value):
        Thread.__init__(self)
        self.value=value
```

