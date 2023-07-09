from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urlparse
# given url, download page in .txt file in /text directory
def download_text_from_url(url):

    print(url) # for debugging and to see the progress
    #  Parse the URL and get the domain
    local_domain = urlparse(url).netloc

    print(local_domain)
    # Create a directory to store the text files
    if not os.path.exists("text/"):
            os.mkdir("text/")
    if not os.path.exists("text/"+local_domain+"/"):
            os.mkdir("text/" + local_domain + "/")

    # Create a directory to store the csv files
    if not os.path.exists("processed"):
            os.mkdir("processed")

    # Save text from the url to a <url>.txt file
    with open('text/'+local_domain+'/'+url[8:].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
          
        # Get the text from the URL using BeautifulSoup
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        # Get the text but remove the tags
        text = soup.get_text()

        # If the crawler gets to a page that requires JavaScript, it will stop the crawl
        if ("You need to enable JavaScript to run this app." in text):
            print("Unable to parse page " + url + " due to JavaScript being required")
        
        # Otherwise, write the text to the file in the text directory
        f.write(text)


download_text_from_url("https://openai.com");
