import random
class enemy():
    def __init__(self):
        self.hayat = True
        self.health = random.randint(10,50)
        self.damage = random.randint(10,50)
        self.kalkan = random.randint(1,10)
    def vur(self,player):
        eksilen = self.damage - player.kalkan
        player.health -= eksilen
        if player.health <= 0:
            player.hayat = False
            print("Game Over")
        else:
            pass

class player():
    def __init__(self):
        self.hayat = True
        self.health = 500
        self.damage = 30
        self.kalkan = 20
    def vur(self,enemy):
        eksilen = ali.damage - enemy.kalkan
        enemy.health -= eksilen
        if enemy.health <= 0:
            enemy.hayat = False
            az.remove(enemy)
        else:
            pass
az = list()
ali = player()
for i in range(10):
    az.append(enemy())

while True:
    print("Player: can:{} güç:{} kalkan:{}".format(ali.health,ali.damage,ali.kalkan))
    for i in az:
        print("{}. düşman >>> canı:{} gücü:{}  kalkanı:{}".format(az.index(i), i.health, i.damage, i.kalkan))

    sec = int(input("Düşman seç: "))
    player.vur(ali,az[sec])
    saldiran = random.randint(0,9)
    enemy.vur(az[2],ali)
    print("Düşmanın kalan canı:{}".format(az[sec].health))

