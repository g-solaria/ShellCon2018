from selenium import webdriver

profileId = input("Please enter a Facebook UserID: ")

with open('fbpagelist.txt') as pl:
	urlEnds = pl.readlines()

urls = []

for ue in urlEnds:
	url = "https://facebook.com" + profileId + ue
	urls.append(url)
	
def browser(url):

	options = webdriver.ChromeOptions()

	options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'

	options.add_argument('headless')
	
	driver = webdriver.Chrome(chrome_options=options)

	driver.get('https://facebook.com')

	driver.implicitly_wait(10)

	email = driver.find_element_by_css_selector('input[type=email]')
	password = driver.find_element_by_css_selector('input[type=password]')
	login = driver.find_element_by_css_selector('input[value="Log In"]')
	
	email.send_keys('hallieamberhall@gmail.com')
	password.send_keys('5`X7b2q&Ef=U~Z`V')
	
	driver.get_screenshot_as_file(ue + 'page.png')

for url in urls:
	browser(url)