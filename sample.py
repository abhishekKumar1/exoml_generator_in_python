#Sample file for exoml creation
#import theses two files:
import exoml
import verb

def example():
	request = exoml.Response()  #response will have all the verbs nested inside it.

	#verbs you want to add in the xml file
	say1 = verb.Say("Hello", voice="man", language="en")  
	play1 = verb.Play("https://s3-ap-southeast-1.amazonaws.com/exotelaudiouploads/0024edb890d9f44603089a6fc663c8ab.wav", loop=2)
	dial1 = verb.Dial("+918293457066")
	record1 = verb.Record(action="abc.com", method="GET", timeout=10, finishOnKey="5", maxLength=5)
	#gather verb is special because it can nest play and say inside it
	gather1 = verb.Gather()
	gather1.say("Hi press 1 to do this and press 2 to do that.")
	#now to add the verbs in rsponse
	request.add(say1, play1, dial1, record1, gather1)
	#you can add in any order
	#you can also add it multiple times
	reject1 = verb.Reject(reason="busy")
	redirect1 = verb.Redirect("https://def.com", method= "GET")
	request.add(reject1, redirect1)
	#you can also add verbs directly like:
	request.add(verb.Say(" What are you doing?"))
	print str(request)

if __name__ == "__main__":
    example()