import os
from flask import Flask, render_template, request, session, redirect
import key_config as keys
#from dynamoDB_create_table import *
from botocore.exceptions import ClientError
import boto3 
from flask_session.__init__ import Session

app = Flask(__name__)
app.secret_key = 'your secret key'

region_name = os.getenv("REGION_NAME")



dynamodb = boto3.resource('dynamodb',
                    region_name=region_name)

from boto3.dynamodb.conditions import Key, Attr

#@app.route('/')
#def index():
#    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        
        table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
        msg = "Registration Complete. Please Login to your account !"
    
        return render_template('login.html',msg = msg)
    return render_template('index.html')


@app.route('/login')
def login():    
    return render_template('login.html')


@app.route('/home',methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            
            #return render_template("home.html",name = name)
            return redirect('https://thinknyx.com')

    return render_template("login.html")

#@app.route('/home')
#def home():
#    return render_template('home.html')

@app.route("/logout",methods=['GET', 'POST'])  
def logout():  
    session.clear()

    return render_template('login.html')



if __name__ == "__main__":
    
    app.run(debug=True)

