import sys

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
	inverse=1;
	while count!=0:		
		inverse=(quotient[count]*current)+previous;
		previous=current;
		current=inverse;
		count=count-1;

	if (total%2)==0:
		inverse=p-inverse;

	return inverse;


def main(argv):
	inverse=findModularInverse(int(argv[2]),int(argv[1]));
	print inverse;

if __name__ == '__main__':
	main(sys.argv);