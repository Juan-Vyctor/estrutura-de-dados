# 1
# alternativa c)

# 2
# (A)
# (C)
# (B)
# (D)

# 3
# alternativa c)

# 4
# a análise empírica se refere à fazer testes com o algoritmo e, ao receber os resultados, faz o levantamento da performance do código
# --------------------------------------------------------------------------------------------------------------------------------------
# a análise matemática analisa de forma teórica o código, considerando seu melhor e pior caso, além dos casos médios, e assim oferecendo
# uma fórmula matemática da performance do algoritmo

# 5

# 6
# i = 0 (1t)
# i <= 3 (1t)
# i > 3 and j < 5 (2t)
# soma = (soma + i) * 5 (3t)
# for i in range(0, 5) (6t)

# 7
# o(n)
# o(nˆ3)
# o(n)
# o(4) = o(1)
# o(nˆ2)


# 8
# def somar(a, b): l1 * 1
#     soma = a + b l2 * 1
#     return soma l3 * 1
# t(n) = 1 + 1 + 1 = 3
# --------------------------------------------------------------------------------------------------------------------------------------
# def multiplicar(a, b): l1 * 1
#     produto = a * b l2 * 1
#     return produto l3 * 1
# t(n) = 1 + 1 + 1 = 3
# --------------------------------------------------------------------------------------------------------------------------------------
# def potencializar(b, e): l1 * 1
#     potencia = 1 l2 * 1
#     for i in range(e): l3 * n+1
#         potencia *= b l4 * n
#     return potencia l5 * 1
# t(n) = 1 + 1 + (1 * n+1) + (1 * n) + 1 = 2n + 4