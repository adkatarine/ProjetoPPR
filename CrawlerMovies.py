import scrapy
from scrapy.crawler import CrawlerProcess

class MovieSpider(scrapy.Spider):
    name = "movieSpider"
    start_urls = ['https://www.ingresso.com/sao-paulo/home']

    '''Recebe a resposta da requisição(response) e realiza o parse para extração das informações sobre os filmes.'''
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

if __name__ == '__main__':
    '''Salva as informações em um arquivo Json.'''
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'InformationsMovies.json'
    })
    
    process.crawl(MovieSpider)
    process.start()