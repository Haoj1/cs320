# project: p4
# submitter: hbian8
# partner: none
# hours: 10

from cProfile import label
from math import nan
from operator import index
from re import L
import pandas as pd
from flask import Flask, request, jsonify, Response
import csv
import pandas as pd
import re
import time
import matplotlib.pyplot as plt
import matplotlib
from io import StringIO
import numpy as np
from matplotlib.pyplot import MultipleLocator

pd.options.mode.chained_assignment = None  # default='warn'

# source of data
# https://www.wihealthatlas.org/obesity/download

typeBrown_count = 0
typeBlue_count = 0
home_visit = 0
app = Flask(__name__)
# df = pd.read_csv("main.csv")

@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()
    global typeBrown_count
    global typeBlue_count
    global home_visit
    home_visit += 1
    if home_visit > 10:
        if typeBrown_count >= typeBlue_count:
            html = html.replace("blue", "brown")
        else:
            html = html.replace("brown", "blue")
    else:
        if home_visit % 2 == 1:
            html = html.replace("blue", "brown")
        else:
            html = html.replace("brown", "blue")
    return html

@app.route('/browse.html')
def browser_handler():
    html = str()
    df = pd.read_csv("main.csv")
    html = str(df.to_html())
    html = "<h1>Browse</h1>" + html
    return f"<html>{html}<html>"

@app.route('/email', methods=["POST"])
def email():
    email = str(request.data, "utf-8")
    if re.match(r"\w+@+\w+\.\w+", email): # 1
        with open("emails.txt", "a") as f: # open file in append mode
            f.write(email + "\n") # 2
        with open("emails.txt", "r") as f:    
            sub_num = len(f.readlines())
        return jsonify(f"thanks, you're subscriber number {sub_num}!")
    return jsonify(f"it is invalid email address") # 3

@app.route('/donate.html')
def donate():
    args = dict(request.args)
    type = args.get("type")
    global typeBrown_count
    global typeBlue_count
    if type == "brown":
        typeBrown_count += 1
    if type == "blue":
        typeBlue_count += 1
    
    html = "Thanks for your donate"
    html = f"<h1>{html}</h1>"
    return f"<html>{html}<html>"

request_user = {}
@app.route('/browse.json')
def browse_json():
    global request_user
    df = pd.read_csv('main.csv')
    if request.remote_addr not in request_user:
        request_user[request.remote_addr] = time.time()
        return jsonify(df.to_dict(orient='index'))
    else:
        if time.time() - request_user[request.remote_addr] > 60:
            request_user[request.remote_addr] = time.time()
            return jsonify(df.to_dict(orient='index'))
        else:
            html = 'too many requst in short period'
        return Response(html, status=429, headers = {"Retry-After":60})

@app.route('/dashboard_1.svg')
def dashboard_1():
    df = pd.read_csv('main.csv')
    # print(df["obese"][0] == pd.NA)
    for i in range(len(df["obese"])):
        if not (df["obese"][i] >= 0):
            df["obese"][i] = 0
    if 'cmap' not in request.args:
        figure, axes=plt.subplots(figsize=(8,4))
        # pd.Series(df["obese"][0:25]).plot.line(ax=ax)
        # df[0:25].plot.bar(x = 'zip', y = 'obese')
        # obese = df['obese'][0:25]
        # zip = df['zip'][0:25]
        # obese = []
        # zip = []
        # for i in range(25):
        #     zip.append(df['zip'][i])
        #     if df['obese'][i] == nan:
        #         obese.append(0)
        #     else:
        #         obese.append(df['obese'][i])
        plt.scatter(x=df["zip"][0:25], y=df["pop"][0:25], cmap='viridis')
        # plt.scatter(x=df["zip"][0:25], y=df["pop"][0:25], c=df["obese"][0:25], cmap='viridis')
        # plt.colorbar()
        plt.xticks(df["zip"][0:25], rotation=60)
        axes.set_ylabel("population")
        axes.set_xlabel("zipcode")
        axes.set_title("population vs zipcode")
    else:
        if dict(request.args).get('cmap') == 'population':
            figure, axes=plt.subplots(figsize=(8,4))
            plt.scatter(x=df["zip"][0:25], y=df["pop"][0:25], c=df["obese"][0:25], cmap='viridis')
            plt.xticks(df["zip"][0:25], rotation=60)
            plt.colorbar(label = 'Obese Number')

            axes.set_ylabel("population")
            axes.set_xlabel("zipcode")
            axes.set_title("population with obese quantity vs zipcode")
    file =StringIO()
    plt.tight_layout()
    figure.savefig(file, format="svg")
    plt.close()
    file=file.getvalue()
    head={"Content-Type":"image/svg+xml"}
    return  Response(file, headers=head)

@app.route('/dashboard_2.svg')
def dashboard_2():
    figure, axes=plt.subplots(figsize=(8,6))
    df = pd.read_csv('main.csv')
    obese = {}
    for i in range(len(df['age'])):
    # if df['obese'][i] >= 0:
    #     print(df['obese'][i])
        if df['age'][i] not in obese:
            if df['obese'][i] >= 0:
                obese[df['age'][i]] = df['obese'][i]
            else:
                obese[df['age'][i]] = 0
        else:
            if df['obese'][i] >= 0:
                obese[df['age'][i]] += df['obese'][i]
    # plot = pd.DataFrame(obese, index=['age']).plot.bar(ax=axes)
    plt.bar(x = df['age'], height = df['obese'])
    axes.set_ylabel("obese")
    axes.set_xlabel("age")
    axes.set_title("age vs obese")
    file =StringIO()
    plt.tight_layout()
    figure.savefig(file, format="svg")
    plt.close()
    file=file.getvalue()
    head={"Content-Type":"image/svg+xml"}
    return  Response(file, headers=head)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!


# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.
