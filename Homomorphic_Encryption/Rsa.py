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
	print "\nImplementation of Unpadded RSA"
	print "------------------------------"
	p=541;
	q=787;
	print "p : ",p;
	print "q : ",q;
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
	plainText2=[];
	plainText3=[];
	print "\nPlainText"
	print "---------"
	for i in range(0,num):
		text=int(raw_input("Enter plainText 1 : "));
		plainText.append(text);

	for i in range(0,num):
		text=int(raw_input("Enter plainText 2 : "));
		plainText2.append(text);

	for i in range(0,num):
		text=int(raw_input("Enter plainText 3 : "));
		plainText3.append(text);

	cipherText=[];
	cipherText2=[];
	cipherText3=[];
	for i in range(0,num):
		cipherText.append(findModulo(plainText[i],e,n));

	for i in range(0,num):
		cipherText2.append(findModulo(plainText2[i],e,n));

	for i in range(0,num):
		cipherText3.append(findModulo(plainText3[i],e,n));

	cipherText4=[];
	for i in range(0,num):
		cipherText4.append(cipherText3[i]*cipherText2[i]*cipherText[i]);
	print "\nCipherText"
	print "----------"
	print "CipherText 1 : ",cipherText[0];
	print "CipherText 2 : ",cipherText2[0];
	print "CipherText 3 : ",cipherText3[0];
	print "\nAfter Mulitplication";
	print "--------------------";
	print "CipherText 4 : ",cipherText4[0];

	decipheredText=[];
	decipheredText2=[];
	decipheredText3=[];
	decipheredText4=[];
	for i in range(0,num):
		decipheredText.append(findModulo(cipherText[i],d,n));

	for i in range(0,num):
		decipheredText2.append(findModulo(cipherText2[i],d,n));

	for i in range(0,num):
		decipheredText3.append(findModulo(cipherText3[i],d,n));

	for i in range(0,num):
		decipheredText4.append(findModulo(cipherText4[i],d,n));

	#print decipheredText;
	#print decipheredText2;
	print "PlainText 4 : ",decipheredText4[0];

if __name__ == '__main__':
	main();