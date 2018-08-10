import random
import time

import speech_recognition as sr


def get_the_voice_from_mic(recognizer, microphone):
	print "inside"
	if not isinstance(recognizer, sr.Recognizer):
		raise TypeError("`recognizer` must be `Recognizer` instance")

	if not isinstance(microphone, sr.Microphone):
		raise TypeError("`microphone` must be `Microphone` instance")
		
	with microphone as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
		text_data = recognizer.recognize_google(audio)
	except sr.RequestError:
		print "It's seems API is not working"
		return
	except sr.UnknownValueError:
		print "Failed to recognige the voice"
		return

	return text_data