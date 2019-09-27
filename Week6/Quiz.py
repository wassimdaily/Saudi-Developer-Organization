def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))
base=int(input("Enter the base number.."))
exp=int(input("Enter the exponential value.."))
print("Result:",power(base,exp))


List = [-4, -6, -5, -1, 2, 3, 7, 9, 88]

checker = lambda x: True if x>0 else False

for y in List:
	print(y, checker(y))
