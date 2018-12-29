sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web/ask
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 -D
