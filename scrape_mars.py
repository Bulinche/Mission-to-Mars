#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import json
import re
from pprint import pprint
from selenium import webdriver
import time


# In[2]:

def scrape():

    executable_path = {'executable_path': 'C:/Users/lhern/Documents/Github Original/12 - Web Scraping Homework/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

# create a dictionary for all of the scraped data
    mars_data = {}
    hemisphere_image_urls = []

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


# In[3]:


# Retrieving the news title
    
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    article = soup.find("div", class_="list_text")
    date = article.find("div", class_="list_date").text
    news_title = article.find('div', class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text
#print(news_title)

# adding the date, title and paragraph body to dictionary
    mars_data["date"] = date
    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    

# In[4]:


#news_p = soup.find('div', class_="article_teaser_body").text
#print (news_p)


# In[5]:


    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html_image = browser.html
    soup = BeautifulSoup(html_image,'html.parser')

    featured_image_url = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))

    main_url = 'https://www.jpl.nasa.gov'

    image = main_url + featured_image_url

    mars_data['image'] = image


# In[8]:


# Mars Weather Twitter Account

    weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_twitter_url)
    time.sleep(2)
    html_weather = browser.html
    soup = BeautifulSoup(html_weather,'html.parser')

    mars_weather = soup.find("div", {"data-testid":"tweet"}).find('div',{"lang":"en"}).find('span').text
    mars_data [mars_weather] = mars_weather

# In[11]:


    url = 'http://space-facts.com/mars/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html,'html.parser')
    tables_df = ((pd.read_html(url))[0]).rename(columns={0:"Attribute", 1:"Value"}).set_index(['Attribute'])
    html_table = (tables_df.to_html()).replace('\n','')

    mars_data['html_table'] = html_table
# In[12]:
    weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_twitter_url)
    time.sleep(2)

    html_weather = browser.html
    soup = BeautifulSoup(html_weather,'html.parser')

    mars_weather = soup.find("div", {"data-testid":"tweet"}).find('div',{"lang":"en"}).find('span').text
    mars_data['mars_weather'] = mars_weather

#mars_weather

#mars_facts = pd.read_html(facts_url)

#mars_df = mars_facts[0]

#mars_df


# In[14]:


#mars_facts_html= mars_facts[0].to_html()
#mars_facts_html


# In[15]:

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title":"Schiaparelli Hemisphere","img_url": schiaparelli_url}])

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title":"Syrtis Major Hemisphere","img_url": syrtis_major_url}])

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    valles_marineries_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title":"Valles Marineris Hemisphere","img_url": valles_marineries_url}])

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    cerberus_marineries_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title":"Cerberus Hemisphere Enhanced","img_url": cerberus_marineries_url}])

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    browser.quit()
    return mars_data


#hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#browser.visit(hemispheres_url)


# In[16]:


#html_hemispheres = browser.html

#soup = BeautifulSoup(html_hemispheres, 'html.parser')
#hemispheres_img_urls = []

# In[17]:



#items = soup.find_all('div',class_='item')

#hemisphere_image_urls=[]
#hemispheres_main_url='https://astrogeology.usgs.gov'

#for item in items:
    #title=item.find('h3').text
    #image_url = item.find('a', class_='itemLink product-item')['href']
    #browser.visit(hemispheres_main_url + image_url)
    #image_html = browser.html
    #soup = BeautifulSoup (image_html,'html.parser')
    #image_url=hemispheres_main_url+soup.find('img',class_='wide-image')['src']
    #hemisphere_image_urls.append({"Title" : title, "Image_URL" : image_url})
#hemisphere_image_urls


# In[ ]:




