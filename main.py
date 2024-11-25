class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def obter_salario(self):
        return self.__salario

    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.__salario += self.__salario * (percentual / 100)


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, "Gerente", salario)

    def obter_salario_com_bonus(self, bonus):
        return self.obter_salario() + bonus


funcionario = Funcionario("João", "Analista", 3000)
print(f"Salário inicial do {funcionario.nome}: R${funcionario.obter_salario()}")

funcionario.aumentar_salario(15)
print(f"Salário atualizado do {funcionario.nome}: R${funcionario.obter_salario()}")

gerente = Gerente("Maria", 6000)
print(f"Salário inicial do {gerente.nome}: R${gerente.obter_salario()}")

bonus = 2500
print(f"Salário do {gerente.nome} com bônus: R${gerente.obter_salario_com_bonus(bonus)}")
