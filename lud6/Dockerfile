FROM oraclelinux:7.9

WORKDIR /app

RUN yum update -y

RUN yum install -y python3.6 python3-pip && \
    mkdir -p /root/.pip

COPY pip.conf /root/.pip/pip.conf

CMD ["tail", "-f", "/dev/null"]
