FROM ubuntu:latest

RUN apt update && apt upgrade -y && apt install -y mysql-server vim 

ENV MYSQL_ROOT_PASSWORD Passwd@123

EXPOSE 3306

CMD ["mysqld"]