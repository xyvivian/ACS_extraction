SET ROLE xding2;

CREATE SCHEMA IF NOT EXISTS xueying_ding_acs;

DROP TABLE IF EXISTS xueying_ding_acs.acs_result_table;

\i create_table.sql

\COPY xueying_ding_acs.acs_result_table from 'result.csv' WITH CSV HEADER;
