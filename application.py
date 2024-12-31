import os
import subprocess
import sys
import platform

os.makedirs('cards', exist_ok=True)

venv_dir = '.venv'
install = ' install -r requirements.txt'

if not os.path.exists(venv_dir):
    print("No virtual environment found.")
    sys.exit(1)
elif not os.path.exists(os.path.join(venv_dir, 'Lib', 'site-packages', 'PIL')):
    print("Requirements not installed.")
    sys.exit(2)


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
