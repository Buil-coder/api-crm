# CRM API

## SETTING UP
```
virtualenv env
pip install -r requirements.txt
```

## TENANT MIGRATIONS
```
python manage.py makemigrations {app1} {app2} {app3}
python manage.py migrate --database {tenant}
```

## REMOVE MIGRATIONS
```
python manage.py makemigrations app --empty
python manage.py migrate --fake-initial
```

### FIX REDIS ISSUES
```
nano /etc/systemd/system/redis.service

[Service]
ExecStop=/bin/kill -s TERM $MAINPID
ExecStartPost=/bin/sh -c "echo $MAINPID > /var/run/redis/redis.pid"

sudo systemctl daemon-reload
sudo systemctl enable redis-server
sudo systemctl restart redis.service
```