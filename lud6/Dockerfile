FROM oraclelinux:8.10

RUN yum update -y && \
    dnf install nano && \
    dnf module enable -y python38 && \
    dnf install -y python38 python38-pip && \
    python3.8 -m ensurepip && \
    python3.8 -m pip install --upgrade pip setuptools

COPY pip.conf /root/.pip/pip.conf

RUN python3.8 -m pip install jupyterlab ipykernel && \
    python3.8 -m ipykernel install --user --name=python3 --display-name "Python 3.8 (lud)"

COPY jupyter_notebook_config.py /root/.jupyter/

CMD ["tail", "-f", "/dev/null"]
