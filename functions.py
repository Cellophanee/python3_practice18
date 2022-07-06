import heapq
l = [3, 6, 6, 1, 89, 2, 0, 0, 5, 27, 4, 4]
print("Список: ", l)
def srtd():
    l.sort(reverse=True)
    print('Сортований список:', l)
def srch():
    s = int(input('Який n-ий елемент списку знайти:'))
    sr = l[s]
    print(s, 'елемент в списку =', sr)
def sqnc(sp, pos):
    for i in range(len(sp) - len(pos)):
        if sp[1:1 + len(pos)] == pos:
            return print('Послідовність збігається')
    return print('Послідовність розбігається')
ls = [int(s) for s in input('Яку послідовність елементів списку знайти:').split(",")]
sqnc(l, ls)
def smlst():
    print("5 найменших елементів списку: ", heapq.nsmallest(5, l))
def lrgst():
    print("5 найбільших елементів списку: ", heapq.nlargest(5, l))
def arfm():
    ar = sum(l) / len(l)
    print('Середнє арифметичне списку =', round(ar, 2))
def fun(l):
    tmp = set()
    res = []
    for element in l:
        if element not in tmp:
            res.append(element)
        tmp.add(element)
    return res
print('Повернений список:', fun(l))