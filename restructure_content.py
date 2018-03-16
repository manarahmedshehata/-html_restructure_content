from bs4 import BeautifulSoup

from pprint import pprint
import re

def restructure_content(filename):
	"""
	json={"sections":[
			{
			"section":"",
			"paragraphs":[],
			{"subsections":
				[{
				"subsection":""
				"paragraphs":[]
				}]
				}
			}	
		]
		}
	"""
	try:
		file = open(filename, encoding="utf8")
		# print(file)
		parsed_html = BeautifulSoup(file.read(), "html.parser")
		print("#########################################")
		html_content=parsed_html.body.find('div', attrs={'class':'body searchable-content'}) 
		if html_content.find_next(re.compile("^h")) != None:
			print(html_content.find_next(re.compile("^h")))
			build_section(html_content.find_next(re.compile("^h")))
	finally:
		file.close()

def build_section(header):
	next=header
	while True:
		next=header.find_next()
		if not next:
			break
		if re.match("^h", next.name):
			#section
			if next.name > header.name:
				#subsection
				build_section(next);






	print(header.find_next())


restructure_content('../inputs/5bd6c00d652cfa3480dff05398d0e4b6')


