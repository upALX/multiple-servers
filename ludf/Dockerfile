FROM oraclelinux:8.10

WORKDIR /app

RUN yum update -y

RUN yum install -y python3.8 python3-pip && \
    mkdir -p /root/.pip

COPY pip.conf /root/.pip/pip.conf

CMD ["tail", "-f", "/dev/null"]
