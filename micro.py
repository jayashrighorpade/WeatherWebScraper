from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import *
from tkinter import messagebox

citySpecific = 'https://city.imd.gov.in/citywx/city_weather.php?id='
cityMain = urlopen('https://internal.imd.gov.in/pages/city_weather_main_mausam.php').read()

mainPage = BeautifulSoup(cityMain, 'lxml')
optionTags = mainPage.find_all('option')
optionsText = list()
for optionTag in optionTags:
    optionsText.append(str(optionTag['value']))

root = Tk()
root.title('Weather Info')
root.geometry('300x80')
root.iconbitmap('cloudy.ico')
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)


def showInfo():
    try:
        selectedPage = BeautifulSoup(
            urlopen(citySpecific + clicked.get().replace(' ', '%20')), 'lxml')
        data_unavailable = selectedPage.find('font', size="3")
        if data_unavailable is not None:
            raise Exception(str(data_unavailable.text))
        rowsMain = selectedPage.find_all('td', align="left")
        metrics = list()
        for tag in rowsMain:
            metrics.append(str(tag.font.text)[1:])
        top = Toplevel(master=root)
        top.resizable(False, False)
        top.iconbitmap('cloudy.ico')
        top.geometry('460x430')
        top.title(f'Weather for {clicked.get()}')
        font = ('Arial', 20)
        Label(top, text='Maximum Temp(C):', font=font).grid(row=0, column=0)
        Label(top, text=metrics[0], font=font).grid(row=0, column=1)
        Label(top, text='Departure from Normal(C):',
              font=font).grid(row=1, column=0)
        Label(top, text=metrics[1], font=font).grid(row=1, column=1)

        Label(top, text='Minimum Temp (C):', font=font).grid(row=2, column=0)
        Label(top, text=metrics[2], font=font).grid(row=2, column=1)
        Label(top, text='Departure from Normal(C):',
              font=font).grid(row=3, column=0)
        Label(top, text=metrics[3], font=font).grid(row=3, column=1)
        Label(top, text='24 Hours Rainfall (mm):',
              font=font).grid(row=4, column=0)
        Label(top, text=metrics[4], font=font).grid(row=4, column=1)
        Label(top, text='Relative Humidity at 0830 hrs:',
              font=font).grid(row=5, column=0)
        Label(top, text=metrics[5], font=font).grid(row=5, column=1)
        Label(top, text='Relative Humidity at 1730 hrs:',
              font=font).grid(row=6, column=0)
        Label(top, text=metrics[6], font=font).grid(row=6, column=1)
        Label(top, text='Todays Sunset (IST):',
              font=font).grid(row=7, column=0)
        Label(top, text=metrics[7], font=font).grid(row=7, column=1)
        Label(top, text='Tomorrow\'s Sunrise (IST):',
              font=font).grid(row=8, column=0)
        Label(top, text=metrics[8], font=font).grid(row=8, column=1)
        Label(top, text='Moonset (IST):', font=font).grid(row=9, column=0)
        Label(top, text=metrics[9], font=font).grid(row=9, column=1)
        Label(top, text='Moonrise (IST):', font=font).grid(row=10, column=0)
        Label(top, text=metrics[10], font=font).grid(row=10, column=1)
    except Exception as e:
        messagebox.showerror('An error occured', str(e))

clicked = StringVar()
clicked.set('43025ADILABAD')
drop = OptionMenu(root, clicked, *optionsText).pack()
btn = Button(root, text='Show Info', command=showInfo).pack()
root.mainloop()
