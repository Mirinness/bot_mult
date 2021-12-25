import requests
from bs4 import BeautifulSoup
import sqlite3


class Cinema:

    def __init__(self, cinema_name, dict_with_cinema):
        self.cinema_name = cinema_name
        self.dict_with_cinema = dict_with_cinema

    def connect_to_site(self, link):
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'lxml')
            return soup
        except:
            return None

    def save_to_db(self, list_):
        # print(list_)
        conn = sqlite3.connect("multiplex.db")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO films2 VALUES (?,?,?,?,?,?,?,?)", list_)
        conn.commit()
        conn.close()


class Multiplex(Cinema):

    def __init__(self, cinema_name, dict_with_cinema):
        Cinema.__init__(self, cinema_name, dict_with_cinema)

    def get_films(self, cinema, link):
        soup = self.connect_to_site(link)
        name_build = soup.select_one('li.breadcrumbs__item_last').text
        address = soup.select_one('p.val').text
        if soup != None:
            arr = []
            for i in soup.find_all('div', class_="ns"):
                if i.get('data-name') != None:
                    arr.append(
                        [
                            i.get('data-name'),
                            i.get('data-anchor'),
                            i.find('p', class_='time').text,
                            i.find('p', class_='tag').text,
                            name_build,
                            address,
                            i.get('data-id'),
                            link
                        ]

                    )
            self.save_to_db(arr)

    def parse(self):

        for cinema, link in self.dict_with_cinema.items():
            self.get_films(cinema, link)


kin_th = Multiplex(
    'Multiplex',
    {
        'Цум' : 'https://multiplex.ua/cinema/kyiv/tsum',
        'Лавіна' : 'https://multiplex.ua/cinema/kyiv/lavina',
        'Республіка' : 'https://multiplex.ua/cinema/kyiv/respublika',
        'Проспект' : 'https://multiplex.ua/cinema/kyiv/prospect',
        'Комод' : 'https://multiplex.ua/cinema/kyiv/komod',
        'Атмосфера' : 'https://multiplex.ua/cinema/kyiv/atmosphera',
        'Краван': 'https://multiplex.ua/cinema/kyiv/karavan',
        'Ретровіль': 'https://multiplex.ua/cinema/kyiv/retroville'
    }
)

kin_th.parse()