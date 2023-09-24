import re

class Pessoa:
    def __init__(self,nome, idade, altura, peso, nascimento):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nascimento = nascimento

    def eh_maior(self):
        if int(self.idade) >= 18:
            return f'{self.nome} é maior de idade!'
        else:
            return f'{self.nome} é menor de idade!'
    
    def imc(self):
        self.imc = float(self.peso)/(float(self.altura)**2)
        return f'imc = {self.imc:.2f}'

    def  imc_longo(self):
        if self.imc < 18.5:
            return 'Faixa de peso: Baixo peso.'
        elif self.imc <= 24.9:
            return 'Faixa de peso: Normal.'
        elif self.imc <= 29.9:
            return 'Faixa de peso: Sobrepeso.'
        elif self.imc <= 34.9: 
            return 'Faixa de peso: Obesidade (Grau I).'
        elif self.imc <= 39.9:
            return 'Faixa de peso: Obesidade Severa (Grau II).'
        else:
            return 'Faixa de peso: Obesidade Mórbida (Grau III).'

    def apresentar(self):
        print(f'{self.nome} tem {self.idade} anos, {self.altura}m de altura, pesa {self.peso}kg e nasceu em {self.nascimento}.\n')

while True:
    nome = input('Nome completo: ')
    if not re.match(r'^[a-zA-Zà-úÀ-Ú\s]+$', nome):
        print('Entrada inválida. Tente novamente!')
    else: 
        break

while True:
    idade = input('Idade: ')
    if not re.match(r'^[0-9]+$', idade):
        print('Entrada inválida. Tente novamente!')
    else: 
        break

while True:
    altura = input('Altura: ')
    if not re.match(r'^[1-9]\.[0-9]+$|^0\.[1-9]+$', altura):
        print('Entrada inválida. Tente novamente!')
    else: 
        break

while True:
    peso = input('Peso: ')
    if not re.match(r'^[1-9][0-9]*[0-9]*\.[0-9]', peso)or float(peso)<=0:
        print('Entrada inválida. Tente novamente!')
    else: 
        break

while True:
    nascimento = input('Data de Nascimento(dd/mm/aaaa): ')
    if not re.match(r'^(0[0-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}+$', nascimento):
        print('Entrada inválida. Tente novamente!')
    else: 
        break

pessoa1 = Pessoa(nome, idade, altura, peso, nascimento)

print(f'\n{pessoa1.eh_maior()}')
print(pessoa1.imc())
print(pessoa1.imc_longo())
pessoa1.apresentar()
