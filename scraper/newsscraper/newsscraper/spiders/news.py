import scrapy 
import re
import unidecode
from newspaper import fulltext
import requests

# running: scrapy crawl ndtv -o ndtv_articles.json

class ndtvSpider(scrapy.Spider):
    name = 'ndtv'	

    # def start_requests(self):
        
    start_urls = [
        'https://www.ndtv.com/top-stories'
    ]


                
    def parse(self, response):
        for article in response.xpath("//h2[@class='newsHdng']"):
            

            ##### HEADLINE
            headline=article.xpath("normalize-space(.//a/text())").extract_first()

            ##### LINK
            link=article.xpath(".//a/@href").extract_first()

            ##### Article
            article = fulltext(requests.get(link).text)


            yield {
                'headline' : headline,
                'link' : link,
                'article': article,

            }
