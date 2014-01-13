__author__ = 'lanjun'

from flask import Flask
app = Flask(__name__)
from app import login
from app import userViews


