def convert_tuple(n):
    t = tuple(n[1:-1].replace("'", "").split(", "))
    return t


def convert_list(n):
    t = list(n[1:-1].replace("'", "").split(", "))
    return t


def convert(n, b: bool):
    n = n.split(";")
    if b:
        flag = True
        stop = False
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
                stop = True
            if n[0] == "[":
                l = n.find("[")
                r = n.find("]")
                if l - 1 < 0 and r + 2 <= len(n) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[r + 3:]
                elif l - 1 > 0 and r + 2 > len(n) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[:l - 2]
                elif l - 1 < 0 and r + 2 > len(n) - 1:
                    m.append(convert_list(n[l:r + 1]))
                    n = ''
                    flag = False
                    break
                else:
                    m.append(convert_list(n[l:r + 1]))
                    n = n[:l - 1] + n[r + 2:]
                stop = True
            if n[0] == "'" and ", " in n and not stop:
                a = n.replace("'", "", 2).split(", ", 1)
                n = a[1]
                m.append(a[0])
                stop = True
            elif ", " in n and not stop:
                a = n.split(", ", 1)
                n = a[1]
                m.append(a[0])
                stop = True
            if ", " not in n and flag:
                flag = False
                if "'" in n:
                    m.append(n.replace("'", ""))
                else:
                    m.append(n)
                n = ''
                break
            stop = False
        return m
    return n


print(convert("[['<>', 'None'], ['<>', 'None'], ['<>', 'None'], ['<>', 'None'], ['<>', 'None']];", True))