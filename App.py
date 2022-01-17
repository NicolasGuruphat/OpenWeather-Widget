from tkinter import *
from Back import Back

class App:
	
	def __init__(self):
		self.root=Tk()#Creation of the main window 
		
		self.back=Back()#Creation of the back that use the API
		self.back.getConnexion()#Creation of the connexion with the webApp
		#self.back.printAll()
		self.back.getSky()
		#Construct of the window's elements
		self.temp = StringVar()
		self.location =StringVar()
		self.sky =StringVar()
		self.location.set(self.back.getLocationName())
		self.tempLabel = Label(self.root, textvariable=self.temp)
		self.locationEntry = Entry(self.root,textvariable=self.location)
		self.changeLocationButton = Button(self.root, text="Change location", command=lambda : self.changeLocation())
		self.skyLabel=Label(self.root, textvariable=self.sky)
		self.tempLabel.pack()
		self.locationEntry.pack()
		self.changeLocationButton.pack()
		self.skyLabel.pack()

		#Root setting
		self.root.geometry('200x200+100+100')
		self.root.resizable(False, False)
		self.root.update_idletasks()
		self.root.overrideredirect(True)
		
		self.refresh() #Call of the loop method

		self.root.mainloop()

	def refresh(self):
		'''
		Refresh data every t milliseconds
		'''
		t=300000
		self.temp.set(self.CalculateTemp())
		self.sky.set(self.back.getSky())
		self.root.after(t,self.refreshTemp)

	def CalculateTemp(self) -> int :
		'''
		Calculate and return celsius round temperature from the API data
		'''
		tempKelvin=self.back.getTempKelvin()
		tempKelvinRound=round(tempKelvin,self.back.getArrondissement())
		tempCelsius=tempKelvin - 273.15
		tempCelsiusRound=round(tempCelsius,self.back.getArrondissement())
		return tempCelsiusRound

	def changeLocation(self):
		'''
		Change the location that the API will call
		'''
		self.back.setLocation(self.locationEntry.get())
		self.temp.set(self.CalculateTemp())


App=App()
