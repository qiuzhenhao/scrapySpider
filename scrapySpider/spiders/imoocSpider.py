
import scrapy
from scrapySpider.items import ScrapyspiderItem

class ImoocSpider(scrapy.Spider):

    name = "ImoocSpider"
    allowed_domains = ["imooc.com"]
    start_urls = ['http://www.imooc.com/course/list']

    def __init__(self):
        self.count = 0


    def parse(self, response):
        # 所有图片的地址
        imgArr = []

        # 实例一个容器保存爬取的信息
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
            item = ScrapyspiderItem()
            # 获取div中的课程标题
            item['title'] = box.xpath('.//div[@class="course-card-content"]/h3/text()').extract()[0].strip()
            # 获取课程的标签
            try:
                item['label'] = ','.join(box.xpath('.//div[@class="course-label"]/label/text()').extract())
            except:
                item['label'] = ""

            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # 获取div中的标题图片地址
            item['image_url'] = 'http:'+box.xpath('.//div[@class="course-card-top"]/img/@src').extract()[0]
            # 获取课程的等级
            item['level'] = box.xpath('.//div[@class="course-card-info"]/span/text()').extract()[0].strip()
            # 获取div中的学生人数
            item['student_count'] = box.xpath('.//div[@class="course-card-info"]/span/text()').extract()[1].strip()
            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            imgArr.append(item['image_url'])
            item['img_arr'] = imgArr
            # 返回信息
            yield item

        # url跟进开始
        # 获取下一页的url信息
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url:
            # 将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            self.count = self.count + 1
            print(self.count)
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
