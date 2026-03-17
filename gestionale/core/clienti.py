from dataclasses import dataclass

categorie_valide = {"Gold", "Silver", "Bronze"}

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
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria

    def descrizione(self): #to_string
        # "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

@dataclass()
class ClienteRecord:
    name: str
    email: str
    categoria: str

def _test_modulo():
    c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Bronze")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()