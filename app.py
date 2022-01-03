# Importing the necessary libraries
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

# Flask app
app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():

    # Web Scraping
    url = "https://www.businesstoday.in/latest/economy"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    outer_data = soup.find_all("div",class_ = "widget-listing", limit=6)
    final_news = ""
    for data in outer_data:
        news = data.div.div.a["title"]
        final_news += "\u2022 " + news + "\n"
    #print(final_news)

    return render_template("index.html", News = final_news)

if __name__ == "__main__":
    app.run(debug = True)

