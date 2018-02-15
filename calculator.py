def main_module():
    num1,num2=input_module()
    menu_module(num1,num2)


main_module()

def sub(sayi1,sayi2):
    print('{} + {} = '.format(sayi1,sayi2)
    toplam=sayi1+sayi2
    return toplam

def extraction(sayi1,sayi2):
    print('{} + {} = '.format(sayi1,sayi2)
    cikarim=sayi1-sayi2
    return cikarim


def division (num_1,num_2):
	div=num_1/num_2
	return div
	
def multiplication (num_1,num_2):
	mul=num_1*num_2
	return mul
