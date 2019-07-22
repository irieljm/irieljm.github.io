from flask import Flask, render_template, url_for, request, render_template_string
from app import app
import requests, json


@app.route('/')
def index():
	url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Dessert"
	cakes = requests.get(url).json().get("meals", [])
	return render_template("cake_designs.html", cakes=cakes)