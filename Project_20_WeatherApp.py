import requests
import json
underline="*"*150
def weather(lat,lon):
    """This function take latitude and longitude as a variable and put it in OPEN WEATHER API for fetching weather condition"""
    url=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=0db69a6afbd22316a026b102cd029a2e&units=metric")
    # Raise an HTTPError for bad responses (4xx or 5xx)
    status = url.status_code
    url.raise_for_status()
    parser_url=json.loads(url.text)
    for i in parser_url["weather"]:
        #This will tell description and weather condition of a place
        print(f"The weather will be:{i['main']}\nThe description for the weather:{i['description']}")
        print(underline)
        #It is just for specifying the output
        print("The temperature are in degree CELSIUS and pressure are in mb")
    for keys, values in parser_url["main"].items():
        #It will tell about temperature humidity and pressure of a place
        print(f"{keys}={values}")
    print(underline)
    for key,value in parser_url["wind"].items():
        #it will tell about wind speed
        print(f"wind: {key}= {value} km/h")
    print(underline)
def menu():
    """This function is helping for finding latitude and longitude of a place."""
    try:
        District_name=input("Give your district name:".title())
        # It identify for for perfect length of district name given by the user.
        if len(District_name)==0 or len(District_name)>30:
            print( "Give correct district name")
        #It identify for is any numbers are present in district name or not.
        elif District_name.isnumeric():
            print("You have given invalid district name as in District name there is no numbers are present in District name")
        #It identify for any special characters present in district name or not.
        elif District_name.isalnum()==False:
            print("You have given invalid district name there is no special characters present in the district name")
        else:
            url=requests.get(f"https://us1.locationiq.com/v1/search?key=pk.aa094583c11c97bd4043729a193b7486&q={District_name},India&format=json")
            # Raise an HTTPError for bad responses (4xx or 5xx)
            status = url.status_code
            url.raise_for_status()
            parser_url=json.loads(url.text)
            for i in parser_url:
                #This will tell abot latitude and longitude as well as a description of a place given by the user.
                lat=i["lat"]
                lon=i["lon"]
                print(i["display_name"])
                weather(lat,lon)
                break
    except Exception as e:
        print(f"The problem occurred is this {e}\n sorry for the inconvenience")
menu()
while True:
    try:
        ask=int(input("Do you want to continue{1} or exit{2} the Weather App\nType 1 for continue and 2 for exit:"))
        if ask==1:
            menu()
        elif ask==2:
            print("You have been successfully exited from the WeatherApp")
            break
        else:
            print("Give your prefer option only by typing 1 and 2")
    except Exception as e:
        print(f"The problem occurred is this {e}\nSorry for the inconvenience")