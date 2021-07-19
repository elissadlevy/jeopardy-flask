import requests
import random

categoriesRequested = 100
categories = requests.get(f'http://jservice.io/api/categories?count={categoriesRequested}').json()

categoriesOffered = 5
categories = random.choices(categories, k=categoriesOffered)
categoryList = []

for category in categories:
    categoryList.append(category["title"])