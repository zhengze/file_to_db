# file_to_db
load data from csv/xlsx  into database(mysql/postgresql)

## INSTALL
- pipenv install  
or  
- pip install -r requirements.txt

## CONFIG
- $sudo touch .env 
```
DATABASE_URI=postgresql+psycopg2://admin:1234@localhost/test
```

## USAGE
- python file_to_db.py -h 
```
usage: file_to_db.py [-h] [--file FILE] [--table TABLE]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  the file path.
  --table TABLE, -t TABLE
                        the table name.

```
