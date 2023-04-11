from web_poet.pages import WebPage

class ProductPage(WebPage):
  """Producto individual de la pagina de abcdin
  por ejemplo https://www.abcdin.cl/notebook-lenovo-ideapad-3-intel-core-i7-1165g7-8gb-ram-512gb-ssd-14-1-1178163
  """
  def to_item(self):
    """Convierte la pagina en un producto"""
    return {
      "url": self.url,
      "name": self.css("h1.page-title span::text").get(),
      "sku": self.css("div.product.attribute.sku div.value::text").get(),
    }