import requests

class Back:
	def __init__(self):
		self.location="Lyon "
		with open("key.txt", "r") as txt_file:
			self.key=txt_file.readlines()[0]
		self.setURL()
		self.createConnexion()
		self.arrondissement=3

	def getArrondissement(self):
		return self.arrondissement

	def setArrondissement(self,newArrondissement):
		if(0<(newArrondissement) and int(newArrondissement)<10):
			self.arrondissement=int(newArrondissement)
			print("L'arrondissement a ete change pour "+newArrondissement)
		else:
			print("Arrondissement invalide")

	def getConnexion(self):
		return self.createConnexion()

	def createConnexion(self):
		r = requests.get(self.URL)
		self.jsonFile=r.json()
		

	def setLocation(self,newLoc):
		oldLoc=self.location
		try:
			self.location=newLoc
			self.setURL()
			self.createConnexion()
			self.getMain()
			print("\nLocalisation changée pour : "+newLoc)
		except:
			self.location=oldLoc
			self.setURL()
			self.createConnexion()
			print("\nLocalisation non valide")

	def getLocation(self):
		return self.location

	def setURL(self):
		self.URL='http://api.openweathermap.org/data/2.5/weather?q='+self.location+"&appid="+self.key

	def getMain(self):
		return self.jsonFile["main"]

	def getWeather(self):
		return self.jsonFile["weather"]
	
	def getSky(self):
		return self.getWeather()[0]["main"]

	def printAll(self):
		print(self.jsonFile)

	def getTempKelvin(self):
		return self.getMain()["temp"]

	def getLocationName(self):
		return self.jsonFile["name"]

