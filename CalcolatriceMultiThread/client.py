#Client TCP multithread che invia NUM_WORKERS richieste contemporanee al server
# Ogni richiesta contiene un'operazione aritmetica da eseguire

import socket         # Per la comunicazione di rete
import json           # Per la codifica/decodifica JSON
import random         # Per generare numeri casuali
import time           # Per misurare i tempi di esecuzione
import threading      # Per gestire l'esecuzione parallela (multithreading)

# --- Configurazione ---
HOST = "127.0.0.1"           # IP del server
PORT = 22224                # Porta del server (assicurarsi che il server stia ascoltando su questa)
NUM_WORKERS = 15            # Numero di richieste (thread) da inviare in parallelo
OPERAZIONI = ["+", "-", "*", "/", "%"]  # Lista delle operazioni consentite

#1 Aggiungi commento
def genera_richieste(address, port):
    #2 Aggiungi commento
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))  # Connessione al server

        #3 Aggiungi commento
        primoNumero = random.randint(0, 100)
        operazione = OPERAZIONI[random.randint(0, 3)]  # Scegli operazione a caso (tra le prime 4)
        secondoNumero = random.randint(0, 100)

        #4 Aggiungi commento
        messaggio = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }
        messaggio = json.dumps(messaggio)

        ##5 Aggiungi commento
        sock_service.sendall(messaggio.encode("UTF-8"))

        #6 Aggiungi commento
        start_time_thread = time.time()

        #7 Aggiungi commento
        data = sock_service.recv(1024)

    #8 Aggiungi commento
    end_time_thread = time.time()
    print("Received: ", data.decode())
    print(f"{threading.current_thread().name} exec time = ", end_time_thread - start_time_thread)

# --- Punto di ingresso del programma ---
if __name__ == "__main__":
    start_time = time.time()  # Tempo di inizio totale

    #9 Aggiungi commento
    threads = [
        threading.Thread(target=genera_richieste, args=(HOST, PORT))
        for _ in range(NUM_WORKERS)
    ]

    #10 Aggiungi commento
    [thread.start() for thread in threads]

    #11 Aggiungi commento
    [thread.join() for thread in threads]

    end_time = time.time()  # Tempo di fine totale

    # Stampa il tempo complessivo impiegato per eseguire tutte le richieste
    print("Tempo totale impiegato = ", end_time - start_time)