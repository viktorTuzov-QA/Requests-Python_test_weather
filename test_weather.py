import requests
from apikey import apiKey


def test_openweather():

    """
    SPK-1. Positive case
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    city = "Ufa"
    units = "metric"
    params = {"q" : city, "units" : units, "appid" : apiKey}

    response = requests.get(url, params=params)

    assert response.status_code == 200

    json = response.json()

    assert json['coord']
    assert isinstance(json['coord'], dict)
    assert json['coord']['lon']
    assert isinstance(json['coord']['lon'], float), 'over class "lon"'
    assert json['coord']['lat']
    assert isinstance(json['coord']['lat'], float)

    assert json['weather']
    assert isinstance(json['weather'], list)
    assert json['weather'][0]['id']
    assert isinstance(json['weather'][0]['id'], int)
    assert json['weather'][0]['main']
    assert isinstance(json['weather'][0]['main'], str)
    assert json['weather'][0]['description']
    assert isinstance(json['weather'][0]['description'], str)
    assert json['weather'][0]['icon']
    assert isinstance(json['weather'][0]['icon'], str)

    assert json['base']
    assert isinstance(json['base'], str)

    assert json['main']
    assert isinstance(json['main'], dict)
    assert json['main']['temp']
    assert isinstance(json['main']['temp'], float)
    assert json['main']['feels_like']
    assert isinstance(json['main']['feels_like'], float)
    assert json['main']['temp_min']
    assert isinstance(json['main']['temp_min'], float)
    assert json['main']['temp_max']
    assert isinstance(json['main']['temp_max'], float)
    assert json['main']['pressure']
    assert isinstance(json['main']['pressure'], int)
    assert json['main']['humidity']
    assert isinstance(json['main']['humidity'], int)
    assert json['main']['sea_level']
    assert isinstance(json['main']['sea_level'], int)
    assert json['main']['grnd_level']
    assert isinstance(json['main']['grnd_level'], int)

    assert json['visibility']
    assert isinstance(json['visibility'], int)

    assert json['wind']
    assert isinstance(json['wind'], dict)
    assert json['wind']['speed']
    assert isinstance(json['wind']['speed'], float)
    assert json['wind']['deg']
    assert isinstance(json['wind']['deg'], int)
    assert json['wind']['gust']
    assert isinstance(json['wind']['gust'], float)

    assert json['clouds']
    assert isinstance(json['clouds'], dict)
    assert json['clouds']['all']
    assert isinstance(json['clouds']['all'], int)

    assert json['dt']
    assert isinstance(json['dt'], int)

    assert json['sys']
    assert isinstance(json['sys'], dict)
    assert json['sys']['type']
    assert isinstance(json['sys']['type'], int)
    assert json['sys']['id']
    assert isinstance(json['sys']['id'], int)
    assert json['sys']['country']
    assert isinstance(json['sys']['country'], str)
    assert json['sys']['sunrise']
    assert isinstance(json['sys']['sunrise'], int)
    assert json['sys']['sunset']
    assert isinstance(json['sys']['sunset'], int)

    assert json['timezone']
    assert isinstance(json['timezone'], int)

    assert json['id']
    assert isinstance(json['id'], int)

    assert json['name']
    assert isinstance(json['name'], str)

    assert json['cod']
    assert isinstance(json['cod'], int)









    



    


   
   
   
    
    