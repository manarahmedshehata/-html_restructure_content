from bs4 import BeautifulSoup

def restructure_content(filename):
	file = open(filename, encoding="utf8").read()
	# print(file)
	out={"sections":[]}
	sections=[]
	#reead html file
	parsed_html = BeautifulSoup(file, "html.parser")
	print("#########################################")
	#Get searchable-content 
	html_content=parsed_html.body.find('div', attrs={'class':'body searchable-content'})
	#print(html_content.find_all('h2'))
	for i in range(1,7):
		if html_content.find_next('h'+ str(i)) != None:
			print(i)
			print(html_content.find_next('h'+ str(i)).text)
			sections.append({"section":html_content.find_next('h'+ str(i)).text})
			
	print("#########################################")	
restructure_content('inputs/5bd6c00d652cfa3480dff05398d0e4b6')
