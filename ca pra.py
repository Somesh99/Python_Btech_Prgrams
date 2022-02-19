def fact(x):
	if x==0:
		print("facto is 1")
	else:
		for i in x:
			y=y*i
			i+=1
			return y
x=int(input("enter no "))
print("factorial of %d is %d" %x,fact())
