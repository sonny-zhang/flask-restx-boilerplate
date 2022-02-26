source /data/env/order_menu/bin/activate

# 启动
uwsgi --stop ../logs/app.pid
uwsgi --ini uwsgi.ini