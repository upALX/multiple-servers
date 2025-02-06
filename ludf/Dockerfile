FROM oraclelinux:8.10

# Atualiza pacotes e instala Python 3.8 + pip
RUN yum update -y && \
    dnf module enable -y python38 && \
    dnf install -y python38 python38-pip && \
    python3.8 -m ensurepip && \
    python3.8 -m pip install --upgrade pip setuptools

# Configuração do pip
COPY pip.conf /root/.pip/pip.conf

# Instala Jupyter e o kernel diretamente no sistema
RUN python3.8 -m pip install jupyterlab ipykernel && \
    python3.8 -m ipykernel install --user --name=python3 --display-name "Python 3.8 (lud)"

# Copia a configuração do Jupyter
COPY jupyter_notebook_config.py /root/.jupyter/

# Mantém o container rodando
CMD ["tail", "-f", "/dev/null"]
