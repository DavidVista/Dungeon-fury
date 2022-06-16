import gen
import main

f_save = main.save
hp = 3
max_hp = 3
inv = [["<>", "None"], ["<>", "None"], ["<>", "None"], ["<>", "None"], ["<>", "None"]]
wp = ("кулаки", "weapon", -0.25)
k_r = 0
map_d = []
map_l = []
xp = 0
xp_max = xp
lvl = 0
n_lvl = gen.lvl(lvl + 1)
ds = main.dialog_screen
s_name = None

player = [main.pl_name, "player", hp, wp[2], wp, xp, lvl]

if main.save is not None:
    s_name = f_save
    file = open(main.path + "/" + f_save, encoding="UTF-8")
    player = gen.convert(file.readline(), True)
    player[2], player[3], player[5], player[6] = float(player[2]), float(player[3]), int(player[5]), int(player[6])
    inv = gen.convert(file.readline(), True)
    map_d = file.readline().split(";")[0][1:-1].replace("'", "").split(", ")
    max_hp = int(file.readline().split(";")[0])
    xp_max = int(file.readline().split(";")[0])
    hp, wp = player[2], player[4]
c = ""

chs = input(ds)

while player[2] >= 0 or chs != "3":
    if chs == "2":
        print(main.inventory % (gen.inv(inv)))
        in_chs = input(main.inventory_chs)
        while in_chs != "3":
            if in_chs == "1":
                in_in_chs = input("Предмет под номером: ")
                index = int(in_in_chs) - 1
                item = inv[index]
                print(main.item % (in_in_chs, item[0], item[1]))
                in_in_chs = input()
                if in_in_chs == "1":
                    if item[1] == "weapon":
                        if player[4][0] != "кулаки":
                            inv[index] = player[4]
                            print("*%s был/-а добавлен/-а в инвентарь*\n", player[4][0])
                        else:
                            inv[index] = ["<>", "None"]
                        print("*Оружие %s сменилось на %s*\n" % (player[4][0], item[0]))
                        player[3] = item[2]
                        player[4] = item
                    elif item[1] == "food":
                        if (max_hp - player[2]) - item[2] <= 0:
                            player[2] = max_hp
                        else:
                            player[2] += item[2]
                        inv[index] = ["<>", "None"]
                        print("*%s был/-о употреблено*\n" % item[0])
                        print(main.heal % (player[0], item[2], player[2], max_hp))
                    else:
                        print("Ячейка пуста!")
            if in_chs == "2":
                in_in_chs = input("Предмет под номером: ")
                index = int(in_in_chs)
                item = inv[index]
                if inv[index] != ["<>", "None"]:
                    inv[index] = ["<>", "None"]
                    print("*%s выбросили*" % item[0])
                else:
                    print("Ячейка пуста!")
            print(main.inventory % (gen.inv(inv)))
            in_chs = input(main.inventory_chs)
        else:
            chs = input(ds)
    elif chs == "1":
        if not map_d:
            room = input(main.chs_screen_main)
            map_d.append(str(room))
        elif map_d[-1] == "2":
            room = input(main.chs_screen_main)
            map_d.append(str(room))
        elif map_d[-1] == "1":
            room = input(main.chs_screen_1)
            map_d.append(str(room))
        elif map_d[-1] == "3":
            room = input(main.chs_screen_3)
            map_d.append(str(room))
        k_r += 1

        m = gen.event()

        if m[1] == "enemy":
            c, unit = gen.fight(m, player, max_hp)
            if c == "W":
                player = unit
                player[5] += m[4]
                print(main.conclusion_w % (player[0], m[0], m[4], player[5]))
                if player[5] > n_lvl:
                    print(main.new_lvl % (lvl + 1, player[5], n_lvl, player[5] - n_lvl))
                    lvl += 1
                    max_hp += gen.upgrade_hp(lvl)
                    player[2] = max_hp
                    print(main.heal % (player[0], max_hp - player[2], player[2], max_hp))
                    xp_max += player[5]
                    player[5] -= n_lvl
                    n_lvl = gen.lvl(lvl + 1)
                c = None
                chs = input(ds)
                print("\n")
            else:
                c = ""
                chs = "5"

        elif m[1] == "trap":
            player[2] += m[2]
            print("@Вы наткнулись на ловушку! Это - %s" % m[0])
            if player[2] <= 0:
                chs = "5"
            else:
                print(main.damage % (player[0], m[2], player[2], max_hp))
                chs = input(ds)
        else:
            if ["<>", "None"] in inv:
                inv[inv.index(["<>", "None"])] = m
                print("@Вы достали %s!" % m[0])
                print("*%s был/-а добавлен/-а в инвентарь*\n" % m[0])
                chs = input(ds)
                print("\n")
            else:
                print("Недостаточно места в инвентаре! Предмет был выброшен!")
                chs = input(ds)
    elif chs == "3":
        s_name = gen.save(player, map_d, inv, s_name, player[5], player[6], max_hp, xp_max)
        chs = input(ds)
    elif chs == "4":
        print(main.save_screen)
        chs = input("- ")
        Ok = True
        while Ok:
            if chs == "2":
                chs = "5"
                break
            if chs == "1":
                s_name = gen.save(player, map_d, inv, s_name, player[5], player[6], max_hp, xp_max)
                chs = "5"
                break
            else:
                print("Введите верный номер")
                Ok = False
    else:
        print(main.stats % (k_r, player[5], player[6]))
        print("Goodbye! See you next time!")
        gen.map_f(map_d)
        main.sys.exit()
