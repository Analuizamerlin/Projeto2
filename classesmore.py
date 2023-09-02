class Pessoa:
    def __init__(self,nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
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
        print(f'{self.nome} tem {self.idade} anos, {self.altura}m de altura e pesa {self.peso}kg!\n')

lista = []
lista.append(Pessoa(input('Nome: '),input('Idade: '),input('Altura: '),input('Peso: ')))
mais = input('\nDeseja adicionar mais alguém? y/n \n')

while mais == 'y':
    lista.append(Pessoa(input('\nNome: '),input('Idade: '),input('Altura: '),input('Peso: ')))
    mais = input('\nDeseja adicionar mais alguém? y/n \n')

for i in lista:
    print(f'\n{i.eh_maior()}')
    print(i.imc())
    print(i.imc_longo())
    i.apresentar()
