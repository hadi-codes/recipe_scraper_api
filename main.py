from typing import Union
from recipe_scrapers import scrape_me

from fastapi import FastAPI

app = FastAPI()


@app.get("/recipe/")
def read_item(url: str):
    if not url:
        return {"error": "url is required"}
    scraper = scrape_me(url)
    return scraper.to_json()
