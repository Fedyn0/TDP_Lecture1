# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...

from __future__ import annotations

class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -- ovvero è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        return cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    @property
    def price(self): # eq. getter
        return self._price
    @price.setter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo.")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price} €"

    def __repr__(self):
        return f"Prodotto(nome= {self.name}, price= {self.price}, quantity= {self.quantity}, supplier= {self.supplier})"

    def __lt__(self, other: Prodotto) -> bool:
        if not isinstance(other, Prodotto):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other: Prodotto) -> bool:
        if not isinstance(other, Prodotto):
            return NotImplemented
        return(self.name == other.name
               and self.price == other.price
               and self.quantity == other.quantity
               and self.supplier == other.supplier)

    def prezzo_finale(self):
        return self.price * (1 + self.aliquota_iva)


class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self):
        return self.valore_lordo() -self.valore_lordo()*self.sconto_percento/100

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria: float, ore: int):
        super().__init__(name = name, price = tariffa_oraria, quantity = 1, supplier = None)
        self.ore = ore

    def prezzo_finale(self):
        return self.price * self.ore


myproduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")

print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC") #Modo per chiamare un metodo di classe.
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}")#Modo per chiamare un metodo statico.

myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
Prodotto.aliquota_iva = 0.24
print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")


print(p3)

p_a=Prodotto("Laptop", 1200,12,"ABC")
p_b=Prodotto("Mause", 10,14,"CDE")

print("myproduct_1 == p_a?", myproduct1 == p_a)
print("p_a == p_b?", p_a == p_b)

mylist = [p_a, p_b, myproduct1]


my_product_scontato = ProdottoScontato("Auricolari",33,1,"ABC",10)
my_service = Servizio("Consulenza", 100, 3)

mylist.append(my_product_scontato)
mylist.append(my_service)
mylist.sort(reverse=True)

for elem in mylist:
    print(elem.name," --> ",elem.prezzo_finale())

print("---------------------------------------")


class Abbonamento:
    def __init__(self, name: str, prezzo_mensile: float, mesi:int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self):
        return self.prezzo_mensile * self.mesi

abb = Abbonamento("Software Gestionale", 30.0, 24)
mylist.append(abb)
for element in mylist:
    print(element.name," --> ",element.prezzo_finale())

def calcola_totale(elementi):
    tot = 0
    for e in elementi:
        tot += e.prezzo_finale()
    return tot

print(f"Il totale è: {calcola_totale(mylist)}")

from typing import Protocol

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self):
        ...

def calcola_totale(elementi: list[HaPrezzoFinale]):
    return sum(e.prezzo_finale() for e in elementi)

print(f"il totale è {calcola_totale(mylist)}")

print("-------------------------------")
print("")

print("sperimentiamo con dataclass")
from dataclasses import dataclass

@dataclass()
class ProdottoRecord:
    name: str
    prezzo_unitario : float

@dataclass()
class ClienteRecord:
    name: str
    email: str
    categoria: str

@dataclass()
class RigaOrdine:
    prodotto: ProdottoRecord
    quantita: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario * self.quantita

@dataclass()
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self,aliquota_iva):
        return self.totale_netto()*(1+aliquota_iva)

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine):
    sconto_percentuale: float

    def totale_scontato(self):
        self.totale_lordo()*(1- self.sconto_percentuale)

    def totale_netto(self):
        netto_base = super().totale_netto()
        return netto_base*(1-self.sconto_percentuale)

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

class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria

    def descrizione(self): #to_string
        # "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Bronze")
print(c1.descrizione())