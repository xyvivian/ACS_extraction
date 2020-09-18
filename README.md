# ACS_extraction
This github repo extracts the acs data into .csv file and convert it into sql.

## Set Up
To set up the required evnironment: 
'''
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
'''

Additionally, need to specify the hose names, user names, passwords, and repo names by:
'''
export PGHOST= pghost
export PGUSER = pguser
export PGPASSWORD = pgpssword
export PGDATABASE = pg database
'''

## ACE Database Loading
To get a ACS database csv file:
'''
download_data_to_csv.py
'''

The result file will be stored in a csv file callsed result.csv

## Set Up Data Table
Run the following command to set up a table:
'''
sh transform_csv_to_sql.sh
'''

For our default databse result.csv, we have already provided the create_table.sql.
However,if we use any other csv file and we want to load it into a table, we can change the csv name in the transform_csv_to_sql.sh.

The following code provides a quick generaton of sql table header(create_table.sql):
'''
sh create_table.sh
'''

### Copy CSV to Sql
To convert csv to sql file, run the following code:
'''
sh load_data.sh
'''
