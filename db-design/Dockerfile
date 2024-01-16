FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteract

################################################################################

ENV PROJECT_NAME=db-design

################################################################################

USER root
RUN apt -y update
RUN apt -y upgrade

RUN apt -y install locales-all
#RUN sed -i -E 's/# (ja\_JP.UTF-8)/\\1/' /etc/locale.gen && locale-gen  
#RUN locale-gen ja_JP.UTF-8
#RUN echo "export LANG=ja_JP.UTF-8" >> /root/.bashrc
#RUN ["/bin/bash", "-c", "source /root/.bashrc"]
ENV LANG ja\_JP.UTF-8

RUN apt -y install vim

RUN apt -y install python3
RUN apt -y install python3-pip
RUN apt -y install libpq-dev
RUN apt -y install postgresql-14
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN pip3 install flask
RUN pip3 install flask-sqlalchemy
RUN pip3 install flask-wtf
RUN pip3 install psycopg2-binary
RUN pip3 install flask-bootstrap
RUN pip3 install pandas

RUN echo "alias python='python3'" >> /root/.bashrc
RUN echo "alias pip='pip3'" >> /root/.bashrc
RUN ["/bin/bash", "-c", "source /root/.bashrc"]

ADD deploy/flaskdb.tar.gz /

USER postgres
RUN cp /etc/postgresql/14/main/postgresql.conf /etc/postgresql/14/main/postgresql.conf.default
RUN sed -i -e "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/14/main/postgresql.conf
RUN sed -i -e "s/^#password_encryption = scram-sha-256/password_encryption = md5/g" /etc/postgresql/14/main/postgresql.conf
RUN cp /etc/postgresql/14/main/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf.default
RUN sed -i -e "s/^host    all             all             127.0.0.1\/32            scram-sha-256/host    all             all            0.0.0.0\/0                md5/g" /etc/postgresql/14/main/pg_hba.conf
RUN /etc/init.d/postgresql start && wait && /usr/bin/createdb -O postgres ${PROJECT_NAME} && wait && psql ${PROJECT_NAME} < /flaskdb/createdb.ddl

USER root
EXPOSE 5432
EXPOSE 8080
VOLUME  ["/flaskdb", "/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

ENV FLASK_APP /flaskdb/app.py
CMD /etc/init.d/postgresql restart && wait && /usr/local/bin/flask run -h 0.0.0.0 -p 8080 --debug --reload --debugger
