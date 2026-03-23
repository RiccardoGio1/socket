import socket;
import json;

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005    # Porta su cui il server rimarrà in ascolto
BUFFER_SIZE = 1024  # Dimensione massima (in byte) dei pacchetti ricevibili

#Creazione del socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Associa il socket all'indirizzo IP e alla porta specificati
sock.bind((SERVER_IP,SERVER_PORT)) 

print("Pronto a ricevere i dati...")

while True:
    #Ricevo i dati
    # sock.recvfrom blocca l'esecuzione finché non arriva un pacchetto
    # Restituisce i dati ricevuti e l'indirizzo (IP, porta) del mittente
    data, addr = sock.recvfrom (1024)
    if not data:
        break
    
    data = data.decode()  # Decodifica i byte ricevuti in una stringa
    data = json.loads(data)  #prende il file formato JSON e lo trasforma in dizionario
    
    # Estrae i valori inviati dal client tramite le chiavi del dizionario
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]
    
    #eval prende il valore dell'operazione (+,-,/,*)
    #e fa l'operazione sui numeri trasformati in stringhe*/
    risultato=eval(str(primoNumero)+(operazione)+str(secondoNumero))  
    
    # Invia il risultato al mittente
    # Il risultato deve essere convertito in stringa e poi in byte (.encode)
    sock.sendto(str(risultato).encode("UTF-8"), addr)
    print(risultato)