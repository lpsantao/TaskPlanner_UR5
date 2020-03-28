import subprocess
#subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "startvm", "ursim"])
subprocess.call(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "guestcontrol", "ursim", "run", "--exe","/home/ur/ursim-current/start-ursim.sh", "--username", "ur", "--password", "easybot", "--", "-l" ,"/usr"])
#subprocess.run(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "ursim", './test.sh']

