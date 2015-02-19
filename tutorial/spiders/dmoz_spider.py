import scrapy

from tutorial.items import SicoesItem

class SicoesSpider(scrapy.Spider):
    name = "sicoes"
    allowed_domains = ["sicoes.gob.bo"]
    start_urls = [
        "https://www.sicoes.gob.bo/contrat/procesos.php"
    ]

    def parse(self, response):
        for sel in response.xpath('//tr'):
            item = SicoesItem()
            item['nro'] = sel.xpath('td[1]/text()').extract()
            item['cuce'] = sel.xpath('td[2]/text()').extract()
            item['entidad'] = sel.xpath('td[3]/text()').extract()
            item['modalidad'] = sel.xpath('td[4]/text()').extract()
            item['nro_ctrl'] = sel.xpath('td[5]/text()').extract()
            item['nro_conv'] = sel.xpath('td[6]/text()').extract()
            item['objeto'] = sel.xpath('td[7]/text()').extract()
            item['estado'] = sel.xpath('td[8]/div/text()').extract()
            item['fecha_publi'] = sel.xpath('td[9]/text()').extract()
            item['fecha_presen'] = sel.xpath('td[10]/text()').extract()
            item['archivos'] = sel.xpath('td[11]/a/@onclick').extract()
            item['formularios'] = sel.xpath('td[12]/a/@onclick').extract()
            yield item



# import scrapy
#
# from tutorial.items import DmozItem
#
# class DmozSpider(scrapy.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]
#
#     # def parse(self, response):
#     #     filename = response.url.split("/")[-2]
#     #     with open(filename, 'wb') as f:
#     #         f.write(response.body)
#     # def parse(self, response):
#     #     for sel in response.xpath('//ul/li'):
#     #         title = sel.xpath('a/text()').extract()
#     #         link = sel.xpath('a/@href').extract()
#     #         desc = sel.xpath('text()').extract()
#     #         print title, link, desc
#     def parse(self, response):
#         for sel in response.xpath('//ul/li'):
#             item = DmozItem()
#             item['title'] = sel.xpath('a/text()').extract()
#             item['link'] = sel.xpath('a/@href').extract()
#             item['desc'] = sel.xpath('text()').extract()
#             yield item