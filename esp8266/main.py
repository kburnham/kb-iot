import network                                                                                                                                         
import socket
import dht
import machine






                                                                                                                                                      
def log(msg):                                                                                                                                         
    print(msg)                                                                                                                                        
                                                                                                                                                      
def read_dht22():
    d = dht.DHT22(machine.Pin(14))
    d.measure()
    return((d.temperature(), d.humidity()))



def make_html():
    html = """<!DOCTYPE html><html><head><title>ESP8266</title></head><body><h1>kb-iot ESP8266 with attached DHT22 temp/humid sensor</h1><p>temp %f</p><p>humidity: %f</p></body></html>""" % (read_dht22())
    return(html)





def start_myserver():
    print('server started')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print('starting while loop . . .')
    while True:
      try:
        if gc.mem_free() < 102000:
          gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)
        response = make_html()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
      except OSError as e:
        conn.close()
        print('Connection closed')



                                                                                                                                                      
                                                                                                                            
#main part                                                                                                                                            
                                                                                                                                                  
                                                                                                                                                      
do_connect()                                                                                                                                          
start_myserver()  




