mysql -uroot -e "CREATE DATABASE qabase"
mysql -uroot -e "CREATE USER 'pavel'@'localhost' IDENTIFIED BY '123456'"
mysql -uroot -e "GRANT ALL ON qabase.* TO 'pavel'@'localhost'"
manage.py syncdb