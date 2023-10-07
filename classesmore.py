import pandas as pd
import re
import csv
cadastro = []

class menu:
    def acionar():
        print('-'*35)
        print(' '*15,'MENU')
        print('-'*35)
        print('1 - Mostrar a pessoa cadastrada\n2 - Editar a pessoa cadastrada\n3 - Sair do programa')
        print('-'*35)

while True:
    try:

        menu.acionar()
        entrada = int((input(' ')))  

        if entrada == 1:
            cadastro.clear()
            df = pd.read_csv('Cadastro.csv') 

            print(df)        

        elif entrada == 2:  
            cadastro.clear()                     
            while True:
                nome = input('Nome completo: ')
                if not re.match(r'^[a-zA-Zà-úÀ-Ú\s]+$', nome):
                    print('Entrada inválida. Tente novamente!')
                
                else: 
                    cadastro.append(nome)
                    break

            while True:
                idade = input('Idade: ')
                if not re.match(r'^[0-9]+$', idade):
                    print('Entrada inválida. Tente novamente!')
                else: 
                    cadastro.append(idade)
                    break

            while True:
                altura = input('Altura: ')
                if not re.match(r'^[1-9]\.[0-9]+$|^0\.[1-9]+$', altura):
                    print('Entrada inválida. Tente novamente!')
                else:
                    cadastro.append(altura) 
                    break

            while True:
                peso = input('Peso: ')
                if not re.match(r'^[1-9][0-9]*[0-9]*\.[0-9]', peso)or float(peso)<=0:
                    print('Entrada inválida. Tente novamente!')
                else: 
                    cadastro.append(peso)
                    break

            while True:
                nascimento = input('Data de Nascimento(dd/mm/aaaa): ')
                if not re.match(r'^(0[0-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}+$', nascimento):
                    print('Entrada inválida. Tente novamente!')
                else: 
                    cadastro.append(nascimento)
                    break
 
            lista = []
            lista.append(cadastro)
            df2 = pd.DataFrame(lista,columns=['Nome', 'Idade', 'Altura', 'Peso','Nascimento'])
            df2 = df2.to_csv('Cadastro.csv', index=False)
            print('\nCADASTRO REALIZADO COM SUCESSO')

        elif entrada == 3:
            print('\nPROGRAMA FINALIZADO\n')
            break     
        else:
            print('\nENTRADA INVÁLIDA\n')
    except ValueError:
        print('\nERRO: ENTRADA INVÁLIDA\n')
    except FileNotFoundError:
        print('\nERRO: NÃO HÁ PESSOA CADASTRADA\n')