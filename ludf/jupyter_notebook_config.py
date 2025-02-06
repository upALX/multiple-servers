import os
import sys
import glob
from pathlib import Path

def find_venv():
    """ Procura um ambiente virtual dentro do diretório do projeto """
    project_path = Path.cwd()
    venv_candidates = list(project_path.glob("*/bin/python"))  # Linux/macOS
    if not venv_candidates:
        venv_candidates = list(project_path.glob("*/Scripts/python.exe"))  # Windows
    return str(venv_candidates[0]) if venv_candidates else None

# Descobrir e configurar automaticamente o kernel
venv_python = find_venv()
if venv_python:
    os.environ["JUPYTER_PYTHON"] = venv_python
    c.NotebookApp.kernel_spec_manager_class = "jupyter_client.kernelspec.KernelSpecManager"
    c.KernelSpecManager.ensure_native_kernel = False
    c.KernelSpecManager.whitelist = ["python3"]
    c.KernelSpecManager.default_kernel_name = "python3"

    # Sobrescrever sys.executable para garantir que Jupyter use o Python correto
    sys.executable = venv_python
