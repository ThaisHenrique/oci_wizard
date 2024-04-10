create or replace PROCEDURE drop_di_tables AS
BEGIN
-- Drop all the tables with 'COPY$' in the name
  FOR cur_rec IN (SELECT table_name
                  FROM user_tables
                  WHERE table_name LIKE 'COPY$%') LOOP
    EXECUTE IMMEDIATE 'DROP TABLE ' || cur_rec.table_name;
    DBMS_OUTPUT.PUT_LINE('table ' || cur_rec.table_name || ' successfully dropped.');
  END LOOP;
END drop_di_tables;
