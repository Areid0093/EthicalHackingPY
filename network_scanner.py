import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered_list.summary())
    # print(arp_request_broadcast.show())
    # scapy.ls(scapy.Ether())


scan('10.0.2.1/24')
