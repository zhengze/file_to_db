# file_to_db
load data from csv/xlsx  into database

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
