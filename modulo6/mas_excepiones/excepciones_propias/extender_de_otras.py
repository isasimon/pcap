class MyZeroDivisionError(ZeroDivisionError):
    pass


def doTheDivision(mine):
    if mine:
        raise MyZeroDivisionError("peores noticias")
    else:
        raise ZeroDivisionError("malas noticias")


for mode in [False, True]:
    try:
        doTheDivision(mode)
    except ZeroDivisionError:
        print('División entre cero')


for mode in [False, True]:
    try:
        doTheDivision(mode)
    except MyZeroDivisionError:
        print('Mi división entre cero')
    except ZeroDivisionError:
        print('División entre cero original')