from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'Config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()

        # (City, Country, Temp_celsius, Temp_fahrenheit, Icon, Weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']

        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final

    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = 'Weather Icons/{}.png'.format(weather[4])
        temp_label['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_label['text'] = '{}'.format(weather[5])

    else:
        messagebox.showerror('Oops!', f'Can not find city {city}. Please check spelling.')


# App dimension
app = Tk()
app.title("Hello Weather")
app_width = 700
app_height = 350
app.configure(bg='#121212')
app.geometry(f"{app_width}x{app_height}")
app.minsize(500, 250)
app.maxsize(900, 450)
app.iconbitmap('E:\Weather Application (Python)\Weather Icons\App Icon.ico')

# City Info
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

# Button
search_button = Button(app, text='Search', width=9, command=search, bg='#282828', fg='#B3B3B3')
search_button.pack()

# Labels
location_label = Label(app, text='', font="Roboto 20", fg='White', bg='#121212')
location_label.pack()

img = PhotoImage(file='')
image = Label(app, image=img, bg='#121212')
image.pack()

temp_label = Label(app, text='', fg='#B3B3B3', bg='#121212')
temp_label.pack()

weather_label = Label(app, text='', fg='#B3B3B3', bg='#121212')
weather_label.pack()

name_label = Label(app, text='Created by Kratarth Singh', fg='#B3B3B3', bg='#121212')
name_label.pack(pady=50)

app.mainloop()
