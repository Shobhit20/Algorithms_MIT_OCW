def karatsuba(X, Y):
	if len(str(X))>1 and len(str(Y))>1:
		n = max(len(str(X)), len(str(Y)))
		n = n/2
		a = X%(10**n)
		b = X / (10**n)
		c = Y % (10**n)
		d = Y / (10**n)
		z0 = karatsuba(b, d)
		z2 = karatsuba(a, c)
		z1 = karatsuba(a+b, c+d) - z0 - z2
		
		result = z0 * 10**(2*n) + z1 * 10**n + z2
		return result
	else:
		return X*Y

	
if __name__ == "__main__":
	x = raw_input("Enter 1st no: ")
	y = raw_input("Enter 2nd no: ")
	res = karatsuba(int(x), int(y))
	print "The result of the algorithm is ", res
		
		

