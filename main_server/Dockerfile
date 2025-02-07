FROM oraclelinux:8.10

WORKDIR /app

RUN yum update -y

RUN yum update -y && yum install -y python3 python3-pip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install "pypiserver<2.0"

RUN yum install nano groupinstall "Development Tools"  

RUN gcc zlib-devel bzip2-devel readline-devel sqlite-devel \
openssl-devel tk-devel libffi-devel xz-devel git

RUN curl https://pyenv.run | bash && \
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-c", "source ~/.bashrc && pypi-server -p 8080 /app/pip_index/packages"]
