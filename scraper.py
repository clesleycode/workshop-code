import scrapy

class BrickSetSpider(scrapy.Spider):

    name = "brickset_spider" # subclass
    start_urls = ['http://brickset.com/sets/year-2016'] # site we're scraping

    def parse(self, response):
        SET_SELECTOR = '.set' # css selector we'll extract off of
        for brickset in response.css(SET_SELECTOR): # iterates through the tags in the css

            # selectors for information we're extracting
            NAME_SELECTOR = 'h1 a ::text' 
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)' 
            yield {
              # extract_first() grabs first element of text
                'name': brickset.css(NAME_SELECTOR).extract_first(),  
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)' # selector for link to next page
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        
        if next_page: # if page is successfully grabbed
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )
