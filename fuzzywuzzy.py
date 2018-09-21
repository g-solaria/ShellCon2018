import fuzzywuzzy
import bs4
from google.cloud import language
import requests

with open('keywordfile.txt') as f_obj: 
	keywords = f_obj.readlines()
	
with open('output.txt') as f_obj:
	results = f_obj.readlines()
	
def get_ents(page):
	
	ents = []
	
	client = language.LanguageServiceClient()
	
	document = language.types.Document(content=page, type="HTML")
	
	response = client.analyze_entities(document=document, encoding_type="UTF32")
	
	for ent in response.entities:
		ents.append(ent.name)
	
	return ents
	
def match(ents):
	
	matched = []
	
	for un in unmatched: 
		if fuzzywuzzy.fuzz(keywords[0], un) > 90:
			matched.append(un)
			print(un)
	
	return matched

for r in results: 
	
	page = requests.get(r)
	
	bsObj = bs4.BeautifulSoup(page.text, "lxml").get_text()
	
	unmatched = get_ents(bsObj)
	
	matched = match(unmatched)
	
	
	