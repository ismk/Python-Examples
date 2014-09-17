def shut_down(s):
	s = s.lower()
	if(s == "yes"):
		return "Shutting down..."
	elif(s == "no"):
		return "Shutdown Aborted!"
	else:
		return "Sorry, I dont Understand you."

print (shut_down("huh"))
    
    
    
    
    