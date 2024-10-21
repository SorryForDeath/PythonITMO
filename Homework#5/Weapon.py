import random
import time

class Weapon:
    def __init__(self, clip_capasity=None, type_of_weapon=None, range_of_weapon=None, damage=None):
        self.type_of_weapon = type_of_weapon
        self.range_of_weapon = range_of_weapon
        self.damage = damage
        self.clip_capasity = [clip_capasity, clip_capasity] #Первое поле - текущее кол-во патронов, второе - тотальное значение
        self.number_of_shots = 100
    def fire(self):
        if self.clip_capasity[0] == 0:
            print('No more bullets Need reload!')
            return
        if self.clip_capasity[0] < self.number_of_shots:
            clip_capacity = self.clip_capasity[0]
            self.clip_capasity[0] = 0
            return [self.damage] * clip_capacity
        self.clip_capasity[0] -= self.number_of_shots
        return [self.damage] * self.number_of_shots

    def reload(self):
        print('Reload is in progress...')
        time.sleep(3)
        print('Reload is completed')
        self.clip_capasity[0] = self.clip_capasity[1]

class Assault_Rifle(Weapon):
    def __init__(self):
        super().__init__('20-40','assault rifle', '100-400', '16-24')

class Sniper_Rifle(Weapon):
    def __init__(self):
        super().__init__('1-10','sniper rifle', '1000-2000', '70-150')


class Shotgun(Weapon):
    def __init__(self):
        super().__init__('2-8', 'shotgun', '20-80', '70-150')

class M416(Assault_Rifle):
    def __init__(self):
        super().__init__()
        self.clip_capasity = [30, 30]
        self.range_of_weapon = 200
        self.damage = 18
        self.number_of_shots = 10

    def fire(self):
        if self.clip_capasity[0] == 0:
            print('Click, click')
        else:
            print("Tratata\n10 shots were fired")
        return super().fire()

class AWM(Sniper_Rifle):
    def __init__(self):
        super().__init__()
        self.clip_capasity = [5, 5]
        self.range_of_weapon = 2000
        self.damage = 140
        self.number_of_shots = 1

    def fire(self):
        if self.clip_capasity[0] == 0:
            print('Click, click')
        else:
            print("Booooom\n1 shot were fired")
        return super().fire()

class Saiga(Shotgun):
    def __init__(self):
        super().__init__()
        self.clip_capasity = [8, 8]
        self.range_of_weapon = 50
        self.damage = 80
        self.number_of_shots = 2

    def fire(self):
        if self.clip_capasity[0] == 0:
            print('Click, click')
        else:
            print("Boom Phhh Bruuuhh\n2 shots were fired")
        return super().fire()

class Soldier:
    __n_aim = 0
    __e_aim = 0
    def __init__(self, specific=None, experience=None):
        self.specific = specific
        self.experience = experience

    def reload(self, gun):
        gun.reload()

    def aim(self):
        self.__n_aim += 1
        match self.__n_aim:
            case 1:
                print("'Ты посмотрел через прицел'")
            case 2:
                print("'Твое дыхание замедлилось'")
            case 3:
                print("'Ты и оружие есть одно целое'")
            case 4:
                print("Ты слишком долго целишься! Дыхание сбилось, эффект потерян!")
                self.__e_aim = 0
                self.__n_aim = 0
                return
        self.__e_aim += 5

    def fire(self, gun, target):
        chance_to_hit = 50 + self.__e_aim
        self.__e_aim = 0
        self.__n_aim = 0
        if self.specific == gun.type_of_weapon:
            chance_to_hit += 25
        else:
            chance_to_hit -= 15
        match self.experience:
            case 0:
                chance_to_hit -= 15
            case 1:
                pass
            case 2:
                chance_to_hit += 15
            case 3:
                chance_to_hit += 25
        if target.range_from_enemy > gun.range_of_weapon + round(gun.range_of_weapon / 3):
            chance_to_hit /= chance_to_hit
        health = target.healthPoints
        try:
            for i in gun.fire():
                temp = random.randrange(0, 100)
                if chance_to_hit >= temp:
                    print(f'Hit! Damage done: {gun.damage}')
                    health -= i
                else:
                    print("Miss!")
        except:
            pass
        target.healthPoints = health
        if health <= 0:
            print("Target eliminated")
        else:
            print(f"Target is alive. Target's current HP is {health}")

class Target(Soldier):
    __alive = True
    def __init__(self, healthPoints, range_from_enemy):
        super().__init__(healthPoints)
        self.range_from_enemy = range_from_enemy
        self.healthPoints = healthPoints

    def Dead(self):
        if self.healthPoints <= 0:
            self.__alive = False
        return not self.__alive


soldier_list = []
print("Добро пожаловать в симулятор стрелкового полигона. Здесь из вас, сопляков, сделают настоящих бравых солдат!")
print("Для начала придется пройти обучение. Оно обязательно! Скипнуть не получится!")
print("Что ж, приступим для начала выбери оружие\n1 - AWM\n2 - M416\n3 - Saiga")
started_soldier = Soldier()
soldier_list.append(started_soldier)
while True:
    match input():
        case '1':
            print("Снайперка! Отличный выбор, посмотрим, на что ты способен на расстоянии")
            started_gun = AWM()
            break
        case '2':
            print("Штурмовая винтовка? Предпочитаешь универсальность, а, салага?")
            started_gun = M416()
            break
        case '3':
            print("Дробовик? Странный выбор, конечно, но кто я такой, чтобы осуждать такое")
            started_gun = Saiga()
            break
        case _:
            print("Боже мой, неужели ты настолько ничтожен, что не справился с первым же заданием. Пробуй еще раз!")

print("Отлично, идем дальше. Видишь ту мишень в конце полигона? Хорошенько прицелься и порази ее!")
started_target = Target(1, 100000)
print("1 - Выстрелить\n2 - Прицелиться")
flag = True
flag2 = True
while flag2:
    match input():
        case '1':
            started_soldier.fire(started_gun, started_target)
            if started_target.Dead():
                print("Чтоооо? Да ты не так прост, как кажешься! Отличный результат, солдат, так держать!")
                break
            print("Что ж, я так и думал, что вас в этих военных академиях ничему не учат. Попробуй еще раз")
            if started_gun.clip_capasity[0] == 0:
                if flag:
                    flag = False
                    continue
                print("Кажется, патроны кончились, перезарядись")
                while True:
                    if  input('1 - Перезарядиться\n') == '1':
                        started_soldier.reload(started_gun)
                        flag2 = False
                        print("Отлично, хоть с этим ты справился.\n"
                              "А теперь снеси эту мишень. Специально для такого доходяги, как ты, ее поставили почти у тебя под носом")
                        break
                    else:
                        print("Мда уж, что с тобой? Смени уже этот магазин")

        case '2':
            started_target.aim()
        case _:
            print("Ты что это делаешь, солдат?! Ну-ка сосредоточься!")
started_target.range_from_enemy = started_gun.range_of_weapon
while not started_target.Dead():
    print("1 - Выстрелить\n2 - Прицелиться\n3 - Перезарядиться")
    match input():
        case '1':
            started_soldier.fire(started_gun, started_target)
        case '2':
            started_target.aim()
        case '3':
            started_soldier.reload(started_gun)
        case _:
            print("Ты что это делаешь, солдат?! Ну-ка сосредоточься!")

print("Отлично, солдат! Ты закончил обучение!")