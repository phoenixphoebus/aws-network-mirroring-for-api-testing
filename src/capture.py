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
      print('Processing HTTP Request packet')
      http_request_list.append(pkt)
      print('Cached HTTP Request packet. Cache size:'+str(len(http_request_list)))
    elif HTTPResponse in pkt:
      print('Processing HTTP Response packet')
      for p in list(http_request_list):
        if pkt.payload.payload.payload.payload.answers(p.payload.payload.payload.payload) == True:
          response_comparer(p[HTTPRequest.Path.decode("utf-8"), pkt.load)
          http_request_list.remove(p)
          print('HTTP Response packet matched with Request. Request packed removed from cache. Cache size:'+str(len(http_request_list)))

def response_comparer(path: string, response: string):
  dict1 = json.loads(response)
  new_api_response = requests.get('http://localhost'+path)
  dict2 = json.loads(new_api_response)
  if dict1 == dict2:
    print('Responses are equal')
  else:
    print('Responses are not equal')

sniff(iface="enX0", filter="udp port 4789", prn=packet_handler)
