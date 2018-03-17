from bs4 import BeautifulSoup

from pprint import pprint
import re

def restructure_content(filename):
	#schema
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
	output_json = {'sections': []}

	try:
		file = open(filename, encoding="utf8")
		# print(file)
		parsed_html = BeautifulSoup(file.read(), "html.parser")
		html_content=parsed_html.body.find('div', attrs={'class':'body searchable-content'}) 
		next=html_content.find_next()
		#print("################### Print Next ######################")
		#print(next)
		#print("#########################################")
		while True:
			print("while")
			if not next:
				break
			#check if next is header
			if re.match("^h", next.name):
				print("next is header")
				section = build_section(next)
				print("################# Print Section ########################")
				print(section)
				print("#########################################")
			else:
				next = next.find_next()
				print("################# Print next ########################")
				print(next)
				print("#########################################")
	finally:
		file.close()

def build_section(header):
	#section_obj to build output_json
	print("build section function")
	section_obj= {}
	next=header.find_next()
	print("#########next in build_section############3")
	print(next)
	print("#########################################")
	while True:
		if not next:
			break
		#Check if next is header or not
		if re.match("^h", next.name):
			#check if next is section or sub section
			if next.name.lower() > header.name.lower():
				#this header has subsection
				print("next is subsection")
				#build subsections array in section_obj if it is not exist
				if not 'subsections' in section_obj:
                    section_obj['subsections'] = []
				section = build_section(next)
				section['subsection'] = next.get_text()
				section_obj['subsections'].append(section)
				print(section_obj)
			else:
				break
		else:
			print("next is not header")
			#
			next = next.find_next()
	return section_obj






	print(header.find_next())


restructure_content('../inputs/5bd6c00d652cfa3480dff05398d0e4b6')


