# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:10:11 2020

@author: CandyZack
"""
import requests
import click

@click.command()
@click.argument('command')
@click.argument('key')
@click.argument('value', nargs=-1)
def main(command, key, value):

    if command == 'get':
        URL = "https://czdatastore.herokuapp.com/get/"+str(key)
        response = requests.get(url=URL)
        data = response.json()
        result = data['result']
        if result=='':
            result = 'null'
        print("output : ", result)
    elif command == 'set':
        URL = "https://czdatastore.herokuapp.com/set/"+str(key)+':'+ str(value[0])
        response = requests.get(url=URL)
        data = response.json()
        print("output : ",data['message'])
    elif command == 'reset':
        pw = key
        URL = "https://czdatastore.herokuapp.com/reset/"+str(pw)
        response = requests.get(url=URL)
        data = response.json()
        result = data['message']
        print("output : ",result)

if __name__ == "__main__":
    main()
