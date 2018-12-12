#!/user/bin/env python

import subprocess
import optparse
import re
# command = "ifconfig -a | sed \'s/[ \t].*//;/^$/d\'"  # the shell command
# process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
#
#
# output = process.communicate()
# interfaces = output[0].decode('ascii')
# xx= interfaces.split(':\n')
# #print(xx[:-1])
# print("[+] interfaces on your device :\n")
# for i  in range(len(xx[:-1])):
#     print('{} : {}'.format(i, xx[i]))




def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="changing the mac for this interface")
	parser.add_option("-m", "--mac", dest="new_mac", help="the mac address")
	(options, arguments) = parser.parse_args()

	if not options.interface :
		print("[-] Please specify an interface , use --help for more Info")
	elif not options.new_mac:
		print("[-] Please specify a mac address , use --help for more Info")

	return options



def change_mac(interface, new_mac):
		 print("[+] changing the mac address for {} to {}".format(interface,new_mac))
		 subprocess.call(["ifconfig", interface, "down"])
		 subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
		 subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	res = re.search(b'\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}', ifconfig_result)
	if res:
		return res.group(0).decode('ascii')
	else:
		print("[-] Could not read the MAC arddess!")


options= get_arguments()
mac = get_current_mac(options.interface)
print("current MAC  : {}".format( str(mac)))
#change_mac(options.interface,options.new_mac)
mac = get_current_mac(options.interface)
if mac == options.new_mac:
	print("[+] MAC address was sucsessfully changed to : {}".format(mac))
else:
	print("[-] Mac address did not be changed!")









# if interface in xx :
#     print("[+] changing mac address for {}".format(interface))
#     # subprocess.call("ifconfig {} down ".format(interface), shell=True)
#     # subprocess.call("ifconfig {} hw ether  {}".format(interface,new_mac), shell=True)
#     # subprocess.call("ifconfig {} up ".format(interface), shell=True)
#

# else:
#     print("[-] wrong interface or you miss typing the interface ! check please :)")





