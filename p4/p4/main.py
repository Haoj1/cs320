import pandas as pd
from flask import Flask, request, jsonify, Response
import re,time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from io import StringIO

matplotlib.use('Agg')
app = Flask(__name__)
df = pd.read_csv("main.csv")


@app.route('/browse.html')
def Browse():
    html=str()
    html=df.to_html()
    table="<h1>{}</h1>".format("Browse")+html
    return table

count_home=0
count_a=0
count_b=0
@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()
    global count_home
    count_home+=1
    if count_home <=10:
        if count_home%2==0:
            html=html
        else:
            html=html.replace("red","blue")
            html=html.replace("from=A","from=B")
    else:
        if count_a>=count_b:
            html=html
        else:
            html=html.replace("red","blue")
            html=html.replace("from=A","from=B")
    return html

num_subscribed=0
@app.route('/email', methods=["POST"])
def email():
    email = str(request.data, "utf-8")
    global num_subscribed
    if re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.{1}...", email): # 1
        with open("emails.txt", "a") as f: # open file in append mode
            f.write(email + "\n") # 2
        num_subscribed+=1
        return jsonify(f"thanks, you're subscriber number {num_subscribed}!")
    return jsonify(f"Please enter a valid email.") # 3


@app.route('/donate.html')
def donation():
    args=dict(request.args)
    version=args.get("from")
    if version=="A":
        global count_a
        count_a+=1
    if version=="B":
        global count_b
        count_b+=1
    return "<h1>{}</h1>".format("A little love is the big kind.")

#last_vist=0
user={}
@app.route('/browse.json')
def browseJson():
   # global last_visit
    global user
    df2=df.to_dict(orient='index')
    if request.remote_addr not in user:
        user[request.remote_addr]=time.time()
        return jsonify(df2)
    elif time.time() - user[request.remote_addr] >60:
        user[request.remote_addr]=time.time()
        return jsonify(df2)
    else:
        html="too many request, come back later."
        return Response(html,status=429,headers={"Retry-After":60})

@app.route('/dashboard_1.svg')
def dashboard_1():
    fig,ax=plt.subplots(figsize=(3,2))
    if "cmap" not in request.args:
        fig, ax=plt.subplots(figsize=(6,4))
        pd.Series(df["Count"][15:39]).plot.line(ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel("Time")
        ax.set_title("Bike count on 6/24/2015")

        f=StringIO()
        plt.tight_layout()
        fig.savefig(f,format="svg")
        plt.close()
        svg=f.getvalue()
        hdr={"Content-Type":"image/svg+xml"}
        return  Response(svg,headers=hdr)
    else: 
        fig, ax=plt.subplots(figsize=(6,4))
        pd.Series(df["Count"][39:]).plot.line(ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel("Time")
        ax.set_title("Bike count on 6/25/2015")

        f=StringIO()
        plt.tight_layout()
        fig.savefig(f,format="svg")
        plt.close()
        svg=f.getvalue()
        hdr={"Content-Type":"image/svg+xml"}
        return  Response(svg,headers=hdr) # return the other




@app.route('/dashboard_2.svg')
def dashboard_2():
    fig, ax=plt.subplots(figsize=(6,4))
    pd.Series(df["Count"][0:15]).plot.line(ax=ax)
    ax.set_ylabel("Count")
    ax.set_xlabel("Time")
    ax.set_title("Bike count on 6/23/2015")

    f=StringIO()
    plt.tight_layout()
    fig.savefig(f,format="svg")
    plt.close()
    svg=f.getvalue()
    hdr={"Content-Type":"image/svg+xml"}
    return  Response(svg,headers=hdr)
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!