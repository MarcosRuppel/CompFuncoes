def f(x):
    return x**2


def g(x):
    return x - 1


def composic_g_f(x):
    return g(f(x))


def composic_g_g(x):
    return g(g(x))


def composic_f_f(x):
    return f(f(x))


def composic_f_g(x):
    return f(g(x))


def main():
    x = float(input("Digite um valor para x: "))

    result_g_f = composic_g_f(x)
    result_g_g = composic_g_g(x)
    result_f_f = composic_f_f(x)
    result_f_g = composic_f_g(x)

    print(f"(g ∘ f)(x) = {result_g_f}")
    print(f"(g ∘ g)(x) = {result_g_g}")
    print(f"(f ∘ f)(x) = {result_f_f}")
    print(f"(f ∘ g)(x) = {result_f_g}")


if __name__ == "__main__":
    main()
