# Faculty-Portal

## Installation
1. Install ``virtualenv`` and create a VM :
```
	virtualenv env -p python3
	source env/bin/activate
```

2. and then, install rest of the dependencies :
```
	pip install -r requirements.txt
```

3. Make sure you have imported all the databases specified in the settings.py
```
  mysql -u username -p database_name < file.sql
```
