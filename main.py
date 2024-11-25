from opencage.geocoder import OpenCageGeocode


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query=city
        results = geocoder.geocode(query)
        if results:
            lat=round(results[0]["geometry"]["lat"],3)
            lng=round(results[0]["geometry"]["lng"],3)

            return f"Широта:{lat}, Долгота:{lng}"
        else:
            print("Данные не найдены")
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


key = '4b118bba547640c0b0a5b30c043600f4'
city="Уфа"
coordinates=get_coords(city, key)

if coordinates:
    print(f"Координаты города {city}: {coordinates}")