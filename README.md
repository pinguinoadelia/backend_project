# My Personal Shop
Un Progetto Django per PPM - UniFi  
Sito E-Commerce

### Non registrato - homepage
Quando apri il sito per la prima volta, è già possibile visualizzare tutti gli articoli. Da qui puoi:

- filtrare gli articoli per categoria e eventualmente rimuovere i filtri
- cercare gli articoli per nome (non è necessaria la corrispondenza completa)  
  [per uscire dalla ricerca, premi il titolo in alto a sinistra]
- combinare le due opzioni precedenti
- da qualsiasi di queste visualizzazioni è possibile aggiungere articoli al carrello
- controllare il numero aggiornato di articoli nel carrello
- effettuare il login (vedi sotto)
- aggiungere un articolo da vendere

### Registrato - homepage
Una volta effettuato il login, puoi:

### Vista carrello
Puoi accedere a questa vista cliccando l’icona del carrello in alto a destra. Da qui puoi:

- vedere gli articoli presenti nel tuo carrello
- modificare la quantità degli articoli selezionati (se porti a zero, verranno rimossi)
- vedere il totale degli articoli, il subtotale e il prezzo totale
- tornare alla homepage
- procedere al checkout se hai almeno un articolo nel carrello

### Vista checkout
Una volta che hai articoli nel carrello, dalla vista checkout puoi:

- tornare al carrello, oppure alla homepage premendo il titolo in alto a sinistra
- inserire il tuo nome e email (solo se non sei loggato)
- fornire il tuo indirizzo per la spedizione
- procedere al pagamento
- cliccando su “Effettua pagamento” verrai reindirizzato alla homepage, il tuo ordine sarà salvato e il carrello svuotato

### Sezione Reparti

Oltre tutto ciò utilizzando il percorso "http://127.0.0.1:8000/uffici/reparti/" sarà possibile accedere ad un'ulteriore pagina di gestione con tre reparti (elettronica, bellezza, libri) ognuno dei quali 
viene gestista da uno o più Manager.

###App Uffici
Oltre all'app di Ecommerce è stata implementata anche un app di gestione degli uffici dove sono presenti due gruppi ovvero "L'Office Manager" dove ci sono tutti gli utenti incaricati di gestire un
reparto specifico e "L'Office Chiefs" Sono utenti “senior” o capi-ufficio con più poteri, di solito superiori ai Manager.
