from pprint import pprint
import boto3
import json
import csv
import datetime
import os
import random
import base64
import decimal
from pymongo import MongoClient
import bson

def lambda_handler(event, context):
    
    HOST = '3.88.188.113'
    PORT = '27017'
    username = 'taxiAppUser'
    pwd = 'Test1234'
    DB_NAME = 'TaxiApp_DB'
    taxiCollection='taxis'
    
    db_conn = MongoClient(f'mongodb://{username}:{pwd}@{HOST}:{PORT}/?authSource={DB_NAME}&authMechanism=SCRAM-SHA-1')
    print(f'mongodb://{username}:{pwd}@{HOST}:{PORT}')
    db = db_conn[DB_NAME]
    
    for myRecord in event['Records']:
        print(myRecord['body'])
        data = json.loads(myRecord['body'])
        collection = db[taxiCollection]
        document = collection.insert_one(data)
        #document = collection.insert_many(myRecord['body'])
        print(document.inserted_id)
   
