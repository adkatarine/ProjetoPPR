import scrapy
from scrapy.crawler import CrawlerProcess
import DynamoDBPut as ddb
dynamodb = ddb.DynamoDBPut()

class MovieSpider(scrapy.Spider):
    name = "movieSpider"
    start_urls = ['https://www.ingresso.com/sao-paulo/home']
    lista = []
    
    '''Recebe a resposta da requisição(response) e realiza o parse para extração das informações sobre os filmes.'''
    def parse(self, response):
        for movie in response.css('div.swiper-slide'):
            estreia = movie.css('article.card span.tag-genre').get()
            #Verifica se o 'filme' tem data de estreia
            if not estreia:
                date = movie.xpath('.//article/meta[re:test(@itemprop, "dateCreated")]/@content').get()
                sinopse = movie.xpath('.//article/meta[re:test(@itemprop, "description")]/@content').get()
                category = movie.css('article.card a::attr(onmousedown)').get()
                title = movie.css('article.card h1::text').get()
                imageM = movie.css('article.card img::attr(data-src)').get()
                yield {'date': date, 'sinopse': sinopse, 'category': category, 'title': title, 'imageM': imageM}
                #Coloca as informações em um dicionário.
                x = {"title": title, "sinopse": sinopse, "category": category, "date": date, "imageM": imageM}
                self.lista.append(x) #Insere o dicionário em uma lista.
        dynamodb.addMovies(self.lista)
                
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(MovieSpider)
    process.start()