import pandas as pd
import pyshark
import csv
# capture = pyshark.RemoteCapture(remote_host='192.168.1.65', remote_interface='Wi-Fi')
# \Device\NPF_{34FF6F81-D543-4DD1-86B8-7F59BCF8569A}
capture = pyshark.LiveCapture(interface=r'Wi-Fi')
capture.sniff(packet_count=2)
listsd = []
for packet in capture.sniff_continuously(packet_count=5):
    print ('Just arrived:', packet)
    di = {}
    captured_length = packet.captured_length
    attributes= [f for  f  in dir(packet) if '__'  not in f]
    for i in attributes:
        var = getattr(packet,i)
        if isinstance(var, str):
            di.update({i: var})
        else:
            attributes= [f for  f  in dir(var) if '__'  not in f]
            for i in attributes:
                var2 = getattr(var,i)
                if isinstance(var2, str):
                    di.update({i: var2})
        listsd.append(di)
        

d = pd.DataFrame(listsd)
d.to_csv("d.csv")          
# import csv


# with open('test.csv', 'w') as f:
#     for packet in capture:
#         val = packet.__dict__
#         keys = val.keys()
#         for key in val.keys():
#             f.write("%s,%s\n"%(key,val[key]))
    
# # writing the raw dataset list of dictionaries
# with open("test.csv", "w") as file:
#     val = capture[0].__dict__
#     keys = val.keys()
#     csvwriter = csv.DictWriter(file, keys)
#     csvwriter.writeheader()
#     csvwriter.writerows(capture)