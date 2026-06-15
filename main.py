
class Conto:
    
    def __init__(self, titolare, saldo, numero_conto):
        self.titolare = titolare
        self.saldo = saldo
        self.numero_conto = numero_conto


    @property 
    def deposita(self):
        return f'{self.saldo}'

    @deposita.setter
    def deposita(self, nuovo_saldo): 

        if nuovo_saldo > 0:
            self.saldo += nuovo_saldo
        else:
            print("Il depositamento di soldi è nullo")


    @property
    def preleva(self):
        return f"{self.saldo}"


    @preleva.setter
    def preleva(self, nuovo_saldo):

        if nuovo_saldo > self.saldo:
            print("Non hai abbastanza denaro")
            raise ValueError
        else:
            self.saldo -= nuovo_saldo

    def mostra_saldo(self):
        return f"Questo è il tuo denaro: {self.saldo}$"
    

class Conto_corrente(Conto):
    pass


class Conto_risparmio(Conto):
    
    def applica_interessi(self):
        self.saldo = self.saldo * 2
        return f"Con gli interessi il tuo saldo sarebbe {self.saldo}$"


class Banca:

    def __init__(self, name, id):
        self.name = name 
        self.id = id
        self.conti = []

    def utenti(self):
        self.conti.append(self.name)
        return self.conti





#persona1 = Conto('Daniel', 400, 1234)
persona1 = Conto_risparmio('Daniel', 400, 1234)
banca = Banca('Daniel', 1234)

persona1.deposita = 10
persona1.deposita = 5

persona1.preleva = 400

print(persona1.mostra_saldo())
print(persona1.applica_interessi())
print(banca.utenti())