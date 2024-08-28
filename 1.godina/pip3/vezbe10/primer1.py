import subprocess

result = subprocess.run(['python', 'primer1-sub.py'], capture_output=True, text=True)
print(result.stdout)