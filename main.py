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
    
def desvio_padrao():
    return NULL

def coeficiente_variacao():
    return NULL

def main():
    conjunto = []
    count_num_elementos = int(input('Digite a quantidade de elementos do conjunto: ')) 

    for i in range(count_num_elementos):
        conjunto.insert(len(conjunto) + 1, float(input('Digite um valor para o conjunto: ')))

    print('Media:' , float("{:.2f}".format(media(conjunto,count_num_elementos))))
    print('Mediana:' , float("{:.2f}".format(mediana(conjunto,count_num_elementos))))
    #print('Moda:' , float(moda(conjunto,count_num_elementos)))
    #print('S: ' + desvio_padrao)
    #print('CV: ' + coeficiente_variacao)

main()