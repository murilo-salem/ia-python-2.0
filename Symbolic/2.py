from sympy import Function, Derivative, dsolve, symbols, Eq

t, k = symbols('t k', real=True)
M = Function('M')(t)
Eqn = Derivative(M, t) - k * M

sol = dsolve(Eqn, ics={M.subs(t, 0): 1})

for n in range(2, 11):
    solução_específica = sol.subs(k, n)
    print(f"Para n = {n}: M(t) = {solução_específica.rhs}")