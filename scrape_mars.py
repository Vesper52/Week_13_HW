
# coding: utf-8

# In[140]:

import time
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import re
import pandas as pd


# In[4]:





# In[6]:

def scrape():
    scrap_dict = {}
    url = "http://mars.nasa.gov/news/"
    r  = requests.get(url)
    time.sleep(1)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    news_p = (soup.find('div',{'class':'rollover_description_inner'}).getText())
    news_title = (soup.find('div',{'class':'content_title'}).getText())



    #Searching for the space image
    browser = Browser('chrome', headless=False)
    url = "http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.article['style']
    image_slim = re.findall(r"'(.*?)'", image)
    image_url = image_slim[0]
    featured_image_url =  "https://www.jpl.nasa.gov"+image_url



    #Searching Twitter
    url = "https://twitter.com/marswxreport?lang=en"
    r  = requests.get(url)
    time.sleep(1)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    mars_weather = (soup.find('p',{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).getText())




    #Pandas Scraping
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Planet Profile', 'Values']



    #Hemisphere Pictures
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    
    scrap_dict['news_title']= news_title
    scrap_dict['news paragraph'] = news_p
    scrap_dict['table']=df
    scrap_dict['mars pics']=hemisphere_image_urls
    return(scrap_dict)

