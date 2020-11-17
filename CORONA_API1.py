import requests

url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewiseSorted"

headers = {
    'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
    'x-rapidapi-key': "a88ff77402mshb59de67584167e6p113a98jsncad39a9d4c55"
    }

response = requests.request("GET", url, headers=headers)
if response.status_code == 200:
    response = response.json()
    print("\n 1. Particular State \n 2. Top five states facing corona \n 3. Total Cases ")
    ch = int(input("\n Choose any option from aobove 1/2 : "))
    if ch == 2:
        five = response[1:6]
        for i in five:
            if i.get("id"):
                print("*"*80)
                print("\n State name : ",i.get("name"))
                print("\n Total Cases : ",i.get("cases"))
                print("\n Recovered : ",i.get("recovered"))
                print("\n Total Deaths : ",i.get("recovered"))
                print("*"*80)
    elif ch == 1:
        state = input("\n Enter any state : ")
        for i in response:
            if i["name"].lower() == state.lower():
                print("\n Total cases : ",i["cases"])
                print("\n Recovered : ",i["recovered"])
                print("\n Total deaths : ",i["deaths"])
        else:
            print("\n Enter correct state")
    elif ch == 3:
        d = response[0]
        print("\n Total Cases : ",d["cases"])
        print("\n Recovered : ",d["recovered"])
        print("\n Deaths : ",d["deaths"])
    else:
        print("\n Invalid Choice")
else:
    print("\n Invalid Url")
