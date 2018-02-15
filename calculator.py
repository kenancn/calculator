def main_module():
    num1,num2=input_module()
    menu_module(num1,num2)


main_module()

def sub (sayi1,sayi2):
    print('{} + {} = '.format(sayi1,sayi2)
    toplam=sayi1+sayi2
    output_module(toplam)

def extraction(sayi1,sayi2):
    print('{} + {} = '.format(sayi1,sayi2)
    cikarim=sayi1-sayi2
    output_module(extraction)


def division (num_1,num_2):
    div=num_1/num_2
    output_module(division)
	
def multiplication (num_1,num_2):
    mul=num_1*num_2
    output_module(multiplication)
	  
def input_module():
    num1=input("1. Sayiyi Giriniz: ")
    num2=input("2. Sayiyi Giriniz: ")
    return num1,num2

def menu_module(num1,num2):
    menu_str="""
Islem Secimi:

    1)Toplama Islemi
    2)Cikarma Islemi
    3)Carpma Islemi
    4)Bolme Islemi
    Cikis icin 'q' harfi girin:
    """
    secim=input(menu_str)

    if(secim == "1"):
        sub(num1,num2)
    elif(secim == "2"):
        extraction(num1,num2)
    elif(secim == "3"):
        multiplication(num1,num2)
    elif(secim == "4"):
        division(num1,num2)
    elif(secim == "q"):
        exit()
    else:
        pass


def output_module(result):
    print("Sonuc:  "+result)
