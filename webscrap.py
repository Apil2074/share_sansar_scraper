import requests
import bs4
from flask import Flask, jsonify


page=requests.get("https://www.sharesansar.com/today-share-price")

soup= bs4.BeautifulSoup(page.text,'lxml')

table=soup.find('table',id="headFixed")

headers=[ heading.text for heading in table.find_all('th')]

table_rows=[ row for row in table.find_all('tr')]

results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]




app = Flask(__name__)

@app.route('/')
def hello_world():
   return jsonify(results)

if __name__ == '__main__':
   app.run(debug = True)