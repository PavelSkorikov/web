sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web/ask/
#sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
sudo python /home/box/web/ask/manage.py runserver 0.0.0.0:8000
sudo /etc/init.d/mysql start

