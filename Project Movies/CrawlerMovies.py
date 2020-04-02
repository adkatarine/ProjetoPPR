import scrapy
from scrapy.crawler import CrawlerProcess
import DynamoDBPut as ddb
dynamodb = ddb.DynamoDBPut()
import CrawlerTwitter as ct
cTwitter = ct.CrawlerTwitter()

class MovieSpider(scrapy.Spider):
    name = "movieSpider"
    start_urls = ['https://www.ingresso.com/sao-paulo/home']
    lista = []

    '''Recebe a resposta da requisição(response) e realiza o parse para extração das informações sobre os filmes.'''
    def parse(self, response):
        for movie in response.css('div.swiper-slide'):
            date = movie.xpath('.//article/meta[re:test(@itemprop, "dateCreated")]/@content').get()
            director = movie.xpath('.//article/meta[re:test(@itemprop, "director")]/@content').get()
            sinopse = movie.xpath('.//article/meta[re:test(@itemprop, "description")]/@content').get()
            actors = movie.xpath('.//article/meta[re:test(@itemprop, "actors")]/@content').get()
            countryOfOrigin = movie.xpath('.//article/meta[re:test(@itemprop, "countryOfOrigin")]/@content').get()
            category = movie.css('article.card a::attr(onmousedown)').get()
            title = movie.css('article.card h1::text').get()
            imageM = movie.css('article.card img::attr(data-src)').get()
            classification = movie.css('article.card span.tag-classification::text').get()
            estreia = movie.css('article.card span.tag-genre').get()
            emCartaz = 'yes'
            #Verifica se o 'filme' tem data de estreia
            if estreia:
                emCartaz = 'no'
            
            yield {'director': director, 'classification': classification, 'sinopse': sinopse, 'category': category, 'title': title, 'imageM': imageM, 'date': date, 'actors': actors, 'countryOfOrigin': countryOfOrigin, 'emCartaz': emCartaz}
            
            #Coloca as informações em um dicionário.
            x = {"director": director, "classification": classification, "title": title, "sinopse": sinopse, "category": category, "imageM": imageM, "date": date, "actors":actors, "countryOfOrigin": countryOfOrigin, "emCartaz": emCartaz}
            self.lista.append(x) #Insere o dicionário em uma lista.
        #dynamodb.addMovies(self.lista)
        #cTwitter.getTitleMoviesDynamodb()
        #cTwitter.tweetStream()
if __name__ == '__main__':
      process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'InformationsMoviesNew.json'
    })
      process.crawl(MovieSpider)
      process.start()