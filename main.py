from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat=round(results[0]["geometry"]["lat"],2)
            lng=round(results[0]["geometry"]["lng"],2)
            country = results[0]['components']['country']
            cur = results[0]['annotations']['currency']['name']
            # Получаем URL для OpenStreetMap
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион: {region}\nВалюта: {cur}",
                        "map_url": osm_url
                        }

            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nВалюта: {cur}",
                        "map_url": osm_url
                        }

        else:
            print("Данные не найдены")
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


def show_coordinates(event=None):
    city = entry.get()
    result = get_coords(city, key)
    label.config(text=result["coordinates"])
    # Сохраняем URL в глобальной переменной для доступа из другой функции
    global map_url
    map_url = result["map_url"]


def show_map():
    if map_url:
        webbrowser.open(map_url)


def delete():
    entry.delete(0, END)  # Очищаем поле ввода
    label.config(text="Введите город и нажмите Поиск")  # Сбрасываем текст метки


key = '4b118bba547640c0b0a5b30c043600f4'


window = Tk()
window.title("Поиск координат города")
window.geometry("250x170")

map_url = None

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)  # Привязка события нажатия Enter

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

delete_button= Button(text="Очистить", command=delete)
delete_button.pack()

# Запуск приложения
window.mainloop()

