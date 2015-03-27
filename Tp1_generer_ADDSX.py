import math
def genereADDS1():
 """ Cette fonction génere ADDS1 dans le fichier ADDS1.py dans le répertoire
courrant.
 """
 of = open("ADDS1.py", "w")
 print( 'def ADDS1(a, b):', file=of )
 for i in range(10):                    #i=a dans (a,b)
     for j in range(10):                #j=b dans (a,b)
         (r,c)=divmod(i+j,10)           #reste r =(a+b)mod10, derniere 
                                        #chiffre c=(a+b)//10
         print("    if(a=='"+str(i)+"' and b=='"+str(j)+"'):",file=of)
         print("        return ('"+str(c)+"','"+str(r)+"')",file=of)
        

 print("    raise ValueError('unknown digits in ADDS1')", file=of)
 of.flush

def genereADDS2():
 """ Cette fonction génere ADDS2 dans le fichier ADDS2.py dans le répertoire
courrant.
 """
 of = open("ADDS2.py", "w")
 print( 'def ADDS2(a, b):', file=of )
 for i in range(10):                            #i=a dans (a,b)
     print("    if(a=='"+str(i)+"'):",file=of)
     for j in range(10):                        #j=b dans (a,b)
         (r,c)=divmod(i+j,10)                   #reste r =(a+b)mod10, derniere
                                                #chiffre c=(a+b)//10         
         print("        if(b=='"+str(j)+"'):",file=of)
         print("            return ('"+str(c)+"','"+str(r)+"')",file=of)
 print("    raise ValueError('unknown digits in ADDS2')", file=of)
 of.flush

def genereADDS3():
 """ Cette fonction génere ADDS3 dans le fichier ADDS3.py dans le répertoire
courrant.
"""
 of = open("ADDS3.py", "w")
 print( 'def ADDS3(a, b):', file=of )
 data=[i for i in range(10)]
 binarymap(data, 0,9, of)                                           #Esquisse un arbre binaire de 1 à 9 pour 'a' 
 print("    raise ValueError('unknown digits in ADDS3')",file=of)   #où a chaque feuille on ajoute un autre arbre 
 of.flush                                                           #de 1 à 9 pour 'b'

def binarymap(A,lower, upper,f,a=0,st='if',let='a',indentation="    "): #A:tableaux a mapper en binaire, lower:debut du tableaux,
                                                                        #upper: fin du tableaux, f:fichier de destination
                                                                        #a: valeur de a dans (a,b), st:prendre valeur 'if' si une
                                                                        #feuille est à gauche ou 'elif' si elle est a droite,
                                                                        #let: trace du boucle qui prendre valeur 'a' quand on est
                                                                        #dans l'arbre de a où quand on est dans l'arbre b,
                                                                        #indentation
    espace='    '
    middle=math.floor((lower+upper)/2) #calul d'un nouveau node de l'arbre binaire
    if lower!=upper:
        print(indentation+st+" ("+let+"<= '"+str(middle)+"'):",file=f)
        binarymap(A,lower, middle,f,a,'if',let,indentation+espace) #Esquisse un arbre pour la partie à gauche du tableaux A initiale
        if let=='a':
            #Arbre binaire de b
            if middle!=a: # si un node est différent de a (une feuille de a à droite)
                a=middle 
                indentation+=espace #on ajoute une indentation
                binarymap(A,0, 9,f,a,'if','b',indentation+espace) #Esquisse un arbre binaire dans une feuille à gauche
                indentation=indentation[:len(indentation)-4]
            else: #si un node est égal à a (une feuille de a à gauche)
                binarymap(A,0, 9,f,a,'if','b',indentation+espace) #Esquisse un arbre binaire dans une feuille à gauche
            
        if middle!=a or let=='b':   #si b!=a
            indentation+=espace     #on ajoute un indentation
            #Calcul de a+b
            (r,c)=divmod(a+middle,10)
            print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(a)+"',b='"+str(middle)+"')",file=f)
            indentation=indentation[:len(indentation)-4]
        elif middle==a and let=='b': #si b=a et feuille de b
            (r,c)=divmod(a+middle,10)
            print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(a)+"',b='"+str(middle)+"')",file=f)
 
        if upper-middle<2: #si il n'y a plus de nodes entre upper et middle
            print(indentation+"else:",file=f) #on print else
        binarymap(A,middle+1,upper,f,a,'elif',let,indentation) #Esquisse un arbre binaire dans une feuille à droite
        
    elif middle==9: #fin de l'arbre et de la recurrence
        if let=='a':
            a=middle
            binarymap(A,0, 9,f,a,'if','b',indentation+espace)#arbre binaire de b dans la derniere feuille de a
        (r,c)=divmod(a+middle,10)
        print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(a)+"',b='"+str(middle)+"')",file=f)

genereADDS1()
genereADDS2()
genereADDS3()

