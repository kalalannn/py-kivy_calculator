import parse
import re

vyraz=r"""
        (?:
        ([.0-9]+)| # cislo
        ([*/\-+^])| # operatory
        (,)| # carka
        (sqrt|log)| #funkce
        (\()| # leva zavorka
        (\))| # prava zavorka
        ([a-zA-Z]+) # chyba
        )
    """
user_inp="1.5 - 2 + sqrt(1,2)/2^3fact(3)"
user_inp=re.sub(r"\s","",user_inp,re.X)
print(user_inp)
m=re.findall(vyraz,user_inp,re.X)

for r in m:
    if r[0]:
        #cislo
        print("cislo",r[0])
    elif r[1]:
        #operator
        print("operator",r[1])
    elif r[2]:
        #carka
        print("carka",r[2])
    elif r[3]:
        #fce
        print("fce",r[3])
    elif r[4]:
        #lb
        print("leva zavorka",r[4])
    elif r[5]: 
        #rb
        print("prava zavorka",r[5])
    elif r[6]:
        #chyba
        print("Neznama fce",r[6])

pl=["".join(i) for i in m]
orig=("".join(pl))
for x in zip(orig,user_inp):
    if x[0]!=x[1]:
        print("neocekavany znak \"%s\"" % x[1])
        break