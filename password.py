import time
import random
import threading
liste = open("password_list.txt", "r")
print (liste.read())
#liste.close()
start = time.time()
motdepasse = []
motdepasse.append(liste.read())




def sortie1():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else:
            continue


def sortie2():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else:
            continue


def sortie3():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else:
            continue


def sortie4():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else:
            pass

def sortie5():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else :
            continue

                
def sortie6():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)            
        else :
            continue

def sortie7():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else :
            continue

def sortie8():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else :
            continue                
                
def sortie9():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else :
            continue

def sortie10():
    for i in random.choice(liste.read()):
        if i not in motdepasse:
            motdepasse.append(i)
        else :
            continue            
            
action1 =threading.Thread(target=sortie1)
action2 =threading.Thread(target=sortie2)
action3 =threading.Thread(target=sortie3)
action4 =threading.Thread(target=sortie4)
action5 =threading.Thread(target=sortie5)
action6 =threading.Thread(target=sortie6)
action7 =threading.Thread(target=sortie7)
action8 =threading.Thread(target=sortie8)
action9 =threading.Thread(target=sortie9)
action10=threading.Thread(target=sortie10)



action1.start()
action2.start()
action3.start()
action4.start()
action5.start()
action6.start()
action7.start()
action8.start()
action9.start()
action10.start()



action1.join()
action2.join()
action3.join()
action4.join()
action5.join()
action6.join()
action7.join()
action8.join()
action9.join()
action10.join()

liste.close()

end = time.time()
print(end-start)