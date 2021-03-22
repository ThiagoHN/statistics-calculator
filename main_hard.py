import math

def somatorio(conjunto):
    soma = 0

    for x in conjunto:
        soma += x

    return soma

def media(conjunto, count_num_elementos):
    soma = 0

    for x in range(count_num_elementos):
        soma += conjunto[x]

    return (soma/count_num_elementos)

def mediana(conjunto, count_num_elementos):
    pos_meio = int(count_num_elementos/2)
    mediana = conjunto[pos_meio]
    
    if (count_num_elementos % 2 == 0):
        mediana = (conjunto[pos_meio] + conjunto[pos_meio + 1]) / 2
        
    return mediana

def moda(conjunto, count_num_elementos):
    conjunto.sorted()
    conjunto_counter = Counter(conjunto)
    moda = -1

    print(conjunto_counter)

    for x in range(count_num_elementos):
        if conjunto_counter[x] > moda:
            moda = conjunto_counter

    return moda;
    
def desvio_padrao(conjunto, count_num_elementos):
    conjunto_quadrado = [i**2 for i in conjunto]
    
    sum = somatorio(conjunto)
    sum_quadrado = somatorio(conjunto_quadrado)

    desvio_padrao = ((count_num_elementos * sum_quadrado) - (sum ** 2)) / (count_num_elementos * (count_num_elementos - 1))

    return math.sqrt(desvio_padrao)


def coeficiente_variacao(media_resp, desvio_padrao_resp):
    CV = (desvio_padrao_resp / media_resp) * 100
    
    return CV


def main():
    conjunto = []
    count_num_elementos = int(input('Digite a quantidade de elementos do conjunto: ')) 

    for i in range(count_num_elementos):
        conjunto.insert(len(conjunto) + 1, int(input('Digite um valor para o conjunto: ')))

    media_resp = media(conjunto,count_num_elementos)
    mediana_resp = mediana(conjunto,count_num_elementos)
    desvio_padrao_resp = desvio_padrao(conjunto,count_num_elementos)
    coeficiente_variacao_resp = coeficiente_variacao(media_resp, desvio_padrao_resp)

    print('Media:' , float("{:.2f}".format(media_resp)))
    print('Mediana:' , float("{:.2f}".format(mediana_resp)))
    #print('Moda:' , float(moda(conjunto,count_num_elementos)))
    print('S:' , float("{:.2f}".format(desvio_padrao_resp)))
    print('CV:' , float("{:.2f}".format(coeficiente_variacao_resp)))

main()