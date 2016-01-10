import sys
import Addition


def findScalarMul(decimal,P,a,p):
	R=P;
	binary="{0:b}".format(decimal);
	for i in range(1,len(binary)):
		if binary[i]=='1':
			R=Addition.doubleP(R,a,p);
			R=Addition.addP(P,R,a,p);
		else:
			R=Addition.doubleP(R,a,p);

	return R;

def main(argv):
	decimal=int(argv[1]);
	P=(int(argv[2]),int(argv[3]));
	a=int(argv[4]);
	p=int(argv[5]);
	R=findScalarMul(decimal,P,a,p);
	print R;

if __name__ == '__main__':
	main(sys.argv);