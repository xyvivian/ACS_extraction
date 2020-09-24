#!/bin/bash

csvsql --dialect mysql --snifflimit 100000  --db-schema xueying_ding_acs --tables xueying_ding_acs.acs_result_table  result.csv > create_table.sql
