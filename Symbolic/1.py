import sympy as sp

t = sp.symbols('t')
y = sp.Function('y')(t)

n = 2

y_serie = sum(a_k * t ** k for k, a_k in enumerate(sp.symbols('a0:10')))

equacao_serie = sp.Derivative(y_serie, t) - sp.exp(-t) + y_serie ** n

coef_eqs = [equacao_serie.coeff(t, k).expand() for k in range(10)]

coeficientes = sp.solve(coef_eqs, sp.symbols('a0:10'))

y_solucao_serie = y_serie.subs(coeficientes)

print("Solução da equação diferencial como série de potências:")
print(y_solucao_serie)
