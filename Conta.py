class Conta:
    def __init__(self, titular, numero, saldo):
        # CONVENÇÃO: Usamos _ para indicar que os atributos são "internos" da classe.
        # Assim, garantimos consistência com os outros métodos.
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def deposita(self, valor):
        # Verificação para não permitir depósito de valor negativo
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def extrato(self):
        print(f"Cliente: {self._titular} | Saldo Atual: R$ {self._saldo:.2f}")

