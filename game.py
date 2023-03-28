import random 
import time

# 프린트 색깔

R = "\033[91m"
B = "\033[94m"
W = "\033[0m"
G = "\033[92m"


# 캐릭터 부모클래스
class Character:
    def __init__(self, name, hp_stat, mp_stat, power_stat, magic_power_stat):  
        self.name = name
        self.hp = 100 + hp_stat
        self.max_hp = 100 + hp_stat
        self.mp = 50 + mp_stat 
        self.power = 10 + power_stat
        self.magic_power = 10 + magic_power_stat

    def character_status(self):
        player_max_hp = self.max_hp
        print(f""" 
        {self.name}의 현재 상태창:{B}
        <HP> {self.hp} / {player_max_hp} {W}
        <MP> {self.mp} 
        <힘> {self.power} 
        <지능> {self.magic_power} """)

    def character_attack(self):
        if char_type == "일반공격":
            critical_attack = random.random() < 0.1 # 10퍼센트 확률로 치명타!
            if critical_attack:
                my_damage = random.randint(self.power - 2, self.power + 2) * 3
                print(f"\n {R}치명타!!{W} {monster.name}에게 {B}{my_damage}의 데미지{W}를 입혔습니다!")
            else:
                my_damage = random.randint(self.power - 2, self.power + 2)
                print(f"\n {self.name}의 {B}일반공격!{W} {monster.name}에게 {B}{my_damage}의 데미지{W}를 입혔습니다!")
        elif char_type == "마법공격":
            critical_attack = random.random() < 0.1 # 10퍼센트 확률로 치명타!
            if critical_attack:
                my_damage = random.randint(self.magic_power, self.magic_power + 6) * 3
                left_mp = max(self.mp - 10, 0)
                self.mp = left_mp
                print(f"\n {R}치명타!!{W} {monster.name}에게 {B}MP 10{W}을 소모해 {B}{my_damage}의 데미지{W}를 입혔습니다!")
            else:
                my_damage = random.randint(self.magic_power, self.magic_power + 6) 
                left_mp = max(self.mp - 10, 0)
                self.mp = left_mp
            # self.mp가 10보다 작으면 마법공격을 사용할 수 없다.
            # 매 마법공격마다 self.mp를 업데이트 한다.
                print(f"\n {self.name}의 {B}마법공격!{W} {monster.name}에게 {B}MP 10{W}을 소모해 {B}{my_damage}의 데미지{W}를 입혔습니다!")
            # 마법공격은 일반공격보다 강하다! 
        monster.hp = max(monster.hp - my_damage, 0) # 0을 붙여줘야 hp가 0 아래로 내려가지 않는다!
        if monster.hp == 0:
            print(f"\n {monster.name}이(가) 쓰러졌습니다. {B}전투 승리!{W}\n")

# 개별 캐릭터(직업별?)

# 몬스터 부모클래스
class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power

    def monster_status(self):
        monster_max_hp = self.max_hp
        print(f""" 
        {self.name}의 현재 상태창: 
        {R}<HP> {self.hp} / {monster_max_hp} {W}
        <힘> {self.power}""")

    def __str__(self): # 이 메소드 안넣으면 object at 0000000 뭐 이런 오류가 난다.
        return self.name
    
    def monster_attack(self):
        monster_damage = random.randint(self.power - 2, self.power + 2)
        player.hp = max(player.hp - monster_damage, 0) # 0을 붙여줘야 hp가 0 아래로 내려가지 않는다!
        print(f"\n {self.name}의 {R}공격! {monster_damage}의 데미지{W}를 입었습니다!")
        if player.hp == 0:
            print(f"\n {player.name}이(가) 쓰러졌습니다. {R}전투 패배...{W}\n")

# 개별몬스터

class Goblin(Monster):
    def __init__(self):
        super().__init__("고블린", 50, 10)
class Imp(Monster):
    def __init__(self):
        super().__init__("임프", 80, 13)      
class Troll(Monster):
    def __init__(self):
        super().__init__("트롤", 100, 15)
class Werewolf (Monster):
    def __init__(self):
        super().__init__("웨어울프", 150, 17)        
class Dragon(Monster):
    def __init__(self):
        super().__init__("드래곤", 200, 30)

monster_list = [Goblin(), Imp(), Troll(), Werewolf(), Dragon()]

def summon_random_monster():
    return random.choice(monster_list)

#--------------------------- 게임 플레이 부분--------------------------------

# 처음 캐릭터 생성

name = input(f"\n 캐릭터 이름을 입력하세요 : ")

