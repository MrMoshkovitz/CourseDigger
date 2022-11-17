from flask import Flask, jsonify, request
app = Flask(__name__)
import requests
from json import loads, dumps

limit = loads(requests.get('https://api.coursera.org/api/courses.v1').text)['paging']['total']
print(limit)