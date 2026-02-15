def get_factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors
number=int(input("Number= "))
print("Factors",get_factors(number))

def int_to_roman(number):
    value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol=[
        "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"
        ]
    roman=""
    i=0
    while number>0:
        for _ in range(number//value[i]):
            roman+=symbol[i]
            number-=value[i]
        i=i+1
    return roman
print(int_to_roman(2026))

def roman_to_integer(number):
    roman={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    result_integer=0

    for i in range(0,len(number)-1):
        if roman[number[i]]<roman[number[i+1]]:
            result_integer-=roman[number[i]]
        else:
            result_integer+=roman[number[i]]
    return result_integer+roman[number[-1]]
    
roman_number=input("Input the roman numeral: ")
print("The numeral value would be",roman_to_integer(roman_number))