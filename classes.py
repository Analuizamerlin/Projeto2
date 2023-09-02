class Pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def eh_maior(self):
        if self.idade >= 18:
            return True
        else:
            return False
    
    def imc(self):
        self.imc = self.peso/(self.altura**2)
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
        print(f'Olá, me chamo {self.nome}, tenho {self.idade} anos, {self.altura}m de altura e peso {self.peso}kg!')

    def compara_idade(self,valor):
        if valor == self.idade:
            print(f'{self.nome} tem a mesma idade!')
        elif valor < self.idade:
            print(f'{self.nome} é mais velha!')
        else:
            print(f'{self.nome} é mais nova!')

pessoa1 = Pessoa('Ana Luiza',21,1.69,68.8)

print(pessoa1.eh_maior())
print(pessoa1.imc())
print(pessoa1.imc_longo())
pessoa1.apresentar()
pessoa1.compara_idade(22)