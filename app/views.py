from flask import Flask, render_template, url_for, request, render_template_string
from app import app
import requests, json


@app.route('/')
def index():
	return render_template_string('hello {{ what }}', what='world')