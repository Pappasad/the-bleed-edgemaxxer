import os
import subprocess
import sys
import platform

os.makedirs('cards', exist_ok=True)

venv_dir = '.venv'
install = ' install -r requirements.txt'

if os.path.exists(os.path.join(venv_dir, 'Lib', 'site-packages', 'PIL')):
    pass
else:
    print("Installing requirements...")
    if platform.system() == "Windows":   
        req_inst = os.path.join(venv_dir, 'Scripts', 'pip.exe') + install
    else:
        req_inst = os.path.join(venv_dir, 'bin', 'pip') + install
    subprocess.check_call(req_inst.split())
    print("Requirements installed.")

if platform.system() == "Windows":
    env = os.path.abspath(os.path.join(venv_dir, 'Scripts', 'python.exe'))
else:
    env = os.path.abspath(os.path.join(venv_dir, 'bin', 'python'))

# Ensure the paths are correct
if not os.path.isfile(env):
    raise FileNotFoundError(f"Python executable not found: {env}")

cmd = os.path.abspath(os.path.join('code', 'app.py'))

# Ensure the paths are correct
if not os.path.isfile(env):
    raise FileNotFoundError(f"Python executable not found: {env}")

subprocess.check_call([env, cmd])
