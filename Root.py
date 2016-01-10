import sys

def findRoot(x,a,b,p):
	Y2=((x**3)+(a*x)+b)%p;
	root1=(Y2**((p+1)/4))%p;
	root2=p-root1;
	r1=(root1**2)%p;
	r2=(root2**2)%p;
	if r1==Y2 and r2==Y2:
		root=(root1,root2);
	else:
		root='NOT_A_ROOT';

	return root;

def main(argv):

	a=2;
	b=9;
	p=23;
	for x in range(0,p):
		root=findRoot(x,a,b,p);
		if root=='NOT_A_ROOT':
			print root;
		else:
			root1=(x,root[0]);
			root2=(x,root[1]);
			print root1,root2;
		
	
    
if __name__ == '__main__':
	main(sys.argv); 