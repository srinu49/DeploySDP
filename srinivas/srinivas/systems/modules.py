from wsgiref import headers
import requests
import os

def invoke_api_extracthunamobject(contents):
    print("Content received")
    #url = "http://localhost:8080/function/mqttextracthuman" 
    url = "http://127.0.0.1:8080/function/mqttextracthuman"
    headers={}
    response = requests.post(url, data=contents, headers=headers)

def invoke_api_sendemail(contents):
    url = "http://127.0.0.1:8080/function/sendemail" 
    headers={}
    response = requests.post(url, data=contents, headers=headers)
