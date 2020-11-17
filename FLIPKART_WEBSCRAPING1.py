

def get_product_details(product):
    url = f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
    page = requests.get(url)
    if page.status_code == 200:
        data = BeautifulSoup(page.content,'html')
        names = []
        for i in data.find_all("div",attrs={"class":"_3wU53n"}):
            names.append(i.text)
        ratings = []
        for i in data.find_all("div",attrs={"class":"hGSR34"}):
            ratings.append(i.text)
        dis_price = []
        for i in data.find_all("div",attrs={"class":"_1vC4OE _2rQ-NK"}):
            dis_price.append(i.text)
        actual_price = []
        for i in data.find_all("div",attrs={"class":"_3auQ3N _2GcJzG"}):
            actual_price.append(i.text)
        for n,r,d,a in zip(names,ratings,dis_price,actual_price):
            print("*"*80)
            print(f"Name : {n}".center(80))
            print(f"Rating : {r}".center(80))
            print(f"After Discount Price : {d}".center(80))
            print(f"Actual Price : {d}".center(80))
            print("*"*80)
    else:
        return "Invalid Url"
    
product = input("\n Enter product : ")
get_product_details(product)
