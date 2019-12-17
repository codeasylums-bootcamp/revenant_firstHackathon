# -*- coding: utf-8 -*-
import scrapy
import sqlite3
import pandas as pd

from ..items import FlipkartItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = ['https://www.flipkart.com/men/shirts/pr?sid=2oq%2Cs9b%2Cmg4&otracker=nmenu_sub_Men_0_Shirts&page=1']

    def parse(self, response):
        #items=FlipkartItem()
        prod_brand =response.css('._2B_pmu::text').extract()
        prod_name = response.css('._2mylT6::text').extract()
        prod_price= response.css('._1vC4OE::text').extract()
        prod_discount =response.css('._2W-UZw span::text').extract()

       # dicti={'prodname':prod_name,'prod_price':prod_price,'prod_brand':prod_brand}
        #print("My dicti vhudfh uhhg ",dicti)
        for i in range(0,50):
            items=FlipkartItem()
            
            items['prod_brand']=prod_brand[i]
            items['prod_name']=prod_name[i]
            items['prod_price']=prod_price[i]
            items['prod_discount']=prod_discount[i]


            yield items
    
    
        #df=pd.DataFrame(dicti)
        #df.to_csv('siip.csv')
        
