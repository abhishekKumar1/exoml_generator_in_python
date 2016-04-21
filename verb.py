import verb_check as check

# Different verbs from which you can pick which verbs you want to use.

# Say verb must have a text content and other parameters are optional.
class Say():
	def __init__(self, text, **kwargs):
		self.out = []
		self.out = check.say("Say", text, self.out, **kwargs)

# Play verb must have an url and other parameters are optional.
class Play():
	def __init__(self, url, **kwargs):
		self.out=[]
		self.out = check.play("Play", url, self.out, **kwargs)

# Dial verb must have a number and other parameters are optional.
# number is defined as a subtree of Dial
class Dial():
	def __init__(self, number, **kwargs):
		self.out=[]
		self.out= check.dial("Dial", number, self.out, **kwargs)
		if(self.out[0]["flag"] == False):
			temp1 = { 
					"verb":"Number",
					"text":number,
					"nested":True,
					"flag": False
			}
			self.out.append(temp1)

# Gather verb has all parameters as optional. It can only have say 
# and play verbs as its nestable verbs.
class Gather():
	def __init__(self, **kwargs):		
		self.out = []
		self.out = check.gather("Gather", self.out, **kwargs)

	def say(self, text, **kwargs):
		gathersay=Say(text, **kwargs)
		temp ={"nested":True}
		gathersay.out[0].update(temp)
		self.out.append(gathersay.out[0])

	def play(self, url, **kwargs):
		gatherplay=Play(url, **kwargs)
		temp ={"nested":True}
		gatherplay.out[0].update(temp)
		self.out.append(gatherplay.out[0])

# Record verb has all parameters as optional.
class Record():
	def __init__(self, **kwargs):
		self.out = []
		self.out = check.record("Record", self.out, **kwargs)

# Hangup verb has all parameters as optional.
class Hangup():
	def __init__(self, **kwargs):
		self.out = []
		self.out = check.hangup("Hangup", self.out, **kwargs)

# Reject verb has all parameters as optional.		
class Reject():
	def __init__(self, **kwargs):
		self.out = []
		self.out = check.reject("Reject", self.out, **kwargs)

# Redirect verb must have an url to redirect and other parameters are optional
class Redirect():
	def __init__(self, url, **kwargs):
		self.out = []
		self.out = check.redirect("Redirect", url, self.out, **kwargs)