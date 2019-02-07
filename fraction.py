def using_in_built_packages():
    from fraction import Fraction
    sum=0
    n= int(input('enter the number of fractions:'))
    for i in range(0,n):
        numerator=int(input('enter the numerator :'+(i+1)))
        denominator=int(input('enter thr denominator:'+(i+1)))
        sum=Fraction(numerator,denominator)+sum
    return sum
sum=using_in_built_packages()
print(sum)
