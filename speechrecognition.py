# Python program to translate 
# speech to text and text to speech 


import speech_recognition as sr 
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to 
# speech  
	
	
# Loop infinitely for user to 
# speak 

def s2t():	 
	# Exception handling to handle 
	# exceptions at the runtime 
	try: 
		
		# use the microphone as source for input. 
		with sr.Microphone() as source2: 
			
			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=2) 
			
			#listens for the user's input 
			print("speak now")
			audio2 = r.listen(source2) 
			
			# Using ggogle to recognize audio 
			MyText = r.recognize_google(audio2) 
			MyText = MyText.lower() 

			print("Did you say "+MyText) 
			print(MyText) 
			
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		
	except sr.UnknownValueError: 
		print("unknown error occured") 
s2t()		
