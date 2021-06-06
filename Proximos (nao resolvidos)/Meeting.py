# -*- coding: utf-8 -*-
"""
O maior problema do encontro é: os membros estão todos espalhados pelo país. Para isso, a escolha da cidade onde vai
acontecer o encontro é feita de forma
que não prejudique nenhum dos caminhoneiros. O critério para isso é: a distância mais longa para chegar ao local para
qualquer um dos caminhoneiros é a mínima possível. Em outras palavras, a distância percorrida pelo caminhoneiro mais
distante deve ser o caminho mais curto possível.

A primeira linha de entrada contém dois inteiros N (2 ≤ N ≤ 100) e M ( N - 1 ≤ M ≤ 10000), eles representam,
respectivamente, a quantidade de cidades e a quantidade de estradas que as conectam. As cidades são identificadas
por números inteiros entre 0 e N - 1 . As próximas M linhas conterão, em cada uma, uma descrição da via. Cada descrição
será composta por três inteiros: U , V e W , onde U e V são cidades (0 ≤ U ≤ N - 1 e 0 ≤ V ≤ N - 1 ) e W é a distância
entre as cidades (todas as estradas são de mão dupla, 1 ≤ W ≤ 100). Sempre é possível viajar entre as cidades com
estradas disponíveis, mas pode haver mais de uma estrada conectando o mesmo par de cidades.
"""

n, m = map(int, input().split())
estradas = {}
for _ in range(m):
    dados = tuple(map(int, input().split()))
    estradas[dados[:2]] = dados[2]
for cidade_sede in range(n):
    distancia_minima = {}
    for cidade in range(n):
        pass


"""for chave, valor in estradas.items():
    print(chave, valor)
print(estradas)"""
