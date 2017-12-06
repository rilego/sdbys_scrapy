import re
import scrapy  # 导入scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request  ##一个单独的reques模块，用来跟进url
from sdbys.items import SdbysItem  ##定义要保存的字段，（导入sdbys项目中，itmes文件的SdbysTtem类）
import time


class Myspider(scrapy.Spider):
    name = 'sdbys'
    allowed_domains = ['www.sdbys.cn']
    # http://www.sdbys.cn/platform/topic/display/searchStudentInfoNewAction_.action?pagingPage=2&pagingNumberPer=20
    bash_url = 'http://www.sdbys.cn/platform/topic/display/searchStudentInfoNewAction_.action?pagingNumberPer=20&searchTime=7&pagingPage='

    def start_requests(self):
        for i in range(1, 4):
            url = self.bash_url + str(i)
            yield Request(url, callback=self.get_line)
            time.sleep(10)

    def get_line(self, response):
        Soup = BeautifulSoup(response.text, 'lxml')
        all_line = Soup.find('table', class_='classicLook').find_all('a')
        line = 0  ##每一页行数重置
        for a in all_line:
            name = a.get_text().strip()  # 取出a标签的文本
            guid = a['href'][95:131]  # 取出链接中的guid
            xueli_num = line * 7 + 1
            zytype_num = line * 7 + 2
            school_num = line * 7 + 3
            year_num = line * 7 + 4
            sex_num = line * 7 + 5
            time_num = line * 7 + 6
            xueli = Soup.find('table', class_='classicLook').find_all('td')[xueli_num].string.strip()
            zytype = Soup.find('table', class_='classicLook').find_all('td')[zytype_num].string.strip()
            school = Soup.find('table', class_='classicLook').find_all('td')[school_num].string.strip()
            year = Soup.find('table', class_='classicLook').find_all('td')[year_num].string.strip()
            sex = Soup.find('table', class_='classicLook').find_all('td')[sex_num].string.strip()
            posttime = Soup.find('table', class_='classicLook').find_all('td')[time_num].string.strip()
            line += 1  ##控制行移动
            # print(name, xueli, zytype, school, year, sex, time, guid)
            item = SdbysItem()
            item['name'] = name
            item['xueli'] = xueli
            item['zhuanye'] = zytype
            item['school'] = school
            item['year'] = year
            item['sex'] = sex
            item['time'] = posttime
            item['guid'] = guid
            yield item
