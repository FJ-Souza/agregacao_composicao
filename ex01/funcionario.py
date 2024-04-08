class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.departamento = None

    def atribuir_departamento(self, departamento):
        self.departamento = departamento