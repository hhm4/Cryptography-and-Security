import sys

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

def main(argv):
	A=findModulo(int(argv[1]),int(argv[2]),int(argv[3]));
	print A;

if __name__ == '__main__':
	main(sys.argv);