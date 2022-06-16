import math
import os

import misc
import random
from main import fight_screen, damage, dialog_screen, dialog_screen_sp, path
from collections import Counter


def loot():
    l = misc.loot_arr[random.randint(0, len(misc.loot_arr) - 1)]
    return l


def enemy():
    e = misc.enemy_arr[random.randint(0, len(misc.enemy_arr) - 1)]
    return e


def trap():
    t = misc.trap_arr[random.randint(0, len(misc.trap_arr) - 1)]
    return t


def inv(inv):
    return inv[0][0], inv[0][1], inv[1][0], inv[1][1], inv[2][0], inv[2][1], inv[3][0], inv[3][1], inv[4][0], inv[4][1]


def event():
    a = random.randint(0, 2)
    if a == 0:
        return loot()
    if a == 1:
        return enemy()
    else:
        return trap()


def fight(enemy, stats, mx):
    e = list(enemy)
    print(fight_screen % (e[0], e[2], e[3], stats[0], stats[2], stats[4][0], stats[3]))
    attacker = [e, stats][random.randint(0, 1)]
    if attacker == e:
        defender = stats
    else:
        defender = e
    print("%s бьёт первый!" % attacker[0])
    while attacker[2] > 0 and defender[2] > 0:
        defender[2] += attacker[3]
        print("%s бьёт %s!" % (attacker[0], defender[0]))
        print(damage % (defender[0], attacker[3], defender[2], mx))
        chs = input("_Нажмите Enter, чтобы продолжить_")
        attacker[2] += defender[3]
        print("%s бьёт %s!" % (defender[0], attacker[0]))
        print(damage % (attacker[0], defender[3], attacker[2], mx))
        chs = input("_Нажмите Enter, чтобы продолжить_")
    if attacker[0] != e[0] and attacker[2] <= 0.0:
        return "L", defender
    elif defender[0] != e[0] and defender[2] <= 0.0:
        return "L", defender
    elif attacker[0] == e[0] and attacker[2] <= 0.0:
        return "W", defender
    else:
        return "W", attacker


def loc_count(n, m):
    if not m:
        m.append([str(n), 1])
    elif m[-1][0] == str(n):
        m[-1][1] += 1
    elif m[-1][0] != str(n):
        m.append([str(n), 1])
    return m


def map_f(m):
    m1 = Counter(m[:-1])
    c_1 = m1["1"]
    c_3 = m1["3"]
    n = 0
    new_line = 0
    if c_3 == 0:
        for i in range(len(m)):
            if new_line == 1:
                print(" " * n + "[%s]" % m[i], end="")
            else:
                print("[%s]" % m[i], end="")
            if i == len(m) - 1:
                break
            if m[i] != "2":
                new_line = 0
                print("—", end="")
                n += 4
            else:
                new_line = 1
                print("\n", end="")
                print(" " * n + " |\n", end="")
    else:
        l = abs((c_3 - c_1) * 4)
        n = l
        k = 0
        new_line = 1
        for i in range(len(m)):
            if i + k == len(m) - 1:
                break
            if m[i + k] != "3":
                if new_line == 0:
                    print("[%s]" % m[i + k], end="")
                else:
                    print(" " * n + "[%s]" % m[i + k], end="")
            if m[i + k] == "2":
                new_line = 1
                print("\n", end="")
                print(" " * n + " |\n", end="")
            elif m[i + k] == "1":
                new_line = 0
                print("—", end="")
                n += 4
            elif m[i + k] == "3":
                new_line = 1
                k += 1
                t = 1
                while m[i + k] == "3":
                    if i + k == len(m) - 1:
                        break
                    k += 1
                    t += 1
                n -= 4 * t
                if i + k == len(m) - 1:
                    print(" " * n + "[*]" + t * "-[3]")
                    break
                else:
                    print(" " * n + "[2]" + t * "—[3]")
                    print(" " * n + " |")


def save(p, m, i, n, x, lvl):
    global ds
    if n == None:
        s_name = input("Имя сохранения - ")
        f_s = open(path + "/%s" % s_name, "w", encoding="UTF-8")
        for j in (p, i, m, x, lvl):
            # f_s.write(str(j) + "\n")
            if j is iter:
                for l in j:
                    f_s.write(str(l) + ";")
            else:
                f_s.write(str(j)+";")
            f_s.write("\n")
        print("Сохранение успешно выполнено!")
        f_s.close()
        ds = dialog_screen_sp
    else:
        s_name = n
        f_s = open(path + "/%s" % n, "w", encoding="UTF-8")
        for j in (p, i, m, x, lvl):
            if j is iter:
                for l in j:
                    f_s.write(str(l) + ";")
            else:
                f_s.write(str(j) + ";")
            f_s.write("\n")
        print("Данные успешно перезаписаны!")
        f_s.close()
    return s_name


def convert(n, b:bool):
    n = n[:-2].split(";")
    if b:
        flag = True
        m = []
        n = n[0][1:-1]
        while flag:
            if n[0] == "(":
                l = n.find("(")
                r = n.find(")")
                if l - 1 < 0 and r + 2 <= len(n) - 1:
                    m.append(convert_tuple(n[l:r + 1]))
                    n = n[r + 3:]
                elif l - 1 > 0 and r + 2 > len(n) - 1:
                    m.append(convert_tuple(n[l:r + 1]))
                    n = n[:l - 2]
                elif l - 1 < 0 and r + 2 > len(a) - 1:
                    m.append(convert_tuple(n[l:r + 1]))
                    n = ''
                    flag = False
                else:
                    m.append(convert_tuple(n[l:r + 1]))
                    n = n[:l - 1] + n[r + 2:]
            if n[0] == "[":
                l = n.find("[")
                r = n.find("]")
                if l - 1 < 0 and r + 2 <= len(n) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[r + 3:]
                elif l - 1 > 0 and r + 2 > len(n) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[:l - 2]
                elif l - 1 < 0 and r + 2 > len(a) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = ''
                    flag = False
                else:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[:l - 1] + n[r + 2:]
            if n[0] == "'" and ", " in n:
                a = n.replace("'", "", 2).split(", ", 1)
                n = a[1]
                m.append(a[0])
            elif ", " in n:
                a = n.split(", ", 1)
                n = a[1]
                m.append(a[0])
            if ", " not in n and flag:
                flag = False
                if "'" in n:
                    m.append(n.replace("'", ""))
                else:
                    m.append(n)
                n = ''
        del a
        return m
    return n

def convert_tuple(n):
    t = tuple(n[1:-1].replace("'", "").split(", "))
    return t


def convert_list(n):
    t = list(n[1:-1].replace("'", "").split(", "))
    return t


def lvl(n):
    if n < 1:
        return "------------<Error>------------"
    if n == 1:
        return 10
    # k = 1.25 + (n // 10)*0.05
    k = 1.25
    return math.ceil(lvl(n-1)*k)


def upgrade_hp(l):
    if l < 1:
        return "------------<Error>------------"
    if l == 2:
        return 2
    return upgrade_hp(l-1)+2




ds = dialog_screen
