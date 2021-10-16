
# RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods

# apt-get install default-mysql-client

ALTER USER 'root'@'*' IDENTIFIED WITH mysql_native_password BY 'admin';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'admin';


click==8.0.3
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
greenlet==1.1.2
itsdangerous==2.0.1
Jinja2==3.0.2
MarkupSafe==2.0.1
PyMySQL==1.0.2
SQLAlchemy==1.4.25
Werkzeug==2.0.2

 docker exec -it ctn-mysql-db /bin/bash


mysql -h ctn-mysql-db -uroot -padmin
