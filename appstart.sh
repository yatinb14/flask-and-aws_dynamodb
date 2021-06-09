#!/bin/bash
cd flask_and_aws_dynamodb
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=app.py
nohup flask run --host 0.0.0.0 --port 8000 &
echo "App started"