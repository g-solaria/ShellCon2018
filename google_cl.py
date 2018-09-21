from google.cloud import language
import requests
import bs4
import time
import timeout_decorator

with open('output.txt', 'r') as f_obj: 
	resultsList = f_obj.readlines()

#for r in resultsList:
#	print(r)


def get_sentiment(page):
	
	client = language.LanguageServiceClient()
	
	document = language.types.Document(content=page, type="PLAIN_TEXT")
	
	response = client.analyze_sentiment(document=document, encoding_type="UTF32")
	
	sentiment = response.document_sentiment
	
	print(sentiment.score)
	print(sentiment.magnitude)
	
for r in resultsList:
	page = requests.get(r)

	try:
		html = page.text
	
		soup = bs4.BeautifulSoup(html, "lxml")
	
		body = soup.body.get_text()
		
		print(r)
		
		sentiment = get_sentiment(body)
	
		
	except AttributeError:
		pass
	except Exception as e:
		print("There was an exception: %s" % (e))	
	
	