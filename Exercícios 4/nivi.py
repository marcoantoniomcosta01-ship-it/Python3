def conta_bancaria(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo
    self.ativo = False

def __str__(self):
    return f'titular: {self.titular} - saldo:{self.saldo}'

conta1 = conta_bancaria('seu Joao', 1000)

print(conta1)