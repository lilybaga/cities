from opencage.geocoder import OpenCageGeocode


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, lanuage="ru")
        if results:
            lat=round(results[0]["geometry"]["lat"],2)
            lng=round(results[0]["geometry"]["lng"],2)

            return f"Широта:{lat}, Долгота:{lng}"
        else:
            print("Данные не найдены")
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


key = '4b118bba547640c0b0a5b30c043600f4'
city="Орск"
coordinates=get_coords(city, key)

if coordinates:
    print(f"Координаты города {city}: {coordinates}")