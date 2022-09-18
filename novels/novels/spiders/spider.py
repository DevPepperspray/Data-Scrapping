import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        all_the_books = response.xpath('//article')

        for book in all_the_books:
            # title = book.xpath('.//h3/a/@title').extract_first()
            # price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            # image_url = self.start_urls[0] + book.xpath('.//a/img/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
            yield scrapy.Request(book_url, callback=self.parse_book)


            

            # yield {
            #     'Title' : title,
            #     'Price' : price,
            #     'Image URL' : image_url,
            #     'Post URL' : book_url,
            # }
    def parse_book(self, response):
        title = response.xpath('.//h1/text()').extract_first()
        price = response.xpath('.//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract()
        stock = response.xpath('.//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()').extract()[1].strip()
        star = response.xpath('.//div[contains(@class, "product_main")]/p[contains(@class, "star-rating")]/i/@class').extract_first().replace('star-rating ', '')
        description = response.xpath('.//div[@id="product_description"]/following-sibling::p/text()').extract_first()
        upc = response.xpath('.//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
        product_type = response.xpath('.//table[@class="table table-striped"]/tr[2]/td/text()').extract_first()
        price_exclud_tax = response.xpath('.//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
        price_includ_tax = response.xpath('.//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
        tax = response.xpath('.//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()
        availability = response.xpath('.//table[@class="table table-striped"]/tr[6]/td/text()').extract_first()
        reviews = response.xpath('.//table[@class="table table-striped"]/tr[7]/td/text()').extract_first()

        yield {
                'Title' : title,
                'Price' : price,
                'Stock' : stock,
                'Star' : star,
                'Description' : description,
                'Upc' : upc,
                'Product type' : product_type,
                'Price excluding tax' : price_exclud_tax,
                'Price including tax' : price_includ_tax,
                'Tax' : tax,
                'Availability' : availability,
                'Reviews' : reviews,
            }



