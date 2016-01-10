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

def main(argv):
   gcd=findGcd(int(argv[1]),int(argv[2]));
   print gcd;

if __name__ == '__main__':
	main(sys.argv);