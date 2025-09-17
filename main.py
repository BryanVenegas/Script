import os
import subprocess
import time
import webbrowser
import requests
import winreg
git_dir = r"C:\Users\veneg\Downloads\Programacion"
repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name))and 
         os.path.exists(os.path.join(git_dir, name, ".git"))]
selected_repo = None
if repos:
    print("Repositorios encontrados:")
    for idx, repo in enumerate(repos,1):
        print(f"{idx}. {repo}")
        
else:
    print("No se encontraron repositorios Git en el directorio especificado.")