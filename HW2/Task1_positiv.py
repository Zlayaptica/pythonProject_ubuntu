# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
# и разархивирования с путями (x).
# *Задание 2. *
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). Проверить,
# что хеш совпадает с рассчитанным командой crc32.

import subprocess

tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    result1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(out), "arx2.7z")
    assert result1 and result2, "test1 FAIL"


def test_step2():
    # test2
    result1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder1), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder1), "qwe")
    result3 = checkout("cd {}; ls".format(folder1), "rty")
    result4 = checkout("cd {}; ls".format(folder1), "add")
    assert result1 and result2 and result3 and result4, "test2 FAIL"


def test_step3():
    # test3
    assert checkout("cd {}; 7z t arx2.7z ".format(out), "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout("cd {}; 7z u {}arx2.7z ".format(tst, out), "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout("cd {}; 7z d {}/arx2.7z ".format(out, out), "Everything is Ok"), "test5 FAIL"
