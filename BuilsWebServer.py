#Web server 
#UDP
print ("####  ####  ####  ##  ##  ####  ####")
print ("#     #     #  #   # #    #     #  #")
print ("####  ##    ####   # #    ##    ####")
print ("   #  #     #   #   #     #     #   #")
print ("####  ####  #    #  #     ####  #    #")
print ("##  ##  ##  ####  ####")
print (" # #  # #   #     #  #")
print (" # #  # #   ##    ####")
print ("  #    #    #     #  #")
print ("  #    #    ####  ####")
import socket
s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5588))
res_data,address = s.recvfrom(1024)
data = res_data.decode("UTF-8")
sen_data = "welcom to my WEB SERVER"
Sdata = sen_data.encode("UTF-8")
send.to(sdata,address)
