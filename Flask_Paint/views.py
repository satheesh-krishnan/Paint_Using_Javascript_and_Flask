from flask import Flask,render_template,flash,redirect,request
from app import app
from model import models
import json

global code
code=[]
global d
d=''    
@app.route('/post',methods=['GET','POST'])
def post():
        conn=models()
        
        if request.method=="POST":
             s=request.form['json_str']
             l=json.loads(s)
             a=0
             while a<len(l)-1:
                 conn.inset(l[a],l[len(l)-1])
                 a+=1
        return render_template('new.html')     

        
        
@app.route('/gett/',methods=['GET','POST'])
def gett():
       
        if request.method=="GET":
            conn=models()
            p=conn.ret()
            s=[]
            for each in p:
                
                s.append(str(each))
        
            global code
            code=s[:]
            
            return json.dumps(s)
        return render_template('new.html')
      

@app.route('/pop/',methods=['GET','POST'])
def pop():
        
        
        return render_template('win.html') 

@app.route('/gtt/',methods=['GET','POST']) 
def gtt():
        conn=models()
       
        each=request.args.get('js')
    
        each=json.loads(each)
        d=conn.retf(each)
    
        return json.dumps(d)
       
