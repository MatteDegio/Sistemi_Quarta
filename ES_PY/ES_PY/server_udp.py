import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.119", 5000))

while True:
    stringa = input("inserisci una stringa: ")
    s.sendto(stringa.encode(), ("192.168.0.124", 5000))
    dati, ind_client = s.recvfrom(4096)
    print(f"{dati.decode()} ricevuti da {ind_client}")
