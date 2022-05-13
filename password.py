liste = open("motdepasse.txt","r")
import threading
import random
import time

start = time.time()
motdepasse =[]

while len(motdepasse) != 10:
    def sortie1():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue
                
                
    def sortie2():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue                       
                
    def sortie3():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue

    def sortie4():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                pass

    def sortie5():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue

                
    def sortie6():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)            
            else :
                continue

    def sortie7():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue

    def sortie8():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue                
                
    def sortie9():
        for i in random.choice(liste):
            if i not in motdepasse:
                motdepasse.append(i)
            else :
                continue

    def sortie10():
        for i in random.choice(liste):
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



sortie1.start()
sortie2.start()
sortie3.start()
sortie4.start()
sortie5.start()
sortie6.start()
sortie7.start()
sortie8.start()
sortie9.start()
sortie10.start()



sortie1.join()
sortie2.join()
sortie3.join()
sortie4.join()
sortie5.join()
sortie6.join()
sortie7.join()
sortie8.join()
sortie9.join()
sortie10.join()

end = time.time()
    
print(end-start)