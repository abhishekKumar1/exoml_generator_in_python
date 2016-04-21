# checks if the attributes defined to a verb is correct or not.

# say function checks the input data of say verb and return the values.
def say(verb, text, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "voice":"default",
	       "language":"default",
	       "loop":"default",
	       "flag":False
	     }
	temp["verb"] = verb
	temp["text"] = text
	for key, value in kwargs.items():
		if (key == "voice"):
			if (value == "man" or value == "woman" or value == "alice"):
				temp["voice"] = value
			else:
				temp["text"] = "Wrong voice value in Say. It can only be " \
				               "\"man\", \"woman\" or \"alice\" " \
				               "enterd value is: " + value 
				temp["flag"] = True
				break
		elif (key == "language"):
			if (value == "en"):
				temp["language"] = value
			else:
				temp["text"] = "Wrong language value in Say. We only " \
				               "support \"en\" as in english for now. " \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		elif (key == "loop"):
			if type(value) is int:
				temp["loop"] = str(value)
			else:
				temp["text"] = "Wrong loop value in Say. It must be an " \
				               "integer."
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Say only " \
			               "support: voice, language and loop. " \
			               "The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output

# play function checks the input data of play verb and return the values.
def play(verb, url, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "loop":"default",
	       "flag":False
	     }
	temp["verb"] = verb
	temp["text"] = url
	for key, value in kwargs.items():
		if (key == "loop"):
			if type(value) is int:
				temp["loop"] = str(value)
			else:
				temp["text"] = "Wrong loop value in Play. It must be " \
				               "an integer."
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Play only " \
			               "support: loop. The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output

# dial function checks the input data of dial verb and return the values.
def dial(verb, number, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "action":"default",
	       "method":"default",
	       "timeout":"default",
	       "record":"default",
	       "flag":False
	 }
	temp["verb"] = verb
	for key, value in kwargs.items():
		if (key == "action"):
			if type(value) is str:
				temp["action"] = value
			else:
				temp["text"] = "Wrong action value in Dial. It must be " \
				               "a string."
				temp["flag"] = True
				break
		elif (key == "method"):
			if (value == "GET" or value == "POST"):
				temp["method"] = value
			else:
				temp["text"] = "Wrong method in Dial. It can only be " \
				               "\"GET\" or \"POST\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		elif (key == "timeout"):
			if type(value) is int:
				temp["timeout"] = str(value)
			else:
				temp["text"] = "Wrong timeout value in Dial. It must be " \
				               "an integer."
				temp["flag"] = True
				break
		elif (key == "record"):
			if (value == "record-from-answer" or  
			   		value == "record-from-ringing" or 
			    	value == "do-not-record"):
				temp["record"] = value
			else:
				temp["text"] = "Wrong record value in Dial. It can only be " \
				               "\"record-from-answer\", \"record-from-" \
				               "ringing\" or \"do-not-record\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Dial only " \
			               "support: action, method, timeout and record." \
			               "The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)	
	return output

# gather function checks the input data of gather verb and return the values.
def gather(verb, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "action":"default",
	       "method":"default",
	       "numDigits":"default",
	       "timeout":"default",
	       "finishOnKey":"default",
	       "flag":False
	     }
	temp["verb"] = verb	
	for key, value in kwargs.items():
		if (key == "action"):
			if type(value) is str:
				temp["action"] = value
			else:
				temp["text"] = "Wrong action value in Gather. It must be " \
				               "a string."
				temp["flag"] = True
				break
		elif (key == "method"):
			if (value == "GET" or value == "POST"):
				temp["method"] = value
			else:
				temp["text"] = "Wrong method in Gather. It can only be " \
				               "\"GET\" or \"POST\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		elif (key == "numDigits"):
			if type(value) is int:
				temp["numDigits"] = str(value)
			else:
				temp["text"] = "Wrong numDigits value in Gather. It must be " \
				               "an integer."
				temp["flag"] = True
				break
		elif (key == "timeout"):
			if type(value) is int:
				temp["timeout"] = str(value)
			else:
				temp["text"] = "Wrong timeout value in Gather. It must be " \
				               "an integer."
				temp["flag"] = True
				break
		elif (key == "finishOnKey"):
			if (value == "*" or value == "#" or
					(value.isdigit() and int(value)<10)):
				temp["finishOnKey"] = str(value)
			else:
				temp["text"] = "Wrong finishOnKey value in Gather. It can " \
				               "only be 0123456789*#" \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Gather only " \
			               "support: action, method, numDigits, timeout " \
			               "and finishOnKey. The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output

# record function checks the input data of record verb and return the values.
def record(verb, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "action":"default",
	       "method":"default",
	       "timeout":"default",
	       "finishOnKey":"default",
	       "maxLength": "default", 
	       "flag":False
	     }
	temp["verb"] = verb	
	for key, value in kwargs.items():
		if (key == "action"):
			if type(value) is str:
				temp["action"] = value
			else:
				temp["text"] = "Wrong action value in Record. It must be " \
				               "a string."
				temp["flag"] = True
				break
		elif (key == "method"):
			if (value == "GET" or value == "POST"):
				temp["method"] = value
			else:
				temp["text"] = "Wrong method in Record. It can only be " \
				               "\"GET\" or \"POST\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break		
		elif (key == "timeout"):
			if type(value) is int:
				temp["timeout"] = str(value)
			else:
				temp["text"] = "Wrong timeout value in Record. It must be " \
				               "an integer."
				temp["flag"] = True
				break
		elif (key == "finishOnKey"):
			if (value == "*" or value == "#" or 
					(value.isdigit() and int(value)<10)):
				temp["finishOnKey"] = str(value)
			else:
				temp["text"] = "Wrong finishOnKey value in Record. It can " \
				               "only be 0123456789*#" \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		elif (key == "maxLength"):
			if type(value) is int:
				temp["maxLength"] = str(value)
			else:
				temp["text"] = "Wrong maxLength value in Record. It must " \
				               "be an integer."
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Record only " \
			               "support: action, method, timeout, finishOnKey " \
			               "and maxLength. The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output

# hangup function checks the input data of hangup verb and return the values.
def hangup(verb, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "flag":False
	     }
	temp["verb"] = verb
	for key, value in kwargs.items():
		if key :
			temp["text"] = "Hangup doesn't have any attribute." \
			               "The unknwon variable is: " + key
			temp["flag"] = True
	output.append(temp)
	return output

# reject function checks the input data of reject verb and return the values.
def reject(verb, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "reason":"default",
	       "flag":False
	     }
	temp["verb"] = verb
	for key, value in kwargs.items():
		if (key == "reason"):
			if value is "busy" or value is "rejected":
				temp["reason"] = value
			else:
				temp["text"] = "Wrong reason value in Reject. It can " \
				               "either be \"busy\" or \"rejected\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Reject only " \
			               "support: reason. The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output

# redirect function checks the input data of redirect verb and return the 
# values.
def redirect(verb, url, output, **kwargs):
	temp={
	       "verb":"default",
	       "text":"default",
	       "method":"default",
	       "flag":False
	     }
	temp["verb"] = verb
	temp["text"] = url
	for key, value in kwargs.items():
		if (key == "method"):
			if value is "GET" or value is "POST":
				temp["method"] = value
			else:
				temp["text"] = "Wrong method value in Redirect. It can " \
				               "either be \"GET\" or \"POST\"." \
				               "enterd value is: " + value
				temp["flag"] = True
				break
		else:
			temp["text"] = "Some unknwon variable enterd. Redirect only " \
			               "support: method. The unknwon variable is: " + key
			temp["flag"] = True
			break
	output.append(temp)
	return output