def genereADDS1Var():
 """ Cette fonction génere ADDS1Var dans le fichier ADDS1Var.py dans le répertoire
courrant.
 """
 of = open("ADDS1Var.py", "w")
 dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    #parcours de toustes les bases de 2 à 16
 for base in range(2,17):
     print( 'def ADDS1B'+str(base)+'(a, b):',file=of)
     for i in range(base):      #iteration de taille 'base' pour a
         if i in dic:           #evalue si la valeur de a est dans dic
             a=dic[i]           #et prendre le character associé
         else:
             a=i                #sinon il prendre la valeur de i
         for j in range(base):  #iteration de taille 'base' pour b
             if j in dic:       #evalue si la valeur de b est dans dic
                 b=dic[j]       #et prendre le character associé
             else:
                 b=j            #sinon il prendre la valeur de j
             (r,c)=divmod(i+j,base) #calcul de a+b
             if r in dic:
                 r=dic[r]       #change a et/ou b s'ils sont dans dic
             if c in dic:
                 c=dic[c]
             print("    if(a=='"+str(a)+"' and b=='"+str(b)+"'):",file=of)
             print("        return ('"+str(c)+"','"+str(r)+"')",file=of)
     print("    raise ValueError('unknown digits in ADDS1B"+str(base)+"')",file=of)
 of.flush

def genereADDS2Var():
 """ Cette fonction génere ADDS2Var dans le fichier ADDS2Var.py dans le répertoire
courrant.
 """
 of = open("ADDS2Var.py", "w")
 dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    #parcours de toutes les bases de 2 à 16
 for base in range(2,17):
     print( 'def ADDS2B'+str(base)+'(a, b):',file=of )
     for i in range(base):              #iteration de taille 'base' pour a
         if i in dic:                   #evalue si la valeur de a est dans dic
                 a=dic[i]               #et prendre le character associé
         else:
             a=i                        #sinon il prendre la valeur de i
         print("    if(a=='"+str(a)+"'):",file=of)
         for j in range(base):          #iteration de taille 'base' pour b
             if j in dic:               #evalue si la valeur de b est dans dic
                     b=dic[j]           #et prendre le character associé
             else:
                 b=j                    #sinon il prendre la valeur de j
             (r,c)=divmod(i+j,base)
             if r in dic:
                 r=dic[r]               #change a et/ou b s'ils sont dans dic
             if c in dic:
                 c=dic[c]
             print("        if(b=='"+str(b)+"'):",file=of)
             print("            return ('"+str(c)+"','"+str(r)+"')",file=of)
     print("    raise ValueError('unknown digits in ADDS2B"+str(base)+"')",file=of)
 of.flush

 
def genereADDS3Var():
 """ Cette fonction génere ADDS3Var dans le fichier ADDS3Var.py dans le répertoire
courrant.
"""
 of = open("ADDS3Var.py", "w")
 #parcours de toutes les bases de 2 à 16
 for base in range(2,17):
     print( 'def ADDS3B'+str(base)+'(a, b):', file=of )
     data=[i for i in range(base)] #crée des tableaux de taille 'base'
     binarymap(data, 0,base-1, of,base) #esquisse des arbres binaires de taille 'base'
     print("    raise ValueError('unknown digits in ADDS3b"+str(base)+"')",file=of)
 of.flush

def binarymap(A,lower, upper,f,base,a=0,st='if',let='a',indentation="    "):
    dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    espace='    '
    middle=math.floor((lower+upper)/2)
    if lower!=upper:
        print(indentation+st+" ("+let+"<= '"+str(middle)+"'):", file=f)
        binarymap(A,lower, middle,f,base,a,'if',let,indentation+espace)
        if let=='a':
            if middle!=a:
                a=middle
                indentation+=espace
                binarymap(A,0, base-1,f,base,a,'if','b',indentation+espace)
                indentation=indentation[:len(indentation)-4]
            else:
                binarymap(A,0, base-1,f,base,a,'if','b',indentation+espace)
            
        if middle!=a or let=='b':
            indentation+=espace
            if a in dic:
                at=dic[a]
            else:
                at=a
            if middle in dic:
                b=dic[middle]
            else:
                b=middle
            (r,c)=divmod(a+middle,base)
            if r in dic:
                 r=dic[r]
            if c in dic:
                 c=dic[c]
            print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(at)+"',b='"+str(middle)+"')", file=f)
            indentation=indentation[:len(indentation)-4]
        elif middle==a and let=='b':
            if a in dic:
                at=dic[a]
            else:
                at=a
            if middle in dic:
                b=dic[middle]
            else:
                b=middle
            (r,c)=divmod(a+middle,base)
            if r in dic:
                 r=dic[r]
            if c in dic:
                 c=dic[c]
            print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(at)+"',b='"+str(middle)+"')", file=f)
 
        if upper-middle<2:
            print(indentation+"else:", file=f)
        binarymap(A,middle+1,upper,f,base,a,'elif',let,indentation)
        
    elif middle==(base-1):
        if let=='a':
            a=middle
            binarymap(A,0, base-1,f,base,a,'if','b',indentation+espace)
        if a in dic:
                at=dic[a]
        else:
            at=a
        if middle in dic:
            b=dic[middle]
        else:
            b=middle
        (r,c)=divmod(a+middle,base)
        if r in dic:
             r=dic[r]
        if c in dic:
             c=dic[c]
        print(indentation+"    return ('"+str(c)+"','"+str(r)+"') #(a='"+str(at)+"',b='"+str(middle)+"')", file=f)


genereADDS1Var()
genereADDS2Var()
genereADDS3Var()
