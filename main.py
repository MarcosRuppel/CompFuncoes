# Definição das funções f(x) e g(x)
def f(x):
    return x**2

def g(x):
    return x - 1

# Composição de funções
def compose(f, g):
    return lambda x: f(g(x))

# Solicita ao usuário que insira as expressões das funções f(x) e g(x)
f_expression = input("Digite a expressão da função f(x): ")
g_expression = input("Digite a expressão da função g(x): ")

# Avalia as expressões das funções e cria as funções correspondentes
try:
    exec(f"f = lambda x: {f_expression}")
    exec(f"g = lambda x: {g_expression}")
except Exception as e:
    print("Erro ao criar as funções. Certifique-se de que a sintaxe está correta.")
    exit()

# Calcula as composições de funções
gf = compose(g, f)
gg = compose(g, g)
ff = compose(f, f)
fg = compose(f, g)

# Solicita ao usuário que insira um valor para x
x_value = float(input("Digite um valor para x: "))

# Calcula as composições de funções para o valor de x fornecido
result_gf = gf(x_value)
result_gg = gg(x_value)
result_ff = ff(x_value)
result_fg = fg(x_value)

# Imprime os resultados
print(f"(g ° f)({x_value}) = {result_gf}")
print(f"(g ° g)({x_value}) = {result_gg}")
print(f"(f ° f)({x_value}) = {result_ff}")
print(f"(f ° g)({x_value}) = {result_fg}")
