FROM python:3.8-slim-buster

WORKDIR /sql_achemy 
# ENV FLASK_APP=sql_achemy/alchemy.py
# ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get -qq update -y && \
    apt-get -qq install -y default-mysql-client

COPY requirements.txt requirements.txt

RUN pip -q install --require-hashes -r requirements.txt

# EXPOSE 5000
COPY . .
# ENTRYPOINT [ "python3" ]
CMD ["/bin/bash"]  