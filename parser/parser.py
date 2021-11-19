from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
everyfilelist = []

r = requests.get('https://www.tltsu.ru/sveden/education/educational-programs/2021-set/') 

html_doc=r.text

soup = BeautifulSoup(html_doc, 'html.parser')

head = soup.find('tbody')

headitems = head.find_all('tr')

'''собираем информацию о файлах'''
for item in headitems:
	listofitem = item.find_all('td')
	try:
		everyfilelist.append({
		'pdf_name': re.sub("\n|(\t ?)|\xa0 ?","",listofitem[1].get_text()),
		'link_to_pdf': listofitem[5].find('a').get('href')
		}
		)
	except:
		pass
		
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(str(filename) + ".pdf", 'wb')
    file.write(response.read())
    file.close()

 

for file in everyfilelist:
	try:
		download_file(file['link_to_pdf'],file['pdf_name'])
	except:
		pass

