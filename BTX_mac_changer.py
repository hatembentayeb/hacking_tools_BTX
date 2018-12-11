#!/user/bin/env python

import subprocess
command = "ifconfig -a | sed \'s/[ \t].*//;/^$/d\'"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)


output = process.communicate()
interfaces = output[0].decode('ascii')
xx= interfaces.split(':\n')
#print(xx[:-1])
print("[+] interfaces on your device :\n")
for i  in range(len(xx[:-1])):
    print('{} : {}'.format(i,xx[i]))

interface = input("[*] choose your your interface :")



if interface in xx :
    print("[+] changing mac address for {}".format(interface))
    # subprocess.call("ifconfig wlp9s0 down ", shell=True)
    # subprocess.call("ifconfig wlp9s0 hw ether 00:11:22:33:55 ", shell=True)
    # subprocess.call("ifconfig wlp9s0 up ", shell=True)
else:
    print("[-] wrong interface or you miss typing the interface ! check please :)")





