import pickle
import requests


# for beer in answ.json():
#     print(beer)
#     print("= " * 10)

def filter(abv_min=0,abv_max=9, ibu_min=0, ibu_max=999):
    endpoint = 'https://api.punkapi.com/v2/beers/'
    beers = []
    for i in range(1, 51):
        request = f"https://api.punkapi.com/v2/beers?page={i}&per_page=80"
        answ = requests.get(request)
        try:
            for beer in answ.json():
                if abv_min <= beer['abv'] <= abv_max and ibu_min <= beer['ibu'] <= ibu_max and ('Pilsner' in beer['tagline']
                or'Stout' in beer['tagline']):
                    beers.append((beer['name'], beer['tagline'], beer['description'], beer['abv']))
        except Exception:
            continue
    beers.sort(key=lambda x: x[3], reverse=True)
    print(beers)

filter(3.5, 8, 5, 80)