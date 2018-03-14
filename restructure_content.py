from bs4 import BeautifulSoup

def test(filename):
	file = open(filename, encoding="utf8").read()
	# print(file)
	parsed_html = BeautifulSoup(file, "html.parser")
	print("#########################################")
	html_content=parsed_html.body.find('div', attrs={'class':'body searchable-content'})
	#print(html_content.find_all('h2'))
	
	print("#########################################")	
test('C:/Users/HassanM/Desktop/manar/ma/inputs/5bd6c00d652cfa3480dff05398d0e4b6')
