import requests, json

def obtener_temperatura_ciudad_guatemala():
    api_key = '8c52ffbf4c6cf9f139cf87594ce726ce'
    lat = 14.6037521797265
    lon = -90.48925798227378
    Baseurl = 'https://api.openweathermap.org/data/2.5/weather?'
    url = Baseurl + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key 
    response = requests.get(url)
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        return temperature - 273.15
    else:
        # showing the error message
        print("Error en el HTTP request")
        return None
    


temperatura = obtener_temperatura_ciudad_guatemala()

