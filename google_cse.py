from googleapiclient.discovery import build
import json

def google_search(search_term, api_key, cse_id, **kwargs):

    # Builds the service using the Custom Search Engine, specifies the CSE version,
    # and provides the CSE API key. 
    service = build("customsearch", "v1", developerKey=api_key)

    # Runs the search using the built service. 
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    # Store the results in a list, with an exception for key errors.  
    try:
        return res['items']
    except KeyError:
        pass

# Create an empty list to store results in. 
results_list = []

# Takes a list of queries and runs them through the CSE API
for query in query_list: 
    results = google_search(query, api_key, cse_id, num=100)
    try: 
        for result in results:
            # Result will be a json object, append the value for key 'link'
            results_list.append(result['link'])
        except Exception as e:
            print(e)

