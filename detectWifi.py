>>> import subprocess
>>> devices = subprocess.check_output(['netsh','wlan','show','network'])
>>> devices = d.decode('ascii')
>>> print(devices)
