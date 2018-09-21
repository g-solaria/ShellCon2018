from google.cloud import language
import requests

with open('output.txt', 'r') as f_obj: 
	resultsList = f_obj.readlines()

#for r in resultsList:
#	print(r)

def get_ents(page):
	
	client = language.LanguageServiceClient()
	
	document = language.types.Document(content=page, type="HTML")
	
	result = client.analyze_entities(document=document)
	
for r in resultsList:
	page = requests.get(r)
	
	html = page.text
	
	print(html)
	 
#	entity = get_ents(html)
	
#	print(entity)
	
	