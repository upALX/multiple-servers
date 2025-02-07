import os
import sys
import subprocess
from pathlib import Path
from traitlets.config import get_config


if len(sys.argv) < 2:
    print("Erro: O diretório do projeto não foi passado.")
    sys.exit(1)

project_path = Path(sys.argv[1])

def find_venv(project_dir):
    venv_candidates = list(project_dir.glob("*/bin/python"))  # Linux/macOS
    if not venv_candidates:
        venv_candidates = list(project_dir.glob("*/Scripts/python.exe"))  # Windows
    return str(venv_candidates[0]) if venv_candidates else None

venv_python = find_venv(project_path)

if venv_python:
    subprocess.run([venv_python, "-m", "ipykernel", "install", "--user", "--name=python-venv", "--display-name", "Python (venv)"], check=True)
    os.environ["JUPYTER_PYTHON"] = venv_python
    print(f"🔹 Usando ambiente virtual: {venv_python}")
else:
    print("⚠️ Nenhuma venv encontrada, usando kernel global.")

c = get_config()

if venv_python:
    c.NotebookApp.kernel_spec_manager_class = "jupyter_client.kernelspec.KernelSpecManager"
    c.KernelSpecManager.ensure_native_kernel = False
    c.KernelSpecManager.whitelist = ["python3"]
    c.KernelSpecManager.default_kernel_name = "python-venv"
    sys.executable = venv_python
else:
    c.NotebookApp.kernel_spec_manager_class = "jupyter_client.kernelspec.KernelSpecManager"
    c.KernelSpecManager.ensure_native_kernel = True
    c.KernelSpecManager.whitelist = ["python3"]
    c.KernelSpecManager.default_kernel_name = "python3"

notebook_dir = os.getcwd()  # O diretório onde o Jupyter será iniciado
c.NotebookApp.notebook_dir = notebook_dir
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.allow_root = True
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
