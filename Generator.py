import sys

def findGenerator(p):
	primeFactors=[];
	p1=p-1;
	primeFactors=findPrimefactors(p1);
	for i in range(2,p):
		flag=0;
		for pf in primeFactors:
			a1=p1/pf;
			a2=i**a1;
			a3=a2%p;
			if a3==1:
				flag=1;
				break;
			else:
				flag=0;

		if flag==0:
			return i;


def findPrimefactors(p):
	factors=[];
	for i in range(1,p+1):
		if p%i==0:
			if checkPrime(i):
				factors.append(i);

	return factors;


def checkPrime(p):
	count=0;
	for i in range(1,p+1):
		if p%i==0:
			count=count+1;

	if count==2:
		return True;
	else:
		return False;

def main(argv):
	g=findGenerator(int(argv[1]));
	print g;

if __name__ == '__main__':
	main(sys.argv);