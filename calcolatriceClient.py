import socket;
import json;

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#Creazione del socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

primoNumero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (simbolo)")
secondoNumero = float(input("Inserisci il secondo numero: "))
messaggio = {"primoNumero": primoNumero,
    "operazione": operazione,
    "secondoNumero": secondoNumero}

#Trasforma il dizionario in una stringa JSON
messaggio = json.dumps(messaggio)

#Invio del messaggio .encode("UTF-8") trasforma la stringa in byte
sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

# Il client si mette in attesa (bloccante) finché il server non risponde
data, addr = sock.recvfrom (1024)

# Decodifica dei byte ricevuti e stampa del risultato finale
print(data.decode())

# Chiusura del socket per liberare le risorse del sistema
sock.close()