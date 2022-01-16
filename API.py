import requests
import json

class App:
	def __init__(self):
		self.back=Back()
		self.back.getConnexion()
		action=""
		while(action != "stop"):
			print("\n\nLocalisation actuelle : "+self.back.getLocationName())
			action=input("\n(1) Afficher la température\n(2) Changer la localisation\n(3) Changer les preferences\n")
			if(action=="1"):
				self.printTemp()
			elif(action=="2"):
				newLoc=input("Quelle est votre nouvelle localisation ?")
				self.back.setLocation(newLoc)
			elif(action=="3"):
				self.changePreferences()

	def printTemp(self):
		tempKelvin=self.back.getTempKelvin()
		tempKelvinRound=round(tempKelvin,self.back.getArrondissement())
		tempCelsius=tempKelvin - 273.15
		tempCelsiusRound=round(tempCelsius,self.back.getArrondissement())
		print("\n\nLa température à "+self.back.getLocationName()+" : ")
		print(str(tempCelsiusRound)+"°C")
		print(str(tempKelvinRound)+"°K")

	def changePreferences(self):
		action=""
		while(action!="stop"):
			action=input("\nBienvenue dans le menu de changement des préférences.\
				  \nTaper le numero de la préférence que vous voulez changer (ou bien stop si vous voulez sortir du menu)\
				  \n(1) Arrondissement de la temperautre (arrondissement actuel : "+str(self.back.getArrondissement())+")\n")
			if(action=="1"):
				arrondissement=input("Nouvel arrondissement : ")
				self.back.setArrondissement(arrondissement)

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

	def printAll(self):
		print(self.jsonFile)


	def getTempKelvin(self):
		tempKelvin=self.getMain()["temp"]
		return tempKelvin

	def getLocationName(self):
		locationName=self.jsonFile["name"]
		return locationName

App=App()
App.printTemp()

'''
for element in jsonDoc :
	print(element +" : "+ str(jsonDoc[element]))

'''