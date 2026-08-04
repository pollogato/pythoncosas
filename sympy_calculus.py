# -*- coding: utf-8 -*-
"""

"""
import sympy
from sympy.plotting import plot3d
from sympy import Eq, pretty

sympy.init_printing(use_unicode=True, wrap_line=True)

# .evalf() evalua en un punto determinado
# sympy.latex(ecuacion) entrega en formato latex


#Definiendo símbolos
x = sympy.Symbol("x")
y = sympy.Symbol("y")

#Ecuación
f = x * y ** 2 + x ** 2 + sympy.sin(2 * y)
#f = sympy.log(x)

#Derivada dx
df_dx = sympy.diff(f, x)
eq_df_dx = sympy.Derivative(f, x) #ecuación
p0 = plot3d(df_dx)
# p0.show()
print(f"La derivada dx de {eq_df_dx} es:\n{df_dx}")
print(pretty(Eq(eq_df_dx, df_dx), use_unicode=True))

# .evalf() evalua en un punto determinado
#print(df_dx.evalf(subs={x: 2, y:6}))

print("")

#Derivada multiple dx dy
df_dx_dy = sympy.diff(f, x, y)
eq_df_dx_dy = sympy.Derivative(f, x, y) #ecuación
p0 = plot3d(df_dx_dy)
# p0.show()
print(f"La soble derivada dxdy de {eq_df_dx_dy} es:\n{df_dx_dy}")

print("")

#Integral dx
sfdx = sympy.integrate(df_dx, (x))
eq_sfdx = sympy.Integral(df_dx, (x)) #ecuación
print(f"La integral dx de {eq_sfdx} es:\n{sfdx} + C")
p1 = plot3d(sfdx)
# p1.show()
print("")


#Integral doble dx dx
ssfdx_dx = sympy.integrate(df_dx, (x),(x))
eq_ssfdx_dx = sympy.Integral(df_dx, (x),(x)) #ecuación
print(f"La integral doble dxdx de {eq_ssfdx_dx} es:\n{str(ssfdx_dx)} + C + xC")
p1 = plot3d(ssfdx_dx)
# p1.show()
print("")

#Integral definida dx
sfdx_dx_def = sympy.integrate(df_dx, (x,5,10))
print(f"La integral definida S5_10 {df_dx} dx es:\n{(sfdx_dx_def)}")
p2 = sympy.plot(sfdx_dx_def)
# p2.show()

print("")
print("")
print("")

#######################
# solve() -> Ecuaciones algebraicas

ecuacion = x**2 - 5*x + 6
ecuacion = sympy.Eq(ecuacion, 0)
solucion = sympy.solve(ecuacion, x)
print(f"Resolver: {ecuacion.args[0]} = {ecuacion.args[1]}")
print(f"Solución simbólica: {solucion}")

print("")
print("")
print("")


# dsolve() -> Ecuaciones diferenciales

t = sympy.Symbol('t')
y = sympy.Function('y')(t)

# EDO simple: dy/dt = y
edo = Eq(y.diff(t), y)
sol_edo = sympy.dsolve(edo, y)
print(f"Ecuación: {edo.args[0]} = {edo.args[1]}")
print(f"Solución general: {sol_edo.args[0]} = {sol_edo.args[1]}")  # Eq(y(t), C1*exp(t))

# Con condición inicial y(0)=1
sol_con_ci = sympy.dsolve(edo, y, ics={y.subs(t, 0): 1})
print(f"\nCon condición y(0)=1: {sol_con_ci.args[0]} = {sol_con_ci.args[1]}")  # Eq(y(t), exp(t))

print("")
print("")
print("")
#######################
# Límites

fl = sympy.sin(x) / x

limite = sympy.limit(fl, x, 0)

print(f"El límite de {fl} en x = 0 es: {limite}")


print("")
print("")
print("")
#######################

# simplify() reduce expresiones a formar algebraicas más simples. Permitiría reducir tiempo de cálculos.

expr = (sympy.sin(x)**2 + sympy.cos(x)**2)
print(expr)
print(sympy.simplify(expr))

print("")
print("")
print("")
#######################
from sympy import log, Symbol
from sympy.integrals.manualintegrate import integral_steps

# steps te "muestra" los pasos a pasos

x = Symbol('x')
steps = integral_steps(log(x), x)
print(steps)
#######################





