sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
cd /home/box/web/ask/
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application

