# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class SicoesItem(scrapy.Item):
    nro = scrapy.Field()
    cuce = scrapy.Field()
    entidad = scrapy.Field()
    modalidad = scrapy.Field()
    nro_ctrl = scrapy.Field()
    nro_conv = scrapy.Field()
    objeto = scrapy.Field()
    estado = scrapy.Field()
    fecha_publi = scrapy.Field()
    fecha_presen = scrapy.Field()
    archivos = scrapy.Field()
    formularios = scrapy.Field()
