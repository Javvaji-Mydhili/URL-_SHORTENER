#steps of projet:
#1.design the app
#2.import modules
#3.design app using "tkinter"
#4.create main function to convert URL using "pyshortener " modules



import pyshorteners
from tkinter import *

def generateUrl():
    shorterClass = pyshorteners.Shortener()
    longUrl = url_field.get()
    shortUrl = shorterClass.tinyurl.short(longUrl)
    url_field.delete(0, END)
    url_field.insert(0, shortUrl)


my_app = Tk()
my_app.geometry("400x200")
my_app.title("URL Shorter")

app_title = Label(my_app, text="My URL Shorter",font=("century 25 bold"))
app_title.pack(pady=20)

label = Label(my_app, text="Enter URL:",font=("century 10"))
label.pack()
url_field = Entry(my_app, font=("century 12"), width=43)
url_field.pack(pady=10)
bttn =Button(my_app, text="Generate short URL", font=("century 12 bold"),command=generateUrl, width=17, height=1)
bttn.pack()

my_app.mainloop()

get_ipython().system('pip install pyshorteners')

