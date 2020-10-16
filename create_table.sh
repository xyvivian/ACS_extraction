#!/bin/bash

csvsql --dialect mysql --snifflimit 100000  --db-schema xueying_ding_acs  --tables acs_result_table  ACS_data.csv > create_table.sql
