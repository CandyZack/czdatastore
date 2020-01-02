Author: Deep Baldha

## File Structure

"source_code.py" :  is the source code of the Flask app. 
		    It handles API calls and saving data of Python Dictionary in Persistence File.
		    
"cli.py"         :  is the python source code for CLI.

## Deployment

Flask App is deployed on Heroku.
URL is https://czdatastore.herokuapp.com
APIs example are as fellow:

For Set: https://czdatastore.herokuapp.com/set/<key>:<value> <br>
For Get: https://czdatastore.herokuapp.com/get/<key> <br>
For Reset: https://czdatastore.herokuapp.com/reset/<password>

Examples for API:

1) https://czdatastore.herokuapp.com/set/foo:104
2) https://czdatastore.herokuapp.com/get/foo
3) https://czdatastore.herokuapp.com/reset/iron

Above API calls returns JSON datafiles.
Password for reset is "iron".

## How to Use CLI.py

In terminal/cmd:

```bash
1) python cli.py set <KEY> <VALUE>
	
	example: python cli.py set foo 104

	This command is used to store value VALUE under key KEY in datastore
	Also gives confirmation on successful storage
```
```bash	
2) python cli.py get <KEY>

	example: python cli.py get foo

	This command is used to get value of key KEY from the datastore
	Return "null" is not value
```
```bash	
3) python cli.py reset <PassWord>

	example: python cli.py reset iron
	
	This command is used to reset the database and delete all the key:value pairs from datastore
```
