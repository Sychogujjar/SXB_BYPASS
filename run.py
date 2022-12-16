import os, platform
 
try:
 
    import requests
 
except:
	
    os.system("xdg-open https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA")
 
    os.system('pip install requests')
 
import requests
 
bit = platform.architecture()[0]
 
if bit == '64bit':
 
    from Premium64 import approval
 
    approval()
 
elif bit == '32bit':
 
    from Premium32 import approval
 
    approval()
