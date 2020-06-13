import requests
from bs4 import BeautifulSoup as soup 

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

while True:
	nums = "0123456789"
	answer = input("\nEnter an amount of money in any currency to convert it to USD (It should be in the format AMOUNT CURRENCY, where the currency is abbreviated: ")
	try:
		number = answer.split()[0]
		currency = answer.split()[1]
	except:
		print("\nYour answer needs to have both a value and a currency.")
		continue

	count = 0
	for char in number:
		if char in nums or char==".":
			count +=1
		else:
			print("\nYour input needs to follow the following format: AMOUNT CURRENCY")
			count = 0
			break

	response = requests.get("https://www.fx-exchange.com/usd/rss.xml", headers=headers)

	if response.status_code == 200:
		page_soup = soup(response.text,"html.parser")
		countries = page_soup.findAll("item")

		parts = []
		for country in countries:
			wanted = str(country.title.text).split("/")[1]
			parts.append(wanted)

		counter_wanted = []
		for wanted in parts:
			for word in wanted.split("("):
				if wanted.split("(").index(word)==1:
					counter_wanted.append(word.strip(word[-1]))

		if currency in counter_wanted or currency.upper() in counter_wanted:
			if count==len(number):
				break

	else:
		print("failure")

currency = currency.upper()

def parser(x):
	return float(x.split("=")[1].split()[0])

if response.status_code == 200:
	page_soup = soup(response.text, "html.parser")
	currencies = page_soup.findAll("item")

	for thing in currencies:
		if currency in str(thing.title.text):
			conversion_rate = parser(str(thing.description.text))
			break

worth = round(float(number)/conversion_rate, 2)

print("\n" + str(number) + " " + str(currency) + " = " + str(worth) + " USD")
print("\nConversation Rate: 1 USD = " + str(round(conversion_rate, 2)) + " " + str(currency))