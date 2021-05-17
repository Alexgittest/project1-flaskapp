#!/usr/bin/python3.8

from flask import Flask,request
import json
from datetime import date
import boto3

# S3 bucket name
S3_BUCKET="alex-flask-app-bucket"
today = date.today()
app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    s3 = boto3.resource('s3',verify=False)
    obj = s3.Object(S3_BUCKET, 'birthday.txt')
    data=obj.get()['Body'].read().decode('utf-8')
    people_dict=json.loads(data)
    if request.method == 'POST':
        user=request.form['username']
        dr=request.form['dr']
        people_dict[user]=dr
        people_str=json.dumps(people_dict)
        str(people_dict).encode()
        obj.put(Body=people_str.encode())
        return "Add new user \n"
    else:       
        return "Hello it is flask app \n"

@app.route('/<username>')
def show_user_birthday(username):
    s3 = boto3.resource('s3',verify=False)
    obj = s3.Object(S3_BUCKET, 'birthday.txt')
    data=obj.get()['Body'].read().decode('utf-8')
    people_dict=json.loads(data)
    birthday="Совпадений не найдено"   
    for i in people_dict.keys():
        if i == username:
            birthday=people_dict[i].split(".")
            dr=date(today.year,int(birthday[1]),int(birthday[0]))
            delta=(today-dr).days
            if 0<delta<3:
                birthday="ДР было меньше чем 3 дня назад \n"
            elif -3<delta<0:
                birthday="ДР будет меньше чем через 3 дня \n"
            elif delta==0:
                birthday="ДР Сегодня! \n"
            else:
                birthday="ДР еще не скоро \n"
    return birthday

if __name__=="__main__":
    app.run(port=5000, host='0.0.0.0')
