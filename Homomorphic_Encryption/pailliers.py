import random
from fractions import gcd
import constantVar as const
import decrypt
import math

nVoters = 9
nCandi = 5
base = 10
p = 293
q = 433
n = p*q
n2 = n*n
lamda = 0
g = 6497955158
mew = 0
votes = []
encVotes = []
tally = 0

def encryptVote(vote):
   print "inside 1";
   r = genR();
   print "inside 1.5",g,vote,r,n,n2;
   encMsg = ((g**vote) * (r**n)) % n2;
   print "inside 2";
   return encMsg

def callLamda():
   print "---Calculating Lamda---"
   lamda = (p-1) * (q-1) / gcd(p-1,q-1)
   #lamda = lamda
   print "Lamda value = ", lamda, "\n"
   return lamda

def calMew():   
   print "---Calculating Mew---"
   lamda=callLamda();
   print g,lamda,n2,n;
   a = (g**lamda % n2 - 1) / n
   b = n
   print a,b;
   mew = egcd(a, b)
   print "mew:",mew;
   mew = mew[1]
   print "Mew value = ", mew, "\n"
   return mew;

def egcd(a, b):
   if a == 0:
      return (b, 0, 1)
   else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b / a) * y, y)

def genR():
   r = genRamdom(3, n - 1)
   return r
   
def genRamdom(a, b):
	num = random.randrange(a, b)
	return num

def tallyVotes(val):
   print "---Tallying votes---"
   product = 1
   
   #Go through all the encrypted votes
   product *= val
   
  # result = product % n2   
   
   print "Encrypted Tallied vote value = ", product, "\n"
   
   decryptTally(product)

def decryptTally(encTally):
   print "---Decrypting tally result---"
   
   divisor = 10
   numVote = 0 #Tempoarily stores the number of votes for one candidate
   lamda=callLamda();
   mew=calMew();
   print encTally,lamda,n2,mew,n;
   decryptTally = (((((encTally**lamda) % n2) -1)/n)* mew) % n
   print "Decrypted Tally vote = ", decryptTally, "\n"
   
   #Initialize array where all candiates currently have 0 votes
   tallyResult = 0
   #[0 for i in range(nCandi)] 
      
   #Get the votes starting with the last listed candiate first
   #for i in range(nCandi-1, -1, -1):
  # tallyResult= int(math.floor(decryptTally / divisor**0))
  # decryptTally = decryptTally - (tallyResult* divisor**0)
   print decryptTally
    
      
   return tallyResult

def main():
	callLamda();
   	calMew();
	plaintext1=int(raw_input("Enter plain text 1 : "));
	#plaintext2=int(raw_input("Enter plain text 2 : "));
	pt1=base**(int(plaintext1));
	print "pt1",pt1;
	cipherText1 = encryptVote(pt1);
	print "cipherText 1 :",cipherText1;
	decryptTally(cipherText1)


if __name__ == '__main__':
	main();
