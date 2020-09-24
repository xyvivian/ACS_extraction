#!/bin/bash

csvsql --dialect mysql --snifflimit 100000  --db-schema zipcode --tables zipcode_acs_table  ACS_data.csv > create_table.sql
