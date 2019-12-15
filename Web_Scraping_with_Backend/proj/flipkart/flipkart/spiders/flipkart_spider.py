# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = ['https://www.flipkart.com/mens-clothing/pr?sid=2oq,s9b&otracker=categorytree&otracker=nmenu_sub_Men_0_Clothing']

    def parse(self, response):
        items=FlipkartItem()

        prod_name = response.css('._2mylT6::text').extract()
        prod_price= response.css('._1vC4OE::text').extract()
        prod_brand =response.css('._2B_pmu::text').extract()
        prod_image=response.css('._3togXc::attr(src)').extract()
        
        items['prod_name']=prod_name
        items['prod_price']=prod_price
        items['prod_brand']=prod_brand
        items['prod_image']=prod_image

        yield items