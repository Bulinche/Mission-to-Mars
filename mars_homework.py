from splinter import browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd 

def init_browser():
    executable_path = {'executable_path': 'C:/Users/lhern/Documents/Github Original/12 - Web Scraping Homework/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

mars_web = {}
hemisphere_image_urls= []

def scrape_news():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news'
