# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...

from __future__ import annotations

from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import ClienteRecord

p1 = Prodotto("Ebook Reader", 120, 1, "AAA")
p2 = crea_prodotto_standard("Tablet", 750)

print ("======================================")

print(p1)
print(p2)

print ("=======================================")




cliente1 = ClienteRecord("Mario Rossi", "mariorossi@polito.it", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mause",20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1, 0.1)


print(ordine)
print("numero di righe dell'ordine: ", ordine.numero_righe())
print("totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))
print("")
print(ordine_scontato)
print("totale netto sconto: ", ordine_scontato.totale_netto())
print("totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))
print("-------------------------------")



#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

#Si modifichi la classe cliente in maniera tale che la proprietà categoria sia "protetta"
# e accetti solo ("Gold", "Silver", "Bronze")

