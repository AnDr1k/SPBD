base = int(input("Enter Base: "))
exp = int(input("Enter Exponentiation: "))
m = int(input("Enter Modular: "))

y = 1

# Fast exponentiation algorithm for calculate b^e mod x
def fast_exp(base, exp, m, y):
	

	if (base == 0):
		return 0
	if (exp == 0):
		if (y == m-1):
			return y
		else:
			return y
	
	if (exp % 2 == 0):
		return (fast_exp(pow(base, 2, m), exp/2,m, y))
	
	else:
		return (fast_exp(base, exp-1,m, base*y%m))
	

print(fast_exp(base, exp, m,y))

	


