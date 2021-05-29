### First create a table in AWS dynamodb.
  1) Table name-> users
  2) Primary key/Partition Key-> email ( it should be string)
  3) Check on default settings box and then create a table
  4) After this on the right side click on Items-> Create item
  5) Then give value to email: demo@gmail.com
  6) Then Click on " + " sign -> select "Append"-> select "string" . In the field type " name" and give any value to it let say "demo".
  7) Again Click on " + " sign -> select "Append"-> select "string" . In the field type "password" and give any value to it let say "Demo@123".
  
  
### After creating dynamodb table and inserting some values.Login to ubuntu and run some commands.
  ```
  - apt-get update -y 
  - apt-get install python3 python3-pip git
  
  ```
### Then clone code ,go inside _flask-and-aws_dynamodb_ folder, install libraries from _requirements.txt_, update  access key and secret access key in _key_config.py_ file,also you need to pass environment var for region_name.
```
- git clone https://github.com/yatinb14/flask-and-aws_dynamodb.git
- cd flask-and-aws_dynamodb/
- ls
- pip3 install -r requirements.txt
- export REGION_NAME=us-east-2
- echo $REGION_NAME

```

### Last step is to run our code
```
- export FLASK_APP=app.py
- export FLASK_ENV=development
- flask run --host 0.0.0.0 --port 8000

```
**It will give the output like**

 Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.31.44.4:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 122-780-811

**You can check that app is running on your ```publicip:portnumber/login``` eg: http://64.65.222.37:8000/login**

