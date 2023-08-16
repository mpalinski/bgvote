from flask import Flask, request, render_template, render_template_string, session, redirect, url_for
from flask_session import Session
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
app.debug = True  # Enable debugging mode
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()