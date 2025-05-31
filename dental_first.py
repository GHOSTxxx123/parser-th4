from bs4 import BeautifulSoup
import requests
import time

BASE_URL = "https://dental-first.ru"
    
def get_descriptions():
    start = time.time()
    url = f"{BASE_URL}/catalog/stomatologicheskie-materialy/adgezivy-i-bondingi/3m-espe/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find("div", {"class": "set-row"})


    products = []
    for item in items.find_all("div", {"class": "set-card"}):
        title = item.select_one("a")["title"]
        href = item.select_one("a")["href"]
        link = BASE_URL + href
        
        product_page = requests.get(link)
        soup_inner = BeautifulSoup(product_page.text, "html.parser") 
        desc = soup_inner.find("div", {"id": "descr-text"})
        brand = soup_inner.find("span", {"itemprop": "brand"}).select_one('a').text
        # count = soup_inner.find("span", {})
        code_product = soup_inner.find("span", {"class": "pass_kodtovara"}).text.split(":")
        article = soup_inner.find("span", {"class": "pass_aticul"}).text.split(":")
        id_product = soup_inner.find("span", {"class": "pass_id"}).text.split(":")
        
        products.append({"title":title, "url": link, "description": desc,  "brand": brand, code_product[0]: code_product[1], article[0]: article[1], id_product[0]:id_product[1]})
        # print(products)

    # print(f"Парсинг названия товаров. Завершено за {time.time() - start:.2f}сек")
    
    return products

# get_descriptions()


