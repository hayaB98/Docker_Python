FROM mysql:latest

COPY code/initdb.sql /docker-entrypoint-initdb.d/initdb.sql
RUN chmod +x /docker-entrypoint-initdb.d/initdb.sql





