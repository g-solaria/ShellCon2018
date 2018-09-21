import sys, os

def makeKeywordList():
	"""Makes a list of keywords to work with"""
	if len(sys.argv) > 1:
		keywordFile = sys.argv[2]
	else:
		keywordFile = input("Please provide a keyword file: ")
	try:	
		with open(keywordFile) as f_obj:
			keywordList = f_obj.readlines()
	except FileNotFoundError:
		while True:
			print("The file " + keywordFile + " does not exist.")
			keywordFile = input("Please enter a valid filename: ")
			if os.path.isfile(keywordFile):
				break
		with open(keywordFile) as f_obj:
			keywordList = f_obj.readlines()
	return keywordList
