### First create a table in AWS dynamodb.
  1) Table name-> users
  2) Primary key/Partition Key-> email ( it should be string)
  3) Check on default settings box and then create a table
  4) After this on the right side click on Items-> Create item
  5) Then give value to email: demo@gmail.com
  6) Then Click on " + " sign -> select "Append"-> select "string" . In the field type " name" and give any value to it let say "demo".
  7) Again Click on " + " sign -> select "Append"-> select "string" . In the field type "password" and give any value to it let say "Demo@123".
  
### After creating dynamodb table and inserting some values.Login to ubuntu and do following steps.
  1) """ apt-get update -y """
  2) """ apt-get install python3 python3-pip git
  3) 

