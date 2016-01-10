
import sys
import ModularInverse

R=();

def doubleP(P,a,p):
	R=()
	BN=(3*(P[0]**2))+a;
	BD=2*P[1];
	XN=(BN**2);
	XD=BD**2;
	#print 'test1***'
	#print XD,p;
	if XD==0:
		return 'O';
	try :
		XN1=ModularInverse.findModularInverse(p,XD);
	except:
		XN1=0;
		print 'handled'

	XN=((XN*XN1)-2*P[0])%p;
	R=(XN,0);
	YN1=BN*(P[0]-R[0]);
	try :
		YN=ModularInverse.findModularInverse(p,BD);
	except:
		YN=0;
	YN=((YN*YN1)-P[1])%p;
	R=(R[0],YN);
	return R; 

def addP(P,Q,a,p):
	R=()
	AN=(P[1]-Q[1]);
	AD=(P[0]-Q[0])%p;
	if AD==0:
		return 'O'
		
	AN=(ModularInverse.findModularInverse(p,AD)*AN)%p;
	XN=((AN**2)-P[0]-Q[0])%p;
	R=(XN,0);
	YN=((AN*(P[0]-R[0]))-P[1])%p;
	R=(R[0],YN);
	return R;

def main(argv):
	P=(int(argv[1]),int(argv[2]));
	a=int(argv[3]);
	p=int(argv[4]);
  	R=doubleP(P,a,p);		#xp,yp,a,p

  	print R;
  	Result=addP(P,R,a,p);
  	print Result;
    
if __name__ == '__main__':
	main(sys.argv);