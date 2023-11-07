# Задание 2. (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.
import subprocess

SIGNS = '''!()-[]{};?@#$%:'"\,./^&;*_ ='''


def subprocess_file(directory: str, name: str, words = 'Yes'):
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    words = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if name in lst:
            for x in name:
                if x in SIGNS:
                    name = name.replace(x, " ")
            if words in name:
                print('Find')
            else:
                print('No find')
            return True
        return False
    return False


if __name__ == '__main__':
    print(subprocess_file('cat /etc/os-release', 'VERSION="22.04.2 LTS (Jammy Jellyfish)"', '04'))