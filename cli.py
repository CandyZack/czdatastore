import requests
import click

@click.command()
@click.argument('command')
@click.argument('key')
@click.argument('value', nargs=-1)
def main(command, key, value):
    project_host_url = "https://czdatastore.herokuapp.com"
    if command == 'get':
        URL = project_host_url + "/get/"+str(key)
        response = requests.get(url=URL)
        data = response.json()
        result = data['result']
        if result=='':
            result = 'null'
        print("output : ", result)
    elif command == 'set':
        URL = project_host_url + "/set/"+str(key)+':'+ str(value[0])
        response = requests.get(url=URL)
        data = response.json()
        print("output : ",data['message'])
    elif command == 'reset':
        pw = key
        URL = project_host_url + "/reset/"+str(pw)
        response = requests.get(url=URL)
        data = response.json()
        result = data['message']
        print("output : ",result)

if __name__ == "__main__":
    main()
