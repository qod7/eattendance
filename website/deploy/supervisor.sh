sudo cp supervisor.conf /etc/supervisor/conf.d/passion.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart passion
