import bs4, re, requests, time, timeout_decorator

with open('keywordfile.txt') as keywords:
	keywordList = keywords.readlines()

@timeout_decorator.timeout(15, timeout_exception=StopIteration)
def priorityFirst(htmlSoup):
    """Counts instances of the first keyword"""
    search_word = keywordList[0].rstrip()    
    keys = htmlSoup.body.find_all(strings=re.compile('.*{0}*'.format(search_word)), recursive=True)
    return keys

@timeout_decorator.timeout(15, timeout_exception=StopIteration)
def prioritySecond(htmlSoup):
    """Counts instances of the second keyword"""
    search_word = keywordList[1].rstrip()
    keys = htmlSoup.body.find_all(strings=re.compile('.*{0}*'.format(search_word)), recursive =True)
    return keys

@timeout_decorator.timeout(15, timeout_exception=StopIteration)	
def priorityRest(htmlSoup):
    """Counts instances of the rest of the keywords"""
    secondKeylist = keywordList[2:-1]
    for keyword in secondKeylist:
        search_word = keyword
        keys = htmlSoup.body.find_all(string=re.compile('.*{0}*'.format(search_word)), recursive=True)
        return keys
		
with open('output.txt') as output: 
	resultList = output.readlines()
	
highPriority = []
mediumPriority = []
lowPriority = []
	
for result in resultList: 
	print("Checking Result " + result)
	try:
		page = requests.get(result)
		htmlPage = bs4.BeautifulSoup(page.text, "lxml")
	
		priority = len(priorityFirst(htmlPage))
		priority = priority + len(prioritySecond(htmlPage))/2
		priority = priority + len(priorityRest(htmlPage))/4
	
		if priority > 4: 
			highPriority.append(result)
		elif 2 < priority < 4:
			mediumPriority.append(result)
		elif priority < 2: 
			lowPriority.append(result)	
	except AttributeError:
		pass		
	except StopIteration:
		print("Timed Out")
	except Exception as exp: 
		print("There was a problem %s" % (exp))

print("High Priority")		
for i in highPriority:
	print(i)
print("Medium Priority")
for i in mediumPriority:
	print(i)
print("Low Priority")	
for i in lowPriority:
	print(i)