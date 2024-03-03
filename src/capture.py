from scapy.all import *
from scapy.layers.http import *
from scapy.sessions import TCPSessions
from scapy.sendrecv import sniff
import requests
import json

http_request_list = list()

# function to process captured packets
def packet_handler(pkt):
  if VXLAN in pkt and HTTP in pkt:
    if HTTPRequest in pkt and pkt[HTTPRequest.].Method == b'GET':
