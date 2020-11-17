import requests
import matplotlib.pyplot as plt
def get_weather(city,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        desc = data['weather'][0]['description']
        temp = round(data['main']['temp'] - 273.15,2)
        humidity = data['main']['humidity']
        min_temp = data['main']['temp_min'] - 273.15
        max_temp = data['main']['temp_max'] - 273.15
        country = data['sys']['country']
        icon = data['weather'][0]['icon']
        print("Details".center(80,"*"))
        print("#"*80)
        print("\n Description : ",desc)
        print("\n Temperature : ",temp)
        print("\n Humidity : ",humidity)
        print("\n Minimum Temperature : ",min_temp)
        print("\n Maximum Temperature : ",max_temp)
        print("\n Country : ",country)
        print("#"*80)
        u= f"http://openweathermap.org/img/w/{icon}.png"
        img = requests.get(u)
        with open(f"{city}.jpg",'wb') as f:
            f.write(img.content)
        image = plt.imread(f"{city}.jpg")
        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])
        plt.show()
    else:
        print("\n Invalid url ",data.status_code)
    
api_key = "e9034b1eee3034977886c9f275b27127"
city = input("\n Enter your city name : ")
get_weather(city,api_key)
