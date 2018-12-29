sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE qabase"
mysql -u root -e "CREATE USER 'pavel'@'localhost' IDENTIFIED BY '123456'"
mysql -u root -e "GRANT ALL ON qabase.* TO 'pavel'@'localhost'"
python3 manage.py makemigrations
python3 manage.py migrate