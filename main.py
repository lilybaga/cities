from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, lanuage="ru")
        if results:
            lat=round(results[0]["geometry"]["lat"],2)
            lng=round(results[0]["geometry"]["lng"],2)
            country = results[0]['components']['country']
            region = results[0]['components']['state']
            return f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион: {region}"

        else:
            print("Данные не найдены")
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coords(city, key)
    label.config(text=coordinates)

key = '4b118bba547640c0b0a5b30c043600f4'


window = Tk()
window.title("Поиск координат города")
window.geometry("200x100")

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)  # Привязка события нажатия Enter

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

# Запуск приложения
window.mainloop()

