def median(l):
	l.sort()
	half=len(l)/2
	b=l[half]
	c=l[-half-1]
	return(b+c)/2
n=int(input())
l=[int(x) for x in raw_input().split()]
print(median(l))
