import sys

def findGcd(x,y):
	gcd=1;
	factors=[];
	for i in range(1,x+1):
		if x%i==0:
			factors.append(i);

	for f in factors:
		if (y%f==0) and (f>gcd):
			gcd=f;

	return gcd;

def findModularInverse(x,y):	
	p=x;
	remainder={};
	quotient={};
	count=1;
	remainder[count]=y;
	while remainder[count]!=1:
		t=x;
		count=count+1;
		remainder[count]=x%y;
		t=x%y;
		quotient[count-1]=x/y;
		x=y;
		y=t;

	total=count;
	count=count-1;
	current=1;
	previous=0;
	while count!=0:		
		inverse=(quotient[count]*current)+previous;
		previous=current;
		current=inverse;
		count=count-1;

	if (total%2)==0:
		inverse=p-inverse;

	return inverse;

def findModulo(u,m,p):
	modValue=[];
	expo=[];
	remainder=[];
	current=0;
	expo.append(m);
	remainder.append(m%2);
	modValue.append((u**1)%p);
	current=current+1;
	while expo[current-1]!=1:
		expo.append(expo[current-1]/2);
		remainder.append(expo[current]%2);
		modValue.append((modValue[current-1]**2)%p);
		current=current+1;
		
	A=1;
	current=current-1;
	while current>=0:
		if remainder[current]!=0:
			A=(A*modValue[current])%p;
		current=current-1;

	return A;

def main():
	#p=int(raw_input("Enter p : "));
	#q=int(raw_input("Enter q : "));
	p=541;
	q=787;
	n=p*q;
	print "n : "+str(n);
	tn=(p-1)*(q-1);
	print "tn : "+str(tn);
	e=1;
	for i in range(2,tn):
		if findGcd(i,tn)==1:
			e=i;
			break;

	print "e : "+str(e);
	d=findModularInverse(tn,e);
	print "d : "+str(d);
	#num=int(raw_input("Enter no. of blocks : "));
	num=1;
	plainText=[];
	for i in range(0,num):
		text=int(raw_input("Enter P"+str(i)+" : "));
		plainText.append(text);

	cipherText=[];
	for i in range(0,num):
		cipherText.append(findModulo(plainText[i],e,n));

	print cipherText;
	decipheredText=[];
	for i in range(0,num):
		decipheredText.append(findModulo(cipherText[i],d,n));

	print decipheredText;


if __name__ == '__main__':
	main();