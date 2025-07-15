class Main:
    pass
print("Testanod o Projeto")

from Cliente import Cliente
from Conta import Conta

c1= Cliente ("João", "991234-5678")
conta=Conta(c1.nome, 6565, 10)


conta.deposita(100)
conta.saque(50)
conta.extrato()
