"""
Scrivere un software gestionale che abbia le seguenti funzionalià:
1) Supportare l'arrivo e la gestione di ordini
1bis) Quando arriva un nuovo ordine lo aggiungo ad una coda, assicurandomi che sia eseguito solo dopo gli altri
2) Avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente
"""
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)


    def add_ordine(self, ordine: Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo oridne da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine (self, nomeP, prezzoP, quantitaP,
                     nomeC, mailC, CategoriaC):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP, prezzoP), quantitaP)],
                      ClienteRecord(nomeC, mailC, CategoriaC))

    def processa_prossimo_ordine(self):

        #Assicuriamoci che un ordine da processare esista

        print("\n" + "-"*60)
        print("\n" + "-" * 60)

        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("","",""))

        # Se esiste, gestiamo il primo in coda
        ordine = self._ordini_da_processare.popleft()

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        # aggiornare statistiche sui prodotti venduti --
        # Laptop - 10 + 1
        # Mouse - 5 + 2
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        # Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato.")

        return True, ordine


    def processa_tutti_gli_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda."""

        print("="*60)
        print(f"Processando {len(self._ordini_da_processare)} ordini.")

        ordini = []
        while self._ordini_da_processare:
            _ , ordine = self.processa_prossimo_ordine()
            ordini.append(ordine)
        print("Tutti gli ordini sono stati processasti.")

        return ordini


    def get_statistiche_prodotti(self, top_n: int = 5 ):
        "questo metodo restituisce info sui prodotti piu venduti."
        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))
        return valori

    def get_distribuzione_categorie(self):
        """questo metodo restituisce info su totale fatturato per ogni categoria presente"""
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_Fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_Fatturato))
        return valori

    def stampa_riepilogo(self):
        """Stampa info di massima"""
        print("\n" + "="*60)
        print("Stato attuale del business:")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        print("Prodotti piu venduti:")
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print(f"Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat}: {fatturato}")

    def get_riepilogo(self):
        """Restituisce una stringa con le info di massima"""
        sommario = ""
        sommario += "\n" + "="*60
        sommario += f"\n Ordini correttamente gestiti: {len(self._ordini_processati)}"
        sommario += f"\n Ordini in coda: {len(self._ordini_da_processare)}"

        sommario += ("\n Prodotti piu venduti:")
        for prod, quantita in self.get_statistiche_prodotti():
            sommario += f"\n {prod}: {quantita}"

        sommario += f"\n Fatturato per categoria:"
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario += f"\n {cat}: {fatturato}"
        sommario += "\n" + "=" * 60

        return sommario


def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mause", 10.0), 3)],
                ClienteRecord("Mario Rossi", "mario@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mause", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 2500.0), 3)],
                ClienteRecord("Fulvio Bianchi", "bianchi@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mause", 10.0), 3)],
                ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 900.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
                ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mause", 10.0), 3)],
                ClienteRecord("Tur Sba", "sbartuliante@libero.unict", "Bronze")),
    ]

if __name__ == "__main__":
    test_modulo()