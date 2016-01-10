
def main():

	text=raw_input("Enter text :");
	text=text.lower();
	position=int(raw_input('Shift By / Enter 0 to exit:'))
	while position!=0:
		shiftedText='';
		if position<1 :
			position=position+26
		for char in text:
			if char==' ':
				shiftedText=shiftedText+str(char);
			else:
				ascii=ord(char);
				ascii=(ascii+position)%122;
				if ascii < 97:
					ascii=ascii+96;

				shiftedText=shiftedText+str(chr(ascii));

		print shiftedText
		position=int(raw_input('Shift By / Enter 0 to exit:'))

	
if __name__ == '__main__':
	main()