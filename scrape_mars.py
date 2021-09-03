# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Create function for scraping all the data

def scrape_info():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ------------------------------------------------------
    # Scrape redplanetscience.com. for title and news snippet
    # ------------------------------------------------------

    # Set URL
    url='https://redplanetscience.com/'
    browser.visit(url)

    # Create browse session & store soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get all the article divs
    news = soup.find_all('div', class_='col-md-8')

    # Scrape News Titles and snippets

    titles = []
    news_p = []

    for new in news:
        title = new.find('div', class_='content_title').text
        news_ = new.find('div', class_='article_teaser_body').text
        titles.append(title)
        news_p.append(news_)

        print(title)
        print(news_)
        print('--------------------')

    browser.quit()

    return titles, news_p
    
    # ------------------------------------------------------
    # Scrape JPL Mars Space Images - Featured Image
    # ------------------------------------------------------

    # Set URL
    url_mars_image='https://spaceimages-mars.com/'
    browser.visit(url_mars_image)

    # Create browse session & store soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get all the article divs
    news = soup.find_all('div', class_='col-md-8')

    # Close the browser after scraping
    browser.quit()

    # Scrape current mars image
    scraped_url = soup.find('img', class_='thumbimg')['src']

    featured_image_url = f"https://spaceimages-mars.com/{scraped_url}"

    print(featured_image_url)

    # ------------------------------------------------------
    # Mars Facts: Visit mars facts website and scrape table of facts
    # ------------------------------------------------------

    # Set URL
    url ='https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Create browse session & store soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Scrap Tables
    tables = pd.read_html(url)
    
    # Convert Mars data to HTML
    df = tables[1]
    df = df.reset_index(drop=True)
    mars_html = df.to_html()
    mars_html.replace('\n','')
    mars_html

    # ------------------------------------------------------
    # Mars Hemisphers Scrape Astropedia Site
    # ------------------------------------------------------
    url='https://marshemispheres.com/'
    browser.visit(url)

    # Create list
    img_urls = []