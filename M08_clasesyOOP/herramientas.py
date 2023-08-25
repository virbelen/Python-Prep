class Herramientas:
    def __init__(self, lista_numeros):
       if type(lista_numeros) != list:
        raise ValueError('Se ha creado una lista vacia. Se esoperaba el ingreso de una lista de numeros enteros')
       else:
        self.lista = lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')
            
    def conversion_grados(self, origen, destino):
        parametros_esperados = ['celsius', 'farenheit', 'kelvin']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print(f'Los parametros de origen esperados son: {parametros_esperados}')
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print(f'Los parametros de destino esperados son: {parametros_esperados}')    
            return lista_conversion
        
        for i in self.lista:
           lista_conversion.append(self.__conversion_grados(i, origen,destino))
        return lista_conversion

    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
            return lista_factorial

    def __verifica_primo(self, numero):
        es_primo = True

        if numero <= 1:
        # print('Los primos son mayores que 2')
            return None
        if numero == 2:
            return True
        
        for i in range(2, numero):
            if numero%i == 0:
               es_primo = False
            break

        return es_primo

    def valor_modal(self, lista, modo = 'menor'):
        contador = {}
        for num in lista:
            if num in contador.keys():
                contador[num] += 1
            else:
                contador[num] = 1

        maximo_repeticion = 0
        mas_repetido = []

        for numero, repeticion in contador.items():
            if repeticion >  maximo_repeticion:
                maximo_repeticion = repeticion #forma para buscar un maximo 
                mas_repetido = [numero]
            elif repeticion == maximo_repeticion:
                mas_repetido.append(numero)

        if modo == 'menor':
            mas_repetido_num = min(mas_repetido)
        elif modo == 'mayor' :
            mas_repetido_num = max(mas_repetido)
                
        return mas_repetido_num , maximo_repeticion

    def __conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        
        return valor_destino

    def __factorial(self, numero):
        if type(numero) != int or numero <= 0:
            return None
        if numero <= 1:
            return 1
        
        numero = numero * self.__factorial(numero - 1)
        return numero