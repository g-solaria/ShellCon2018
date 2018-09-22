from fuzzywuzzy import fuzz
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
	
	matchedEnts = []
	
	for ent in ents: 
		score = fuzz.partial_ratio(ent, keywords[0])
		if score > 90:
			matchedEnts.append(ent)
	
	return matchedEnts	

for r in results: 
	
	try:
		print("Matching...")
		page = requests.get(r)
	
		bsObj = bs4.BeautifulSoup(page.text, "lxml").get_text()
	
		ents = get_ents(bsObj)
	
		matchedEnts = match(ents)
	
	except Exception as e:
		print(e)
	
for ent in matchedEnts:
	print(ent)