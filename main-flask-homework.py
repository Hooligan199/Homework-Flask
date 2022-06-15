import random, string
import pandas as pd
from flask import Flask
from markupsafe import escape
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route("/")
def start():
    return "<h1>Hello</h1>"

@app.route("/requirements/")
def greeting():
    with open("requirements.txt") as file:
        text = ""
        for line in file:
            text += f"<p><b>{line}</b></p>"
    return text

@app.route("/generate-users/")
@app.route("/generate-users/<amount>")
def generator(amount):
    double_string = ""
    for _ in range(int(amount)):
        double_string += f"<p>{fake.name()} " \
                         f"{''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(9))}" \
                         f"@gmail.com</p>"

    return double_string

@app.route("/mean/")
def calculated_csv():
    data = pd.read_csv("hw.csv")
    print(data.columns)


if __name__ == '__main__':
    COSMONAUT_URL = "http://api.open-notify.org/astros.json"

    app.run(debug=True)
