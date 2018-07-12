# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class BackSpiderSpider(scrapy.Spider):
    name = 'back-spider'
    allowed_domains = ['backpackers.com.tw']
    start_urls = ['https://www.backpackers.com.tw/forum/forumdisplay.php?f=25']
    count = 0
    def parse(self, response):
	    while count<3:
	    	form  = response.xpath('//tbody[starts-with(@id,"threadbits")]') 
	    	trs = form.xpath('.//tr')


	    	for tr in trs:
	    		if tr.xpath('.//td[@colspan]//ins[@class]').extract_first() is not None:
	    			pass
	    		else:
	    			title = tr.xpath('.//td[starts-with(@id,"td_threadtitle_")]//a[starts-with(@href,"showthread")]//text()').extract_first()
	    			last_reply = tr.xpath('.//td[starts-with(@title,"回覆")]/div[@class="smallfont"]/text()').extract_first().lstrip()
	    			num_of_reply = tr.xpath('.//td[@class = "alt1 smallfont"]/text()').extract_first()
	    			num_of_view = tr.xpath('.//td[@class = "alt2 smallfont"]/text()').extract_first()


	    		yield{'title':title,
					  'last_reply':last_reply,
					  'num_of_reply':num_of_reply,
					  'num_of_view':num_of_view}


	    	if response.xpath('//td//a[@rel="next"]/@href').extract_first():
	    		next_btn_url = response.xpath('//td//a[@rel="next"]/@href').extract_first()
	    		absolute_next_btn_url = response.urljoin(next_btn_url)
	    	count+=1
    	yield Request(absolute_next_btn_url, callback = self.parse)


    		# 	yield{'title':title,
    		# 		  'last_reply':last_reply}
    			


    


    		
    		




        
