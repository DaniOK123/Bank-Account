
class Conto_corrente:
    
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
        if nuovo_saldo < 0:
            self.saldo -= nuovo_saldo
        else:
            print("Il prelievo di soldi è nullo")

    def mostra_saldo(self):
        return f"Questo è il tuo denaro: {self.saldo}$"
    


persona1 = Conto_corrente('Daniel', 400, 1234)

persona1.deposita = 10
persona1.deposita = 5

persona1.preleva = -50

print(persona1.mostra_saldo())
