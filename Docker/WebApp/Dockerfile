FROM python:3

RUN mkdir /project
WORKDIR /project

COPY Docker/WebApp/requirements.txt /project/
RUN pip3 install -r requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY Docker/setup.sh /setup.sh
RUN chmod +x /setup.sh
CMD ["/setup.sh"]

VOLUME ["/project"]
EXPOSE 5000
