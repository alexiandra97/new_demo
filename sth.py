import pandas as pd
def stl(tekst):
    li = tekst.split(",")
    ime = li[0]
    zemlja = li[-1]
    ostalo = li[1:-1]
    deli=","
    ostalo = deli.join(ostalo)


    return ime,zemlja, ostalo

podaci=[]

file1 = open("doc.txt.txt", 'r')
count = 0
for i in file1:
    Name, Organization, Country = stl(i)
    podaci.append([Name, Organization, Country])
    count+=1
    
df = pd.DataFrame(podaci, columns=['Name', 'Organization', 'Country'])

df.to_csv("podaci.csv")