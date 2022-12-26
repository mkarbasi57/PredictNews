import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv
import regexx
rows = []



def scraping(year,page,title):
    webpage = requests.get(f'https://www.irna.ir/page/archive.xhtml?mn=6&wide=0&dy=3&ms=0&pi={page}&yr={year}&tp=14')
    webpage = webpage.text
    soup = BeautifulSoup(webpage, 'lxml')
    titr = soup.find_all('li', class_="news")
    for t in titr:
        text = str(t.p.text).replace('\n','').replace('   ',' ').replace('  ',' ')
        text = regexx.regex(text)
        row = [text, title]
        rows.append(row)

def main():

    fields = ['Text', 'Title']
    filename = "sport.csv"

    LastPageNumber = 100
    print("Total page to scrape: {}".format(LastPageNumber))
    #scraping(2,fields)
    for year in range(1400,1402):
        for page_number in tqdm(range(1,LastPageNumber)):
            scraping(year,page_number,'sport')

    with open(filename, 'w',encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


main()