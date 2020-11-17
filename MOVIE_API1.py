

import matplotlib.pyplot as plt
def get_movie_data(title):
    key = "e22bdd41"
    url = f"http://www.omdbapi.com/?t={title}&apikey={key}"
    page = requests.get(url)
    if page.status_code == 200:
        data = page.json()
        year = data.get('Year')
        release = data.get('Released')
        run_time = data.get('Runtime')
        genre = data.get('Genre')
        actors = data.get('Actors')
        plot = data.get("Plot")
        lang = data.get("Language")
        poster = data.get("Poster")
        ratings = data.get("imdbRating")
        typ = data.get("type")
        print(".........Details.........")
        print("\n Year : ",year)
        print("\n Release : ",release)
        print("\n Genre : ",genre)
        print("\n Plot : ",plot)
        print("\n Language : ",lang)
        print("\n Ratings  : ",ratings)
        if poster:
            img = requests.get(poster)
            with open(f"{title}.jpg","wb") as fp:
                fp.write(img.content)
            image = plt.imread(f"{title}.jpg")
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])
            plt.rcParams["axes.spines.bottom"] = True
            plt.rcParams['axes.spines.right'] = True
            plt.show()
    else:
        print("\n Invalid URL")
        
        
get_movie_data("Uri")
