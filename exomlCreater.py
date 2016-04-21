from xml.etree.ElementTree import Element, SubElement, tostring, XML

# This file creates the xml.

# create function creates the xml tree with verb as a subtree of resp and
# flag is used to find out if input has an error.
def create(resp, verb, text, flag, **kwargs):
	if flag == True:
		temp = SubElement(resp, verb)
	else:
		temp = SubElement(resp, verb, **kwargs)
	if text != "default" :
		temp.text =	text
	return temp

# response function reads out the data from a list of dictionaries and 
# pass it to create to make an xml tree. 
def response(output):
	resp = Element("Response")
	for i in output:
		verb = i.pop("verb")
		text = i.pop("text")
		flag = i.pop("flag")
		for key,value in i.items():
			if value == "default":
				del i[key]
		if "nested" in i :
			del i["nested"]
			temp1 = create(temp, verb, text, flag)
		else:		
			temp = create(resp, verb, text, flag, **i)					 
	return resp