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



if(all([interface for i in xx])):
    print("[+] this is your interface : {}".format(interface))
else:
    print("[-] wrong interface or you miss typing the interface ! check please :)")