input(f"\n 당신의 스탯은 랜덤으로 {G}기본능력치에 추가{W}됩니다. enter를 눌러 운을 시험해보세요. (enter)")
hp_stat = random.randint(1,50)
mp_stat = random.randint(1,20)
power_stat = random.randint(1,20)
magic_power_stat = random.randint(1,15)
player = Character(name, hp_stat, mp_stat, power_stat, magic_power_stat)

print(f"\n HP +{B}{hp_stat}{W} MP +{B}{mp_stat}{W} 힘 +{B}{power_stat}{W} 지능 +{B}{magic_power_stat}{W}")

print(f"\n          {G}합산중...{W}")

time.sleep(0.5)

print(f"\n 새로운 캐릭터 {player.name}이(가) 생성되었습니다.")

player.character_status()

time.sleep(1)

# 콘솔 몬스터 부분

input(f"\n 눈 앞에 몬스터가 나타났습니다! {G}어떤 몬스터일까요?{W} (enter)")

# 몬스터 랜덤 등장(수정 전)

# monsters = [
#     Monster("고블린", 50, 10),
#     Monster("트롤", 100, 15),
#     Monster("드래곤", 200, 20),
# ]
# monster = random.choice(monsters)

# # 몬스터 랜덤 출력

# time.sleep(1)

# if monster == monsters[0]:
#     print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. 약해보입니다.")
# if monster == monsters[1]:
#     print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. 싸우기 적당할 것 같습니다.")
# if monster == monsters[2]:
#     print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. 도망가는 게 어떨까요?")

# monster.monster_status() 

# 몬스터 랜덤 등장(수정 후)
monster = summon_random_monster()

if isinstance(monster, Goblin):
    print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. 약해보입니다.")
if isinstance(monster, Imp):
    print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. {B}날쌔보이네요.{W}")  
if isinstance(monster, Troll):
    print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. {B}싸우기 적당할 것 같습니다.{W}")
if isinstance(monster, Werewolf):
    print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. {R}드래곤보다는 낫습니다.{W}")    
if isinstance(monster, Dragon):
    print(f"\n 당신과 싸울 몬스터는 {monster} 입니다. {R}도망가는 게 어떨까요..{W}")

monster.monster_status()

time.sleep(1)

# 전투
# 내가 먼저 공격
# while문을 쓸 것.

while player.hp > 0 and monster.hp > 0 or active == 2:

    active = input("\n (공격:1 도망가기:2) : ")
    if active == "1":
        char_type = input(f"\n 공격 타입을 선택하세요. \n {R}일반공격은 힘, {B}마법공격은 지능{W}을 기반으로 데미지가 결정됩니다. \n 또한 마법공격은 {G}mp 10{W}을 소모합니다. (1: 일반공격, 2: 마법공격) : ")
        if char_type == "1":
            char_type = "일반공격"
        elif char_type == "2":
            char_type = "마법공격"
            if player.mp < 10:
                print(f"\n {R}MP 부족!{W} 마법공격을 할 수 없습니다!")
                continue
                # mp가 10보다 작으면 while문 시작으로 돌아간다.
        else:
            while True:   
                print("\n 1번과 2번 중에 골라주세요.")
                char_type = input(f"\n 공격 타입을 선택하세요. \n {R}일반공격은 힘, {B}마법공격은 지능{W}을 기반으로 데미지가 결정됩니다. \n 또한 마법공격은 {G}mp 10{W}을 소모합니다. (1: 일반공격, 2: 마법공격) : ")
                if char_type == "1":
                    char_type = "일반공격"
                    break
                elif char_type == "2":
                    char_type = "마법공격"
                    break
        player.character_attack() 
        if monster.hp == 0:
            break
        monster.monster_status() 
        monster.monster_attack()
        if player.hp == 0:
            break
        player.character_status()
    elif active == "2":
        print("\n 당신은 무사히 도망쳤습니다.\n")
        quit()
# player와 monster 둘 다 체력이 0보다 큰 동안만 while문을 반복한다. 즉 하나라도 0과 같거나 작아지면 while문은 종료된다. 
# 공격타입을 잘못 선택하면 제대로 선택할때까지 반복한다.
# 도망가기를 선택하면 역시 종료된다.


# 공격할 때 일반/마법 선택하게 변경 -> clear!
# 마법공격은 공격에 마나를 소모한다.-> clear!
# 몬스터가 쓰러졌는데도 몬스터 공격이 실행되는 문제 -> clear!
# 마나 10 이하면 마법공격 못하게 한다. -> clear!
# 프린트 가독성 높이기 -> clear!
# 몬스터 상속으로 바꾸기 -> clear! 
# 크리티컬 : 10% 확률로 3배 데미지! -> clear!

# 끝