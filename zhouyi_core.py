print(" 卜卦开始...")
print(" 心诚则灵")

# qigua_simple.py
import random

def yao():  # 蓍草概率 1:5:7:3
    return random.choices([6, 7, 8, 9], weights=[1, 5, 7, 3])[0]

def symbol(n):
    return '⚊' if n in (7, 9) else '⚋'

def qi_gua():
    return [yao() for _ in range(6)][::-1]  

def show(gua):
    print('本卦：')
    for i, v in enumerate(gua, 1):
        print(f'{i}爻  {symbol(v)}  {v}{" (变)" if v in (6, 9) else ""}')

if __name__ == '__main__':
    show(qi_gua())