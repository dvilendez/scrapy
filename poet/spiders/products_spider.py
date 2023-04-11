import scrapy
from scrapy_poet import callback_for
from poet.page_objects.abcdin.products_po import ProductPage

class ProductsSpider(scrapy.Spider):
  name = "products"
  start_urls = ["https://www.abcdin.cl/computacion/notebooks/notebooks-lenovo"]
  parse_product = callback_for(ProductPage)

  def parse(self, response):
    links = response.css("div.image-reviews-box a")
    yield from response.follow_all(links, self.parse_product)


