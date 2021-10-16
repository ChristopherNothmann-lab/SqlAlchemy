FROM mysql:latest
LABEL name="MySQL"
LABEL authors="christopher.nothmann@gmail.com"
LABEL version="1.0"


RUN apt-get -q update && apt-get upgrade -y && apt-get -y -q install sudo vim

EXPOSE 3306 
ENV MYSQL_ROOT_PASSWORD=admin

COPY . .

RUN bash -c "chmod +x /execute-sql.sh"

CMD ["mysqld", "--user=mysql"]   