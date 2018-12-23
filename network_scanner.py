#!/user/bin/env python

import scapy.all as sc


def scan(ip):
	arp_req = sc.ARP(pdst=ip)
	broadcast = sc.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_req_broadcast = broadcast / arp_req
	answered_list = sc.srp(arp_req_broadcast, timeout=1, verbose=False)[0]


	client_list = list()
	for el in answered_list:
		client_dict = {'IP':el[1].pdst,'MAC':el[1].hwsrc}
		client_list.append(client_dict)

	return client_list



def print_result(client_list):
	print("+-------------------------------------------+")
	print("|\t\tIP\t\t\t|\t\tMAC Address\t\t|\n+-------------------------------------------+")
	for client in client_list:
		print("|{}\t\t|\t{}\t|".format(client["IP"], client["MAC"]))
		print("+-------------------------------------------+")



client_list = scan('192.168.0.1/24')
print_result(client_list)
