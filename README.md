# python-mysql


docker pull ubuntu/mysql

docker run -d --name test_db -e TZ=IST -p 30306:3306 -e MYSQL_ROOT_PASSWORD=Passwd@123 ubuntu/mysql:latest

docker logs -f test_db

docker exec -it test_db /bin/bash

sudo docker exec -it test_db mysql -uroot -p

docker exec -it test_db service mysql restart

sudo docker inspect test_db | grep -i port

sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' test_db


ALTER USER 'ken'@'localhost' IDENTIFIED BY 'NewPassword';
ALTER USER 'ken'@'%' IDENTIFIED BY 'Pass@12345';


CREATE USER 'ken'@'%' IDENTIFIED BY 'Ken@12345';
GRANT ALL PRIVILEGES ON *.* TO 'ken'@'%';
FLUSH PRIVILEGES;