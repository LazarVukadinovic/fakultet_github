import subprocess

sub = subprocess.Popen(['python', '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, error = sub.communicate()
print(output)