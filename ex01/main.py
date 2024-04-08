from funcionario import Funcionario
from departamento import Departamento


nome_funcionario = str(input("Digite o nome do funcionario: "))
salario_funcionario = float(input("Digite o salário do funcionário: "))
nome_departamento = str(input("Digite o nome do departamento: "))
codigo_departamento = int(input("digite o código do departamento: "))

departamento = Departamento(nome_departamento, codigo_departamento)
funcionario = Funcionario(nome_funcionario, salario_funcionario)

funcionario.atribuir_departamento(departamento)

print("\nDados do funcionário -")
print("Nome:", funcionario.nome)
print("Salário:", funcionario.salario)

print("\nDados do departamento -")
print("Nome:", departamento.nome)
print("Codigo:", departamento.codigo)