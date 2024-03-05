
#Feghoul Celina.


#inputs
#on s'assure d'abord que le probleme proposé par le user est bien un probleme qu'on peux resoudre avec la methode du bigM
Sol=int(input("votre probleme contient il (=) ou (>=) ? 1.Oui 2.Non"))
while Sol==2:#si non
  print("pour resoudre votre probleme vous n'avez pas besoins de cet algorithme,choisissez un autre probleme!\n")
  Sol=int(input("votre probleme contient il (=) ou (>=) ? 1.Oui 2.Non"))
  #si oui
mode=int(input(" choisissez votre mode.. 1_Max 2_Min"))
var_nbr=int(input("***Entrez le nombre de variables de decision ***\n"))
contraintes_nbr=int(input("***Entrez le nombre de contraintes ***\n"))

# creation d'un tableau qui gardera toutes nos entrées
print("votre fonction objectif est: \n")
zeroMatrix=[]
zeroLine=[]
for i in range(var_nbr):
    zeroLine.append(int(input("coef_"+"x"+str(i+1)+":")))
zeroMatrix.append(zeroLine)
print("les contraintes :  \n")
for i in range(contraintes_nbr):
    print("contrainte ",i+1,"\n")
    zeroLine=[]
    for j in range(var_nbr):
        zeroLine.append(float(input("x"+str(j+1)+"coef : ")))
    zeroLine.append(str(input("le signe ( = ou <= ou >= ): ")))
    zeroLine.append(float(input("b"+str(i+1)+"= ")))
#si b<0 alors on change l'equation on la multipliant par (-1)
    if zeroLine[var_nbr+1]<0:
        for k in range(var_nbr):
            zeroLine[k]=zeroLine[k]*(-1)
        zeroLine[var_nbr+1]=zeroLine[var_nbr+1]*-1
        if zeroLine[var_nbr]=="<=" :
            zeroLine[var_nbr]=">="
        elif zeroLine[var_nbr]==">=":
            zeroLine[var_nbr]="<="
    zeroMatrix.append(zeroLine)

# oneMatrix est la premiéere matrice de l'algo du bigM
oneMatrix=[]
for i in range(contraintes_nbr+2):
    zeroLine=[]
    for j in range(var_nbr+contraintes_nbr*2+2):
        zeroLine.append(0)
    oneMatrix.append(zeroLine)
#application de la methode du bigM
v=var_nbr
c=var_nbr+contraintes_nbr
for i in range(1,contraintes_nbr+1):
    if zeroMatrix[i][var_nbr]=="<=":
        oneMatrix[i][v]=1
        v+=1
    elif zeroMatrix[i][var_nbr]==">=":
        oneMatrix[i][v]=-1
        oneMatrix[i][c]=1
        c+=1
        v+=1  

    elif zeroMatrix[i][var_nbr]=="=":
        oneMatrix[i][c]=1
        c+=1

    

for i in range(1,contraintes_nbr+1):
    for j in range(var_nbr):
        oneMatrix[i][j]=zeroMatrix[i][j]
# creation d'un vecteur qui contiedera les variables de decisions, les ti et les ei ainsi que les bi et bi/cp
vecteur=[]
for i in range (var_nbr):
    vecteur.append(str("x"+str(i+1)))
for i in range (contraintes_nbr):
    vecteur.append(str("e"+str(i+1)))
for i in range(contraintes_nbr):
    vecteur.append(str("t"+str(i+1)))
vecteur.append("bi")
vecteur.append("bi/cp")
for j in range(var_nbr+contraintes_nbr*2+2):
    oneMatrix[0][j]=vecteur[j]
for i in range(1,contraintes_nbr+1):
    oneMatrix[i][var_nbr+contraintes_nbr*2]=zeroMatrix[i][var_nbr+1]
#on declare un vecteur qui contiendera les variables de bases
base=[]
base.append("base")
for i in range(1,contraintes_nbr+1):
    for j in range(var_nbr,var_nbr+contraintes_nbr*2):
        if oneMatrix[i][j]==1:
            base.append(vecteur[j])
base.append("-z")
Z=[]
for j in range(var_nbr+contraintes_nbr,var_nbr+contraintes_nbr*2+1):
    for i in range(1,contraintes_nbr+1):
        if oneMatrix[i][j]==1:
            for p in range(var_nbr+contraintes_nbr):
                oneMatrix[contraintes_nbr+1][p]=oneMatrix[contraintes_nbr+1][p]+oneMatrix[i][p]
            oneMatrix[contraintes_nbr + 1][var_nbr+contraintes_nbr*2] = oneMatrix[contraintes_nbr + 1][var_nbr+contraintes_nbr*2] + oneMatrix[i][var_nbr+contraintes_nbr*2]
   
if mode==1:#maximisation   

    for j in range(len(oneMatrix[0])):
        Z.append(-1*oneMatrix[contraintes_nbr + 1][j])
for j in range(len(oneMatrix[0])):
    if not oneMatrix[contraintes_nbr+1][j]==0:
        oneMatrix[contraintes_nbr+1][j]=str(Z[j])+"m"
for j in range(var_nbr):
    oneMatrix[contraintes_nbr+1][j] = oneMatrix[contraintes_nbr+1][j]+"+("+str(zeroMatrix[0][j])+")"
column=0
if mode==2:#minimization
    for j in range(len(oneMatrix[0])):
        Z.append(oneMatrix[contraintes_nbr + 1][j])

if mode==1: #maximisation
    for i in range(var_nbr+contraintes_nbr+1):
        if Z[i]==min(Z) and min(Z)<0 :
            column=i
            break
if mode==2: #minimisation
    for i in range(var_nbr+contraintes_nbr+1):
        if Z[i]==max(Z) and max(Z)>0 :
            column=i
            break          
#bi/cp
for i in range(1,contraintes_nbr+1):
    if not oneMatrix[i][column]==0:
        oneMatrix[i][var_nbr+contraintes_nbr*2+1]=oneMatrix[i][var_nbr+contraintes_nbr*2]/oneMatrix[i][column]
    else :
        oneMatrix[i][contraintes_nbr * 2 + var_nbr + 1] ="-"
oneMatrix[contraintes_nbr+1][contraintes_nbr*2+var_nbr+1]="*"

for j in range(var_nbr,var_nbr+contraintes_nbr*2):
    nb = 0
    for i in range(1, contraintes_nbr+1):
        if oneMatrix[i][j]==0:
            nb+=1
    if nb>=contraintes_nbr:
        for i in range (contraintes_nbr+2):
            oneMatrix[i].pop(j)
matrix=[]
scp=-1
for j in range(len(oneMatrix[i])):
    scp=-1
    for i in range(contraintes_nbr + 2):
        if len(str(oneMatrix[i][j]))>scp:
            scp=len(str(oneMatrix[i][j]))
    matrix.append(scp)

#affichage
print("*"*16," Affichage ","*"*16 )
print()
print("____K=0____\n")
print("les variables de bases\n")
for i in range (contraintes_nbr+2):
    print(" ",base[i],end=" "*(4-len(str(base[i])))+"| ")
    for j in range(len(oneMatrix[i])):
        print(oneMatrix[i][j],end=" "*(matrix[j]-len(str(oneMatrix[i][j])))+"|")
    print()
    print("_"*(sum(matrix)+2+3*(contraintes_nbr*2+var_nbr+2)))
    print()

  
         