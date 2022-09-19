# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:55:22 2022

Este doc do bb contém um erro na pag 16
https://www.bb.com.br/docs/pub/emp/empl/dwn/Doc5175Bloqueto.pdf

Esta função é usada no cálculo dos digitos verificadores em Boletos Bancários
Segue especificação da Febraban

Voce pode baixar documento explicativo do Banco do Brasil no link abaixo:
https://www.bb.com.br/docs/pub/emp/empl/dwn/Doc5175Bloqueto.pdf
Obs.:
Existe um erro de cálculo na pagina 16.
Entretanto, a seguir o documento explica o cálculo corretamente.

@author: Manoel Canova
"""

# O argumento aceita somente valores em string, ok?
def digModulo10(numString):
    # 1. "mult" é a variável de multiplicação
    #    será sempre 2, 1, 2, 1, 2, 1, ...
    #    iniciei esta variável com o valor 1 para inverter logo adiante.
    mult = 1
    somaDigitos = 0
    # 2. "numReverso" é o "numString" invertido.
    #    O cálculo é feito da direita para a esquerda.
    numReverso = numString[::-1]
    for digitoStr in numReverso:
        # 3. Como expliquei acima, o primeiro valor é 2.
        #    o "if" abaixo se encarregará de inputar o valor 2 a 
        #    variável "mult".
        if mult == 1:
            mult = 2
        else:
            mult = 1
        # 4. Transforma o numero string em número inteiro
        #    e multiplica pelo valor 2 ou 1.
        #    A partir daqui, o numero será chamado de "digito"
        digito = int(digitoStr)
        digito = digito  * mult
        # 5. Se o valor multiplicado do digito for maior que 9, ele é recalculado.
        #    Neste caso, é feito a soma dos dígitos deste valor.
        #    Por exemplo: se "digito" for 16, o valor do 
        #    dígito será 1+6, ou seja, 7
        if digito > 9:
            digito = int(str(digito)[0]) + int(str(digito)[1])
        # 6. "somaDigitos" acumula os valores dos digitos calculados
        somaDigitos += digito
    # 7. Por fim, é calculado o módulo (resto da divisão por 10)
    #    e o valor final é a subtração deste valor de módulo por 10
    Modulo10 = somaDigitos % 10
    digitoVerificador = 10 - Modulo10
    return(digitoVerificador)

    
print(digModulo10("4660010102"))

