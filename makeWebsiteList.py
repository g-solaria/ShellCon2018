import sys, os

def makeWebsiteList():
	"""Makes a list of the websites"""
	if len(sys.argv) > 1: 
		websiteFile = sys.argv[1]
	else: 
		websiteFile = input("Please provide a list of websites: ")
	try:
		with open(websiteFile) as f_obj:
			websiteList = f_obj.readlines()
	except FileNotFoundError:
		while True:
			print("The file " + websiteFile + " does not exist.")
			websiteFile = input("Please enter a valid file: ")
			if os.path.isfile(websiteFile):
				break
		with open(websiteFile) as f_obj:
			websiteList = f_obj.readlines()
	return websiteList
