import copy
from collections import Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mause", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700)]

print("="*60)
print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")
print("="*60)

carrello.append(ProdottoRecord("Monitor", 150.0))
carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)

print("="*60)
print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")
print("="*60)

print("="*60)
print("Prodotti nel carrello:")
tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 150.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#rimuovere
carrello.pop() #rimuove l'ultimo elemento
carrello.pop(2) #rimuove l'elemento in posizione 2
carrello.remove(p1) #elmino la prima occorrenza di p1
#carrello.clear() #svuoto la lista

#sorting
#carrello.sort() #ordina seguendo ordinamento naturale
#carrello.sort(reverse=True) #ordina al contrario
carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)
#carrello_ordinato = sorted(carrello)

#copie ed altro
carrello.reverse() #inverte l'ordine
carrello_copia = carrello.copy() #shallow copy
carrello_copia2 = copy.deepcopy(carrello) #deep copy, copio anche il contenuto


#TUPLE
sede_principale = (45,8) #lat e long della sede di Torino
sede_milano = (45,9) #lat e long della sede di Milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIva = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIva:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return(sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)
print(altri_campi)


#SET
categorie = {"Gold", "Silver", "Bronze"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
categorie_all = categorie.union(categorie2)  #È molto più tollerante. Accetta qualsiasi tipo di collezione
                                            #(liste, tuple, dizionari) come argomento. Python prenderà
                                            #quella lista, la trasformerà al volo in un set e farà l'unione.
#categorie_all = categorie | categorie2  #meno tollerante
print(categorie_all)

categorie_comuni = categorie & categorie2 #solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2
print(categorie_esclusive)

categorie_esclusive_simmetrico = categorie ^ categorie2 #differenza simmetrica
print(categorie_esclusive_simmetrico)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mause", 250.0),
                     ProdottoRecord("Tablet", 700.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                     ProdottoRecord("Mause2", 250.0),
                     ProdottoRecord("Tablet2", 700.0)}

#metodi utili per i set
s = set()

#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiungo un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0), ProdottoRecord("ccc", 20.0)]) #aggiungo piu elementi

print(s)

#togliere
s.remove(ProdottoRecord("aaa", 20.0)) #rimuove un elemento. Raise KeyError se non esiste.
s.discard(ProdottoRecord("aaa", 20.0)) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear() #svuota il set

#operazioni insiemistiche
s.union(prodotti_ordine_A) # s | prodotti_ordine_A, ovvero genera un set che unisce i due set di partenza
s.intersection(prodotti_ordine_A) #prende solo elementi comuni
s.difference(prodotti_ordine_A) #prende elementi di s che non sono contenuti in prodottti_ordine_A
s.symmetric_difference(prodotti_ordine_A)  # s ^s1, ovvero elementi di s non contenuti in prodottti_ordine_A
                                            # ed elementi di prodotti_ordine_A non contenuti in s

s.issubset(prodotti_ordine_A) # se gli elementi di s sono contenuti in prodotti_ordine_A
s.issuperset(prodotti_ordine_A) #se gli elementi di prodotti_ordine_A sono contenuti in s
s.isdisjoint(prodotti_ordine_A) #se glielementi di prodotti_ordine_A quelli di s sono diversi

#dictionary
catalogo = {
    "LAP001" : ProdottoRecord("Laptop", 1200.0),
    "LAP002" : ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001" : ProdottoRecord("Mause", 20.0),
    "AUR001" : ProdottoRecord("Auricolari", 250.0),
}

cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

#print(f"Cerco un altro oggetto: {catalogo["NonEsiste"]}")

prod1 = catalogo.get("NonEsiste")

if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0.0))
print(prod2)

keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a: {val}")

rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

#DA RICORDARE
d = {}
# d[key] = v #scrivo sul dizionario
# v = d[key] #leggere - restituisce key error se non esiste
# v = d.get(key) #legge senza rischiare keyerror. Se non esiste resituisce default
# d.pop(key) #restituisce un valore e lo cancella dal diz
# d.clear() #elimina tutto
# d.keys() #restituisce tutte le chiavi definite nel diz
# d.values()  #restituisce tutti i valori salvati nel diz
# d.items() #restituisce le coppie chiave valore
# key in d #condizione che verifica se key è presente nel diz

"""ESERCIZIO LIVE
Per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo""" #lista
"""2) Memorizzare i CF dei clienti (univoco)""" #set
"""3) Creare un database di prodotti che posso cercare con un codice univoco""" #diz
"""4) Memorizzare le coordinate gps della nuova sede di Roma""" #tuple
"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale""" #set


print("="*50)

#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("2 Categorie piu frequenti")
print(categorie_counter.most_common(2))

print("totale: ")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop" : 13 , "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop" : 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio + vendite_febbraio

#aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite Bimestre: {vendite_bimestre}")

#fare differenza
print(f"Differenza di vendite: {vendite_gennaio - vendite_febbraio}")

#modificarne i valori in the fly

vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennio: {vendite_gennaio}")

# #metodi da ricordare
# c.most_common(n) #restituisce gli n elementi più frequenti
# c.total() #somma dei conteggi

