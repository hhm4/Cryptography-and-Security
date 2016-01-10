import sys
import Addition

def findOrder(P,a,p):
	R=P;
  	order=1;
  	Result=Addition.doubleP(P,a,p)
  	while Result!='O':
  		#print Result;
  		order=order+1;
  		R=Result;
  		Result=Addition.addP(P,R,a,p);

  	order=order+1;
  	return order;

def main(argv):
	P=(int(argv[1]),int(argv[2]));
	a=int(argv[3]);
	p=int(argv[4]);
	order=findOrder(P,a,p);
  	print order;
    
if __name__ == '__main__':
	main(sys.argv);