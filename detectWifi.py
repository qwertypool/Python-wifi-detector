>>> import subprocess   
>>> devices = subprocess.check_output(['netsh','wlan','show','network'])
>>> devices = d.decode('ascii')
>>> print(devices)

Note:  subprocess allows to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. dont need pip to install it as the subprocess module comes preinstalled.
