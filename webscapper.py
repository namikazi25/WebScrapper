import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

for x in range(1, 3):
    my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1&Order=2&page='+str(x)
    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs each product
    containers = page_soup.findAll("div",{"class":"item-container"})

    filename = "products.csv"
    f = open(filename, "w")

    headers = "Brand, Product_name, Shipping, Price\n"

    f.write(headers)

    for container in containers:
        brand = container.div.div.a.img["title"]

        title_container = container.findAll("a",{"class":"item-title"})
        product_name = title_container[0].text

        shipping_container = container.findAll("li",{"class":"price-ship"})
        shipping = shipping_container[0].text

        price_container = container.findAll("li",{"class":"price-current"})
        price = price_container[0].text[:7]

        print("brand:" + brand)
        print("product_name: " + product_name)
        print("shipping: " + shipping)
        print("price: " + price)
        f.write(brand + "," + product_name.replace(",","|")+ ","+shipping + "," + price + "\n")

f.close()
