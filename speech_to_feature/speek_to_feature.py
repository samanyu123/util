import os
import speech_recognition as sr
from convert_voice import recognize_speech_from_mic

class SpeakToFeature(object):
	"""Create the behave feature file based on the 
	   user input. The user needs to speek for the
	   question ask"""
	def __init__(self):
		self.recognizer = sr.Recognizer()
		self.microphone = sr.Microphone()
	
	def get_text(self):
		return recognize_speech_from_mic(self.recognizer,self.microphone)["transcription"]
		
	def create_feature_file(self):
		print "What is your feature file name"
		file_name = self.get_text().replace(" ","_")
		if file_name:
			self.create_file(file_name)
			
	def create_file(self, file_name):
		file_name+=".feature"
		self.feature_fh = open(file_name, "w")
	
	def close_fh(self):
		self.feature_fh.close()
		
	def fetaure_description(self):
		print "What is your feature objective"
		feature_desc = self.get_text()
		print feature_desc
		if feature_desc:
			self.write_feature_descp(feature_desc)
			
	def write_feature_descp(self, desc):
		feature_desc = "Feature:" + desc.capitalize() + "\n"
		self.feature_fh.write(feature_desc)
		
	def sceanrio_description(self):
		print "What is your scenario objective.Say done if completed"
		scenario_desc = self.get_text()
		print scenario_desc
		if scenario_desc == "done":
			return True
		elif scenario_desc:
			self.write_scenario_descp(scenario_desc)
		else:
			print "Failed to get the sceanrio description"
			
	def write_scenario_descp(self, desc):
		scenario_desc = "Scenario:" + desc.capitalize() + "\n"
		self.feature_fh.write(scenario_desc)
		
	def sceanrio_step(self):
		print "What is your step. Say done if comleted"
		step_desc = self.get_text()
		print step_desc
		if step_desc == "done":
			return True
		elif step_desc:
			self.write_step_descp(step_desc)
		else:
			print "Failed to get the sceanrio step"
		
	
	def write_step_descp(self, decs):
		desc = decs + "\n"
		self.feature_fh.write(desc)
		
	def create_scenario(self):
		while True:
			if self.sceanrio_description():
				break
			while True:
				if self.sceanrio_step():
					break
if __name__ == "__main__":
	import pdb
	#pdb.set_trace()
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()
	guess = SpeakToFeature()
	guess.create_feature_file()
	guess.fetaure_description()
	guess.create_scenario()
	guess.close_fh()