#!/bin/bash

head -n 1000 result.csv | tr [:upper:] [:lower:] | tr ' ' '_' | sed 's/#/num/' | csvsql -i postgresql --db-schema xueying_ding_acs --tables acs_result_table | tee create_table.sql