# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computer.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mzane <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/05/27 10:26:43 by mzane             #+#    #+#              #
#    Updated: 2015/06/21 09:36:09 by mzane            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys
from pylab import *

def graph_poly(a1, b1, c1):
	a = float(a1)
	b = float(b1)
	c = float(c1)
	t = arange(-10.0, 10.0, 0.1)
	s1 = a * t**2 + b * t + c
	plot(t, s1)
	axhline(linewidth=4, color='r')
	title('Polynomial/Linear')
	grid(True)
	show()

def racine(val):
	if val == 0.0:
		return 0.0
	else:
		m = 1.0
	n = val
	while n >= 2.0:
		n= 0.25 * n
		m= 2.0 * m
	while n < 0.5:
		n = 4.0 * n
		m = 0.5 * m
	a = n
	b = 1.0 - n
	while 1 == 1:
		a = a * (1.0 + 0.5 * b)
		b = 0.25 * (3.0 + b) * b * b
		if b < 1.0E-15:
			return (a * m)

def carre(x):
	x = float(x)
	x = x * x
	return x

def complexe(poly, delta):
	real = (-1 * float(poly[4])) / (2 * float(poly[8]))
	ima = racine(delta * -1)
	print ("\033[32m==========SOLUTION======================\033[37m")
	print ("x1 = " + str(real) + " - " + str(ima) + "i / "),
	print (str(2 * float(poly[8])))
	print ("x2 = " + str(real) + " + " + str(ima) + "i / "),
	print(str(2 * float(poly[8])))

def second_degress(poly):
	c = float(poly[0])
	if poly[1] == "-":
		b = -1 * float(poly[4])
	else:
		b = float(poly[4])
	if poly[5] == "-":
		a = -1 * float(poly[8])
	else:
		a = float(poly[8])
	print("avec : ")
	print("\033[31m[a]\033[37m = " + str(a))
	print("\033[31m[b]\033[37m = " + str(b))
	print("\033[31m[c]\033[37m = " + str(c))
	delta = carre(b) - (4 * a * c)
	print("\033[32m[------ DISCRIMANT : -----]\033[37m")
	print("\033[31m[Delta]\033[37m = b^2 - 4*ac soit \033[31m[Delta]\033[37m = (" + str(b) + ")^2 " + "-4*"+ str(a) + "*" + str(c))
	print("\033[31m[Delta]\033[37m vaut = " + str(delta) + " Donc :")
	if delta > 0:
		print ("\033[4mDelta > 0 alors l'equation admet 2 solutions reelles x1 et x2:")
		print ("x1 : " + str(-1 * (b + racine(delta)) / (2 * a)))
		print ("x2 : " + str(-1 *(b - racine(delta)) / (2 * a)))
	if delta == 0:
		print("\033[4mDelta = 0 alors l'equation admet une solution reelle double -b/2a:\033[0m")
		print ((-1 * b) / (2 * a))
	if delta < 0:
		print("\033[4mDelta < 0 alors l'equation possede pas de solution\033[0m"),
		print("\033[4mmais admet 2 solutions complexes x1 et x2 :\033[0m")
		complexe (poly, delta)
	if len(sys.argv) == 3:
		graph_poly(a, b, c)

def all_solution():
	print("\033[32m===========La forme reduite===========\033[37m")
	print(" 0 = 0")
	print("\033[93mLe degre polynome: 0 ,Donc:\033[0m")
	print("\033[32m----------SOLUTION--------------------\033[37m")
	print("\033[4mTout les reels sont une solution")

def first_degress(poly):
	if poly[1] == '-':
		solution = float(poly[0]) / float(poly[4])
		solution *= -1
	else:
		solution = float(poly[0]) / float(poly[4])
	print("\033[32m[-------------SOLUTION-----------------]\033[37m'")
	print("\033[4mla solution de l'equation est egal a : " + str(solution))

def	no_solution():
	print("\033[32m[----------SOLUTION-------]\033[37m")
	print("\033[4mil n'y a pas de solution\033[0m ")

def builtins(poly, count):
	if count == 0 and poly[0] != 0:
		no_solution()
	elif count == 0 and poly[0] == 0:
		all_solution()
	elif count == 1:
		first_degress(poly)
	elif count == 2:
		second_degress(poly)
	elif count > 2:
		print("\033[32m[--------------SOLUTION------------------]\033[37m")
		print("\033[4mle degre polynome est strictement superieur de 2, I cain't solve it\033[0m") 


def degress(poly):
	if poly.count("*") == 0:
		return (no_solution())
	count = int(poly[len(poly) - 1].strip("X^"))
	print("\033[1m\033[93mLe degre du polynome est: " + str(count) + '\033[0m')
	builtins(poly, count)

def print_poly(poly):
	i = 0
	print("\033[32m[=========La forme reduite========]\033[37m")
	reduce = " "
	while i < len(poly):
		reduce += ' ' + str(poly[i])
		i += 1
	print(reduce + " = 0")
'''
def check_null(poly):
	i = 0
	truc = poly
	while i < len(truc):
		if truc[i] == '0':
			truc.pop(i)
			truc.pop(i)
			truc.pop(i)
			truc.pop(i)
			i = 0
		elif truc[i] == "X^0":
			truc.pop(i)
			truc.pop(i - 1)
			i = 0
		i += 1
	return truc
'''
def second_part(poly_0, poly_1):
	second = poly_1.strip(' ').split(' ',len(poly_1))
	i = 0
	while i < len(second):
		second[i] = -1 * float(second[i])
		i += 4
	poly_0 += ' +'
	i = 0
	while i < len(second):
		poly_0 += ' ' + str(second[i])
		i += 1
	return (poly_0)

def computer(argv):
	poly = argv.split('=', 1)
	if poly[0] == 0:
		poly[0] = poly[1].strip(' ')
		poly[0] = str(poly[0]) + ' '
		poly[1] = " 0"
	if poly[0].strip(' ') == poly[1].strip(' '):
		return (all_solution())
	if poly[1] != ' 0':
		poly[0] = second_part(poly[0], poly[1])
	poly = poly[0].split(' ', len(poly[0]))
	i = 0
	while i < len(poly):
		if poly[i] == '':
			poly.pop(i)
		i += 1
	i = 0
	while i < len(poly):
		if poly[i] == '*':
			nombre = float(poly[i - 1])
			puissance = poly[i + 1]
			j = i + 2
			while j < len(poly):
				if poly[j] == puissance:
					if poly[j - 3] == '-':
						poly[i - 1] = nombre - float(poly[j - 2])
					elif poly[j - 3] == '+':
						poly[i - 1] = nombre + float(poly[j - 2])
					poly.pop(j)
					poly.pop(j - 1)
					poly.pop(j - 2)
					poly.pop(j - 3)
				j += 1
		i += 1
	if len(poly) == 0:
		return (no_solution())
	print_poly(poly)
	degress(poly)

if len(sys.argv) == 3:
	if sys.argv[1] == '-v':
		computer(sys.argv[2])
elif len (sys.argv) == 2:
	if sys.argv[1] == " " or sys.argv[1] == "" or sys.argv[1].find("=") == -1:
		print("\033[91m\033[1mUsage: put Equation between quotes !\033[0m")
	elif len (sys.argv[1]) != 0:
		computer(sys.argv[1])
else:
	print("\033[91m\033[1mUsage : php computer.py [...Equation...] !\033[0m")
