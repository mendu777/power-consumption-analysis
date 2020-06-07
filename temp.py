# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('mlr.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('index.html', **locals())
@app.route('/datavis')
def datavis():
    sb1m = Flask.request.files.get('sb1-m.png','')
    return render_template('datavis.html', **locals())

@app.route('/login',methods=["POST"])
def login():
    vol=request.form["vol"]
    sb1=request.form["sb1"]
    sb2=request.form["sb2"]
    sb3=request.form["sb3"]
    gi=request.form["gi"]
    gr=request.form["gr"]
    total=[[int(vol),int(sb1),int(sb2),int(sb3),int(gi),int(gr)]]
    p=model.predict(total)
    p=p[0][0]
    return render_template('index.html',label=p)
if __name__=='__main__':
    app.run(debug=False,port=5000)
