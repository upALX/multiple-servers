FROM oraclelinux:8.10

WORKDIR /app

RUN yum update -y

RUN yum update -y && yum install -y python3 python3-pip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install "pypiserver<2.0"

EXPOSE 8080

CMD ["pypi-server", "-p", "8080", "/app/pip_index/packages"]
