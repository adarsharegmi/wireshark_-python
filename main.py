import pandas as pd
import pyshark
# capture = pyshark.RemoteCapture(remote_host='192.168.1.65', remote_interface='Wi-Fi')
# \Device\NPF_{34FF6F81-D543-4DD1-86B8-7F59BCF8569A}
capture = pyshark.LiveCapture(interface=r'Wi-Fi',output_file="a.csv")
capture.sniff(timeout=50)
print(capture)

# for packet in capture.sniff_continuously(packet_count=5):
#     print ('Just arrived:', packet)
#     breakpoint()
   
# f = open ("layers.txt", "w")
# if len(capture) > 0:
#     for packet in capture:
#         val = packet.__dict__
#         f.writelines(str(val))
#         break
    
    
    
