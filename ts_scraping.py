import requests
from bs4 import BeautifulSoup
import csv

url = 'https://lenouvelliste.com/'

reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find_all('h1')  
    lyen = soup.find_all('a')
    artik = soup.find_all('div', class_='lnv-featured-article-lg')

    lien_image = []

    for div in artik:
        imgt = div.find('img')
        if imgt:
            srcvaleur = imgt.get('src')
            lien_image.append(srcvaleur)

    with open('Nouv_donne.csv', mode='w', newline='') as e:
        ekri = csv.writer(e)

        ekri.writerow(['Titres'])  
        for titre in title:
            ekri.writerow([titre.text.strip()])  
            
        ekri.writerow(['Liens'])
        for lien in lyen : 
            ekri.writerow([lien.text.strip()])
    
        ekri.writerow(['Lien Images']) 
        for link in lien_image:
            ekri.writerow([link])
            
print(lien_image)