-- lists privileges for select users
SELECT * FROM information_schema.table_privileges WHERE privilege_type = 'SELECT';