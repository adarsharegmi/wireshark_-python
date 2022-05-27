from ipaddress import ip_address
import pyshark
capture = pyshark.RemoteCapture(remote_host='192.168.1.65', remote_interface='Wi-Fi')
# \Device\NPF_{34FF6F81-D543-4DD1-86B8-7F59BCF8569A}
# capture = pyshark.LiveCapture(interface='Wi-Fi', )
capture.sniff(timeout=50)
print(capture)

for packet in capture.sniff_continuously(packet_count=5):
    print ('Just arrived:', packet)
    breakpoint()
    
    
    
