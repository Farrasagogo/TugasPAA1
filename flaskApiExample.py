#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Muhammad Taqiyuddin Al Farras',
                       'email': '222410102024@mail.unej.ac.id'})
app.run()