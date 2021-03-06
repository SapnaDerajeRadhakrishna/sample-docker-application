FROM centos

MAINTAINER Sapna Radhakrishna "sapna.dr@gmail.com"

RUN yum update -y \
	 && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
	 && yum install -y python36u python36u-libs python36u-devel python36u-pip

# pipenv installation
RUN pip3.6 install pipenv
RUN ln -s /usr/bin/pip3.6 /bin/pip
RUN rm /usr/bin/python
# python must be pointing to python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python

COPY ./flask-service/requirements.txt /requirements.txt

WORKDIR /

RUN pip3.6 install -r requirements.txt

COPY . /

EXPOSE 5000

ENTRYPOINT [ "python3.6" ]

CMD ["flask-service/service_uwsgi.py"]
