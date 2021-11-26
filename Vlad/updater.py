import requests
from Vlad.configurer import config


class Updater:
	def __init__(self, speaker):
		self.speaker = speaker
		self.c = config
		self.current_version = self.c.config.get("APPLICATION", "version")
		self.update_url = "https://google.com/drive/asaad313/version.json"
		self.requests = requests
		self.data = None

	def check_for_update(self):
		try:
			self.data = self.get_update_information()
		except Exception:
			print("Couldn't access Vlad's version update information.")
			return
		try:
			if str(self.current_version) != str(self.data['version']):
				print("Your virtual assistant's version is %s, while the latest one is %s" % (self.current_version, self.data['version']))
				if int(self.data['print_status']):
					print("To update visit: What can I help you with?")
				if int(self.data['speak_status']):
					self.speaker.speak(self.data['message'])
			for message in self.data['additional_information']:
				print(message)
			if self.data['speak_announcement']:
				self.speaker.speak(self.data['speak_announcement'])
		except Exception:
			print("Connectio Error with master services.")
			return


	def get_update_information(self):
		r = self.requests.get(self.update_url)
		data = r.json()
		return data
