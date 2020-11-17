def get_fb_data(key,fields):
    if "," in fields:
        url = f"https://graph.facebook.com/v7.0/me?fields={fields}&access_token={key}"
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
            if "posts" in fields.split(","):
                f = open("myposts.txt",'a+')
                for p in data['posts']['data']: 
                    try:
                        f.write(p.get("created_time")+"\t"+p.get("id")+"\t"+str(p.get("message")))
                        f.write("\n")
                    except:
                        pass
                f.close()
            if "likes" in fields.split(","):
                name = input("\n ENter name : ").lower()
                for i in data["likes"]["data"]:
                    if name in i.get("name").lower():
                        print("\n Name : ",i.get("name"))
                        print("\n Id : ",i.get("id"))
                        print("\n Created at : ",i.get("created_time"))
                    
                
        else:
            print(data.status_code)
            print("\n Invalid code.....")
    else:
        print("\n Invalid fields")
        
        
key = "EAAIEVOKyhdcBAIMZCzLIqEn9rUK6D5KZCx7cwcBgEXW8ftL4DeJmXdlCk7NOspqypwcRaDHSce0NxH3H8YF6qs7iKXnFIIEfQXhmDb91fWzAbD39q9zTCU9rsGMXMhKn6ZCHNBMO2p7jbyZBsSkNtBeqZAOEDZAMWwEjUsrXg08DuX2ZAgB7rIBDfuLqRn2a367jH6CHEUXq94DiZCbT9PMnU7LNZCZAEm9ISgpgr5ea2sVwZDZD"
fields = input("\n Enter your fields , separated : ")
get_fb_data(key,fields)
