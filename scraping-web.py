from bs4 import BeautifulSoup
import requests

#web scraping para obtener información de sitios web
def run():
    URL = 'https://yonatanmc.com/research/resumen-de-metodologia-de-investigacion-cuantitativa'

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.prettify())


if __name__ == '__main__':
    run()