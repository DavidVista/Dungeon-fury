import sys
import os


def load_list(p, n):
    print("_Saves_________________")
    i = 1
    while i != n:
        if os.listdir(p)[i] != "scores.txt":
            print("[%s]. %s" % (i, os.listdir(p)[i]))
            i += 1
    print("_______________________")


def game(pl_name):
    global save
    chs = input(menu_load_save % pl_name)
    while chs != "1":
        if chs == "2":
            if os.listdir(path) is []:
                print("Нет сохранений!")
                chs = input(menu_load_save % pl_name)
            else:
                f = os.listdir(path)
                load_list(path, len(f))
                chs_in = input(dialog_screen_s)
                while chs_in != "3":
                    if chs_in == "1":
                        chs_num = input("Загрузить сохранение под номером: ")
                        if int(chs_num) > len(f) or int(chs_num) < 1:
                            print("Такого сохранения не существует!")
                            chs_in = input(dialog_screen_s)
                        else:
                            save = f[int(chs_num)]
                            return 1
                    if chs_in == "2":
                        chs_num = input("Удалить сохранение под номером: ")
                        if int(chs_num) > len(f) or int(chs_num) < 1:
                            print("Такого сохранения не существует!")
                            chs_in = input(dialog_screen_s)
                        else:
                            chs_in = input(del_screen % f[int(chs_num)])
                            if chs_in == "1":
                                os.remove(path + "/" + f[int(chs_num)])
                                print("Сохранение %s успешно удалено!" % f[int(chs_num)])
                                chs_in = input(dialog_screen_s)
                            else:
                                print("Отмена удаления!")
                                chs_in = input(dialog_screen_s)
                chs = input(menu_load_save % pl_name)
        if chs == "3":
            print("Hello!")
            chs = input(menu_load_save % pl_name)
        if chs == "4":
            return 0
    else:
        return 1


def change_name():
    global pl_name
    pl_name = input("Теперь вас зовут: ")
    print("Приветствуем вас, %s" % pl_name)


def rules():
    return 0


key = 0
path = os.getcwd()


if not os.path.exists(path + "/saves"):
    os.mkdir(path + "/saves")
if not os.path.exists(path + "/saves/scores.txt"):
    scores_file = open(path + "/saves/scores.txt", "w", encoding="UTF-8")
    scores_file.write("Name | Level | Q. of chambers | Total xp")
    scores_file.close()
path += "/saves"
save = None

menu = """
_________________________________
[1]. Начать игру!
[2]. Сменить имя.
[3]. Правила игры.
[4]. Выход.
__
% s
_________________________________
"""

menu_load_save = """
_________________________________
[1]. Начать новую игру.
[2]. Загрузить.
[3]. Список рекордов.
[4]. Назад ->
--
% s
_________________________________
"""

save_list = """
_________________________________
Save list
[1]. <%s>                  [%s]
[2]. <%s>                  [%s]
[3]. <%s>                  [%s]
[4]. <%s>                  [%s]
[5]. <%s>                  [%s]
_________________________________

"""

dialog_screen = """
|1| Продолжить |2| Открыть инвентарь |3| Сохранить |4| Выйти
"""

save_screen = """
_________________________________
Сохранить прогресс перед выходом?
 _______________________________
  [1] Да                [2] Нет
"""

del_screen = """
_______________________________________________
Вы уверены, что хотите удалить сохранение %s?
 ___________________________________________
  [1] Да                            [2] Нет
"""

dialog_screen_sp = """
|1| Продолжить |2| Открыть инвентарь |3| Пересохранить |4| Выйти
"""

dialog_screen_s = """
|1| Выбрать сохранение |2| Удалить сохранение |3| Назад
"""

chs_screen_main = """
|            [2]
|             ↑
|       [1]← [☺] →[3]
|       Выберите проход
"""

chs_screen_1 = """
|            [2]
|             ↑
|       [1]← [☺]
|       Выберите проход
"""

chs_screen_3 = """
|            [2]
|             ↑
|            [☺] →[3]
|       Выберите проход
"""

inventory = """
+-Инвентарь---------------------
|1. %s                     [%s]
|2. %s                     [%s]
|3. %s                     [%s]
|4. %s                     [%s]
|5. %s                     [%s]
-------------------------------
"""

inventory_chs = """
|1| Выбрать |2| Удалить |3| Выйти из инвентаря
"""

item = """
| %s %s                 [%s]
| <1) Использовать/Экипировать>
|                    <2) Выход>
"""

fight_screen = """
_Бой!_____________________________

    Враг: %s
    Здоровье: %s
    Урон: %s
   ____________________________
    %s
    Здоровье: %s
    Оружие: %s
    Урон: %s
__________________________________
"""

damage = """
_Урон________
    %s
  %s hp
%shp / %shp
_____________
        """

heal = """
_Лечение________
    %s
  %s hp
%shp / %shp
________________
"""

conclusion_w = """
__Победа!__________________
 %s одержал победу над %s!
 Так держать!
        + %s xp
          %s xp
 __________________________
"""
conclusion_l = """
__Проигрыш!__________________
 %s одержал победу над %s!
 Вы погибли!
 ____________________________
"""

end_titles = """
_________Game_Over__________
Вы погибли!
Причина гибели: %s;
____________________________
"""

stats = """
________Статистика__________
Всего пройдено комнат : %s
Опыт : %s xp
Уровень : %s lvl
____________________________
"""

new_lvl = """
__________Новый_Уровень!__________
             %s Lvl
          %s xp / %s xp
               _
             %s xp
__________________________________
"""

print("""
_________________________________
Cave quest - Пещерное приключение
v.0.3.3
DavidXp (c)
_________________________________
""")
pl_name = input("Введите ваше имя: ")
print(menu % pl_name)
chs = input("- ")

while key != 1:
    if chs == "1":
        key = game(pl_name)
        if key == 1:
            break
        print(menu % pl_name)
        chs = input("- ")
    if chs == "2":
        change_name()
        print(menu % pl_name)
        chs = input("- ")
    if chs == "3":
        rules()
        print(menu % pl_name)
        chs = input("- ")
    if chs == "4":
        sys.exit()
