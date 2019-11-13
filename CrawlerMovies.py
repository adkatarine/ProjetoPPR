import scrapy
import json

class MovieSpider(scrapy.Spider):
    name = "movieSpider"
    start_urls = ['https://www.ingresso.com/sao-paulo/home']
    informationsM = {}
    lista = []

    ''''''
    def parse(self, response):
        for movie in response.css('div.swiper-slide'):
            estreia = movie.css('article.card span.tag-genre').get()
            #Verifica se o 'filme' tem data de estreia
            if not estreia:
                date = movie.xpath('.//article/meta[re:test(@itemprop, "dateCreated")]/@content').get()
                sinopse = movie.xpath('.//article/meta[re:test(@itemprop, "description")]/@content').get()
                category = movie.css('article.card a::attr(onmousedown)').get()
                name = movie.css('article.card h1::text').get()
                imageM = movie.css('article.card img::attr(data-src)').get()
                yield {'date': date, 'sinopse': sinopse, 'category': category, 'name': name, 'imageM': imageM}
                #Colcoa as informações em um dicionário.
                x = {"name": name, "sinopse": sinopse, "category": category, "date": date, "imageM": imageM}
                self.lista.append(x) #Insere o dicionário em uma lista.
        self.saveJson()
    
    '''Salva as informações em um arquivo Json.'''
    def saveJson(self):
        self.informationsM['complet'] = self.lista
        with open("InformationsM.json", "w", encoding='utf-8') as outfile:
            json.dump(self.informationsM, outfile, ensure_ascii = False)