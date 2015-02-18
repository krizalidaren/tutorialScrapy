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
            item['nro'] = sel.xpath('td/text()').extract()
            item['cuce'] = sel.xpath('td/text()').extract()
            item['entidad'] = sel.xpath('td/text()').extract()
            item['modalidad'] = sel.xpath('td/text()').extract()
            item['nro_ctrl'] = sel.xpath('td/text()').extract()
            item['nro_conv'] = sel.xpath('td/text()').extract()
            item['objeto'] = sel.xpath('td/text()').extract()
            item['estado'] = sel.xpath('td/text()').extract()
            item['fecha_publi'] = sel.xpath('td/text()').extract()
            item['fecha_presen'] = sel.xpath('td/text()').extract()
            # item['archivos'] = sel.xpath('td/text()').extract()
            # item['formularios'] = sel.xpath('td/text()').extract()
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