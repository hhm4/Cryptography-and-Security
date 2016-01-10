import sys
import Root
import Order
import Addition

def main(argv):
	a=13;
	b=9;
	p=7951;
	output='Order\t';

	bigOrder=1;
	for x in range(0,p):
		root=Root.findRoot(x,a,b,p);
		if root!='NOT_A_ROOT':
			root1=(x,root[0]);
			root2=(x,root[1]);
			res=();
			order=Order.findOrder(root1,a,p);
			

			output = str(order)+'\t1-'+str(root1)+' ';
			if bigOrder< order:
				bigOrder=order;
				res=root1;
			#R=Addition.doubleP(root1,a,p);
			#output=output+'2-'+str(R)+' ';
			#for i in range(3,order):
			#	R=Addition.addP(root1,R,a,p);
			#	output=output+str(i)+'-'+str(R)+' ';

			#print output;
			order=Order.findOrder(root2,a,p);
			if bigOrder< order:
				bigOrder=order;
				res=root2;
			output = str(order)+'\t1-'+str(root2)+' ';
			#print output;

	print bigOrder, res;
			#R=Addition.doubleP(root2,a,p);
			#output=output+'2-'+str(R)+' ';
			#for i in range(3,order):
			#	R=Addition.addP(root2,R,a,p);
			#	output=output+str(i)+'-'+str(R)+' ';

			


if __name__ == '__main__':
	main(sys.argv);