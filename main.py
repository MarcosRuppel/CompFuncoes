import sympy as sp
# Esse programa requer a instalacao do pacote "sympy" para reconhecer as
# expressoes.


# Criação dos símbolos e das funções
x = sp.symbols('x')
f_x = sp.Function('f')(x)
g_x = sp.Function('g')(x)

# Solicita as expressões de f(x) e g(x) ao usuário
expressao_f = input("Digite a expressão de f(x): ")
expressao_g = input("Digite a expressão de g(x): ")

# Avalia as expressões fornecidas pelo usuário
f_x = sp.sympify(expressao_f)
g_x = sp.sympify(expressao_g)

# Solicita o valor de x
valor_x = float(input("Digite o valor de x: "))

# Calcula as composições das funções
g_composta_f = g_x.subs(x, f_x).subs(x, valor_x)
g_composta_g = g_x.subs(x, g_x).subs(x, valor_x)
f_composta_f = f_x.subs(x, f_x).subs(x, valor_x)
f_composta_g = f_x.subs(x, g_x).subs(x, valor_x)

# Exibe os resultados
print(f"(g ° f)({valor_x}) = {g_composta_f}")
print(f"(g ° g)({valor_x}) = {g_composta_g}")
print(f"(f ° f)({valor_x}) = {f_composta_f}")
print(f"(f ° g)({valor_x}) = {f_composta_g}")
