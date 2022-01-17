from tkinter import *
from Back import Back

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


App=App()
