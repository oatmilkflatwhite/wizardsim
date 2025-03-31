import random
import time

character = ("      ","The Princess: ","Boblin the Goblin: ","Danny Devil:" ,"Terry Tree-man: ","The D-Dragon: ")
start_dia = ("Long, long, ago... In a place far, far, away... Was someone who wielded great magic.","You are a brave wizard embarking on a quest to retrieve the Princess.")
prin_bend = ("")
tab = "     "
mpoints = 2
hpoints = 50
qspeed = 0.4
nspeed = 0.8
lspeed = 1.2


def wprint(y,x,s): #y is character x is str or tuple/list s is seconds y=str x=str s=flt
    if isinstance(x,str) == True:
        print(x)
        time.sleep(s)
    else:
        for i in x:
            print(y.upper() + i)
            time.sleep(s)

def visgap(x):
    gaps = []
    if len(x) == 10:
        return x
    elif len(x) < 10:
        gaps.append(x)
        gapno = 10 - len(x)
        for i in range(gapno):
            j = " "
            gaps.append(j)
        l = "".join(gaps)
        return l
    else:
        print("Something's gone deepy wrong here.")    
        

def showpoints():
    healthpoints = []
    brix = int(hpoints/5) + (hpoints % 5 > 0)
    jumbo = round(brix)
    for j in range(jumbo):
        q = "—"
        healthpoints.append(q)
    j = "".join(healthpoints)
    points = []
    for i in range(mpoints):
        u = "*"
        points.append(u)
    p = "".join(points)
    bingo = visgap(j)
    bongo = visgap(p)
    print("Your Health: " + str(hpoints) + tab + "Magic Points: " + str(mpoints))
    print(bingo + tab + tab + bongo)

class Gun():
    def __init__(self,name,dam,damtype,bul,mag,amo):
        self.name = name
        self.dam = dam
        self.damtype = damtype
        self.bul = bul
        self.mag = mag
        self.amo = amo

    def shoot(self):
        if self.bul > 7 :
            b = random.randint(2,7)
            self.bul = self.bul - b
            damage = b*self.dam + random.randint(1,4)
            return [damage, self.damtype,b]
        elif self.bul == 0:
            self.amo = self.amo - self.mag
            print("Out of bullets... You have reloaded the " + self.name + ".")
            self.bul = self.mag
            return[0, 0, 0]
        else:
            b = self.bul
            self.bul = 0
            damage = b*self.dam
            damage = b*self.dam
            return [damage, self.damtype,b]



class Spell():
    def __init__(self,name,dnum,dtype,damtype,cost):
        self.name = name
        self.dnum = dnum
        self.dtype = dtype
        self.damtype = damtype
        self.cost = cost

    def cast(self):
         global mpoints
         die = []
         while len(die) < self.dnum:
            x = random.randint(1,self.dtype)
            die.append(x)
         print("Output: " + str(die))
         y = sum(die)
         mpoints = mpoints - self.cost
         return [y, self.damtype]
class Enemy:
    def __init__(self,name,hp,wkns,res,cphra):
        self.name = name
        self.hp = hp
        self.wkns = wkns
        self.res = res
        self.cphra = cphra
    def showhp(self):
        health = []
        brix = int(self.hp/5) + (self.hp % 5 > 0)
        jumbo = round(brix)
        for j in range(jumbo):
            q = "—"
            health.append(q)
        j = "".join(health)
        print(f"{self.name}'s Health: " + str(self.hp))
        print(j)

def dmgtext(u):
    print(str(u[0]) + " " + u[1] + " damage.")

def isalive(x):
    if hpoints <= 0:
        print("You have died...")
        return False
    elif x.hp <= 0:
        print(x.name + " has died!")
        return False
    else:
        return True


def attack(y,x): #y is spell, x is whos getting maimed
        if isinstance(y, Spell):
            print("You used " + y.name + " on " + x.name + "!") ### checking for magic points happens at this point
            global mpoints
            cost = y.cost
            if mpoints >= cost:
                u = y.cast()
                if u[1] == x.wkns:
                    dmg = u[0]*2
                    x.hp = x.hp - dmg
                    print(x.name + " took " + str(dmg) + " points of " + u[1] + " damage from a weakness to it!")
                elif u[1] == x.res:
                    dmg = u[0]*0.5
                    x.hp = x.hp - dmg
                    print(x.name + " resists " + u[1] + " damage, and took " + str(int(dmg)) + " points of damage.")
                else:
                    dmg = u[0]
                    x.hp = x.hp - dmg
                    print(x.name + " took " + str(dmg) + " points of " + u[1] + " damage.")
            else: 
                print("A measly burst of magic fizzled out from your staff instead... " + y.name + " couldn't be cast!")
        else:
            j = y.shoot()
            if j[1] !=0:
                print("You shot %s with the %s for a total of %d times." % (x.name,y.name,j[2]))
                if j[1] == x.wkns:
                    dmg = j[0]*2
                    x.hp = x.hp - dmg
                    print(x.name + " took " + str(dmg) + " points of " + j[1] + " damage from a weakness to it!")
                elif j[1] == x.res:
                    dmg = j[0]*0.5
                    x.hp = x.hp - dmg
                    print(x.name + " resists " + j[1] + " damage, and took " + str(int(dmg)) + " points of damage.")
                else:
                    dmg = j[0]
                    x.hp = x.hp - dmg
                    print(x.name + " took " + str(dmg) + " points of " + j[1] + " damage.")
            else:
                print("You spent the turn reloading your weapon.")

        
fbl = Spell("Fireball",8,6,"FIRE",2)
lgt = Spell("Lightning Bolt",8,6,"LIGHTNING",2)
clo = Spell("Clobber",1,4,"PHYSICAL",0)
gun_bfs = Gun("Beretta 92 FS",7,"PHYSICAL",10,10,30)

# idea of a weakness quote, res quote, lose quote. 
bob = Enemy("Boblin the Goblin",100,"PHYSICAL","None","I'm a menace to society!")
dev = Enemy("Danny Devil",140,"None","FIRE","Hee-hee! I'm gonna make people do sin!")
tre = Enemy("Terry Tree-man",40,"FIRE","LIGHTNING","I'm going to suck the life out of the earth!")
 
fighting = True
while fighting == True:
    e = bob
    showpoints()
    e.showhp()
    attack(clo,e)
    fighting = isalive(e)

