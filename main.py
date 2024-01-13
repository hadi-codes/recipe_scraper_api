from typing import Union
from recipe_scrapers import scrape_me

from fastapi import FastAPI

app = FastAPI()

recipes_urls = [
    "https://www.chefkoch.de/rezepte/3466261516440078/Kuemmelrotkraut-mit-Ofen-Suesskartoffeln.html",
    "https://www.chefkoch.de/rezepte/1631611270752104/Vegetarische-Frikadellen.html",
    "https://www.chefkoch.de/rezepte/2352371374010722/Cremiger-Nudelauflauf-mit-Tomaten-und-Mozzarella.html",
    "https://www.chefkoch.de/rezepte/802701184066929/Bester-vegetarischer-Nudelauflauf.html",
    "https://www.chefkoch.de/rezepte/745721177147257/Lasagne.html",
    "https://www.chefkoch.de/rezepte/2293251365606285/Bulgogi-mariniertes-koreanisches-Rindfleisch.html",
]


@app.get("/recipe/")
def read_item(url: str):
    if not url:
        return {"error": "url is required"}
    scraper = scrape_me(url)
    json = scraper.to_json()
    return restructure_recipe(json)

@app.get("/recipes/")
def get_recipes():
    recipes = []
    for url in recipes_urls:
        json = read_item(url)
        recipes.append(json)
    return recipes


def restructure_recipe(recipe: dict) -> dict:
    new_recipe = {}
    new_recipe["name"] = recipe["title"]
    new_recipe["info"] = recipe["description"]
    new_recipe["imageUrl"] = recipe["image"]
    new_recipe["ingredients"] = recipe["ingredients"]
    new_recipe["time"] = recipe["cook_time"]
    new_recipe["tags"] = []
    category= recipe["category"]
    if category:
        new_recipe["tags"].append(recipe["category"])
    
    # convert instructions_list to list of objects (name, time=0 )
    new_recipe["instructions"] = []
    for instruction in recipe["instructions_list"]:
        new_recipe["instructions"].append({"name": instruction, "time": 0})
    # split splace and try to get number
    yields = recipe["yields"]
    yield_number = yields.split(" ")[0]
    if yield_number.isdigit():
        new_recipe["servings"] = int(yield_number)
    else:
        new_recipe["servings"] = 1
    return new_recipe
