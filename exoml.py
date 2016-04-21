from xml.etree.ElementTree import Element, SubElement, tostring, XML
import exomlCreater

# This file have the data for the response.

# Response class as all xml request should open with it. Also used for 
# adding and printing all verbs. 
class Response():
	def __init__(self):
		self.output = []

	def __str__(self):
		self.tempPrint = exomlCreater.response(self.output)
		return tostring(self.tempPrint)

	def add(self, *args):
		for i in args:
			for j in i.out:
				self.output.append(j)