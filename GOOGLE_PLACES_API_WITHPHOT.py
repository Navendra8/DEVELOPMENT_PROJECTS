
def get_place_details(place):
    mykey = "AIzaSyAtzvDoPkWFu8g6urdrhaManQq-zccP9RM"
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&fields=formatted_address,geometry,name,photos,place_id,rating,opening_hours&input={place}&key={mykey}"
    data = requests.get(url)
    c = 0
    if data.status_code == 200:
        data = data.json()
        #print(data['candidates'])
        #return data['candidates']
        for i in data.get("candidates"):
            add = i["formatted_address"]
            opening_hours = i.get("opening_hours")
            rating = i.get('rating')
            try:
                photo_ref = i["photos"][0]['photo_reference']
            except:
                photo_ref = None
            else:
                c += 1
            print("\n Address : ",add)
            print("\n Rating : ",rating)
            print("\n Opening_hours : ",opening_hours)
            #print(photo_ref,i)
            if photo_ref:
                url2 = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={mykey}"
                image = requests.get(url2)
                if image.status_code == 200:
                    with open(f"{place}{c}.jpg","wb") as f:
                        f.write(image.content)
                    img = plt.imread(f"{place}{c}.jpg")
                    plt.rcParams["axes.spines.bottom"] = False
                    plt.rcParams['axes.spines.right'] = False
                    plt.rcParams['axes.spines.top'] = False
                    plt.rcParams['axes.spines.left'] = False
                    plt.imshow(img)
                    plt.xticks([])
                    plt.yticks([])
                    plt.show()
                else:
                    print("\n No image")
    else:
        print("\n Invalid Url.....")
        
place = input("\n Enter any place : ")
d = get_place_details(place)
