import requests
import json
from tkinter import *

class App:
	def __init__(self):
		self.root=Tk()
		self.temp = StringVar()
		self.back=Back()
		self.back.getConnexion()
		print(self.back.getLocation())
		self.location =StringVar()
		self.location.set(self.back.getLocationName())
		self.tempLabel = Label(self.root, textvariable=self.temp)
		self.tempLabel.pack()
		self.locationEntry = Entry(self.root,textvariable=self.location)
		self.locationEntry.pack()
		self.changeLocationButton = Button(self.root, text="Change location", command=lambda : self.changeLocation())
		self.changeLocationButton.pack()
		self.refreshTemp()
		self.root.geometry('200x200+100+100')
		self.root.resizable(False, False)
		self.root.update_idletasks()
		self.root.overrideredirect(True)
		self.root.mainloop()

	def refreshTemp(self):
		self.temp.set(self.CalculateTemp())
		self.root.after(300000,self.refreshTemp)

	def CalculateTemp(self):
		tempKelvin=self.back.getTempKelvin()
		tempKelvinRound=round(tempKelvin,self.back.getArrondissement())
		tempCelsius=tempKelvin - 273.15
		tempCelsiusRound=round(tempCelsius,self.back.getArrondissement())
		return tempCelsiusRound

	def changeLocation(self):
		self.back.setLocation(self.locationEntry.get())
		self.temp.set(self.CalculateTemp())

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
