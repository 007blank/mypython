def splitdit():
    st = "a=b;c=d;e=f;g=h"
    d = dict(x.split('=') for x in st.split(';'))
    return d
print(splitdit())
