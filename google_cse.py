from googleapiclient.discovery import build
from makeKeywordList import makeKeywordList
from makeWebsiteList import makeWebsiteList
import json

websiteList = makeWebsiteList()
keywordList = makeKeywordList()

# Google CSE api key and search engine ID. 
keyFile = '.monitor.api'
engineFile = '.search.id'

# read API key and CSE ID into memory
with open(keyFile) as f_obj:
    my_api_key = f_obj.read().rstrip()

with open(engineFile) as f_obj:
    my_cse_id = f_obj.read().rstrip()

queryList = []
for website in websiteList:
    query = "site:" + website.rstrip() + ' ' + '"' + keywordList[0].rstrip() + '"'
    queryList.append(query)

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	try:
		return res['items']
	except KeyError:
		pass

resultsList = []

for query in queryList:
    results = google_search(query, my_api_key, my_cse_id, num=10)
    try:
        for result in results:
            resultsList.append(result['link'])
    except TypeError:
        pass

with open('output.txt', 'w') as file:
	for r in resultsList:
		file.write('%s\n' % r)
