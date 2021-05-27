# sum 1
a=0
sum=5
if a<=sum:
	print("right")
# sum 2
def sum():
	a=0
	sum=9
	sum*=a
	print("sum=",sum)
# sum 2 (function call)
sum()
# convert to String
sum=str(sum)
print("sum="+sum)
# convert to string will not supported to function
# pluse
def pluse():
	a=1
	sum=1
	while a<5:
		sum+=a
		a+=1
	print("sum=",sum,"a=",a)
# pluse function callable
pluse()
