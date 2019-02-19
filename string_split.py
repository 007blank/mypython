def string_split():
    string="a=b;c=d;e=f;g=h"
    split1=string.split(";")
    split2=[]
    for i in split1:
        convertor1=str(i)
        convertor2=convertor1.split("=")
        convertor2=tuple(convertor2)
        split2.append(convertor2)
    return split2
print(string_split())
