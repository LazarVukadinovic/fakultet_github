import subprocess

result = subprocess.run(['dir'], shell=True, text=True, capture_output=True)
print(result.stdout)