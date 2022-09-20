
"
Esta função é usada no cálculo dos digitos verificadores em Boletos Bancários
Segue especificação da Febraban

Voce pode baixar documento explicativo do Banco do Brasil no link abaixo:
https://www.bb.com.br/docs/pub/emp/empl/dwn/Doc5175Bloqueto.pdf
Obs.:
Existe um erro de cálculo na pagina 16.
Entretanto, a seguir o documento explica o cálculo corretamente.

"

library(stringi)

digModulo10 <- function(numString){
  
  # 1. O fator de multiplicação "multi" será sempre 2, 1, 2, 1, 2...
  #    iniciei com o valor 1, mas este valor será invertido adiante
  
  multi <- 1
  
  # 2. A variável "somaDigitos" acumula os valores calculados
  
  somaDigitos <- 0
  
  # 3. Inverti a ordem dos digitos do numero porque o 
  #    cálculo é feito da direita para a esquerda
  
  numReverso <- stri_reverse(numString)
  
  # 4. Pega cada um dos dígitos do número já invertido
  
  for (digitoStr in strsplit(numReverso, "")[[1]]){
    
    # 5. "multi" será sempre 2 ou 1, alternadamente
    
    if (multi == 1){multi <- 2} else {multi <- 1}
    
    # 6. Converte o dígito string para integer e multiplica pelo fator "multi".
    #    Daqui por diante, chamaremos esta variável de "digito"
    
    digito <- as.integer(strtoi(digitoStr) * multi)
    
    # 7. Se "digito" for maior que 9, a função quebra este número em outros 2
    #    digitos, e soma estes digitos. Por exemplo: se "digito" for 16, o novo
    #    "digito" será recalculado em 1+6, ou seja, 7
    
    if (digito > 9){
      digito <- as.integer(substr(toString(digito),1,1)) + as.integer(substr(toString(digito),2,2))
    }
    
    # 8. Os digitos calculados são acumulados na variável "somaDigitos"
    
    somaDigitos <- somaDigitos + digito
  }
  
  # 9. Por fim é calculado o "digitoVerificador": 10 menos o resto da divisão 
  #    de "somaDigitos" por 10.
  
  digitoVerificador <- (10 - (somaDigitos %% 10))
  
  return(digitoVerificador)
}


# O exemplo abaixo retorna o valor 1 para o digito verificador:

print(digModulo10("1234565590"))

