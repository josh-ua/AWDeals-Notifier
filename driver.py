from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import config
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient




def checkIfSelling(url, name):
	productPage = requests.get(url)
	soup = BeautifulSoup(productPage.content, "html.parser")
	AMWcount = 0;
	for seller in soup.find_all('h3', {'class':'a-spacing-none olpSellerName'}): ##find imgs (denotes AMW seller)
		for img in seller.findAll('img'):
			if (img.get('alt', '') == 'Amazon Warehouse Deals'):
				 AMWcount += 1
	if AMWcount > 0:
		sendMessage(url, name, AMWcount);
		return True;

def sendMessage(url, name, count):
	messageBody = str(count) + ' '+ name + ' sellers selling. Link: ' + url
	client = TwilioRestClient(config.ACCOUNT_SID, config.AUTH_TOKEN)
	
	try:
		message = client.messages.create(to=config.YOURNUMBER, from_= config.TWILIONUMBER, body=messageBody)
	except TwilioRestException as e:
		print(e)
	print('Message Sent')


if __name__ == "__main__":
	while True:
		print('Scanning for product name: ' + config.PRODUCTNAME)
		if checkIfSelling(config.PRODUCTURL, config.PRODUCTNAME) == True:
			print('Being sold - sleeping for 7 minutes.')
			print(str(datetime.now()))
			time.sleep(420)
			print()
			
		else:
			print('Sorry! Nothing found. Sleeping for 60 seconds.')
			print(str(datetime.now()))
			time.sleep(60)
			print()





