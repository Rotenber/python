import random

# Баланс
try:

    with open("casino_balance.txt", "r") as file:
     balance = int(file.read().strip())

except FileNotFoundError:
    balance = 10000 
except ValueError:
    balance = 10000 

try:
    with open("casino_credit.txt", "r") as file:
        loan = int(file.read().strip())
except FileNotFoundError:
    loan = 0

except ValueError:
    loan = 0
    
try:
     with open("casino_fortune.txt", "r") as file:
        spins = int(file.read().strip())
except FileNotFoundError:
    spins = 1

except ValueError:
    spins = 1
    
    
# Начало

print("Добро пожаловать в Las Vegas Casino!!!")
print("Умножение при выигрышном числа:  36х")
print("Умножение при выпадении (цвета, Even, Odd): 2х")
print("Умножение при выпадении сектора: x3")
print("Навигация\n Рулетка - roulet\n Колесо фортуны - fortune\n Купить спины колеса фортуны - shop")


while True:

    # УУууулетаю на гаити 
    menu = input("Выберите режим из навигации! ").lower()
    if menu == "exit":
        print("Выходим из программы!")
        break
        
    elif menu == "shop":
        while True:
            print("Вы вошли в магазин!")
            print("Вы можете купить спины для колеса фортуны (1 спин - 3000$).")
            buy = input("Хотите купить? (да/нет): ").lower()
            price = 3000
            
            if buy == "exit": 
                print("Вы вышли из магазина. Возвращаемся в главное меню.")
                break

            elif buy == "нет":
                print("Вы вышли из магазина. Возвращаемся в главное меню.")
                break  

            elif buy == "да":
                try:
                    spins_to_buy = int(input("Сколько вы хотите купить спинов? "))
                    if spins_to_buy <= 0:
                        print("Введите положительное число!")
                        continue
                    
                    total_cost = spins_to_buy * price
                    
                    if total_cost > balance:
                        print(f"Недостаточно средств. Ваш баланс: {balance}$. Попробуйте снова.")
                        continue
                    
                    # Проверка на покупку всех денег
                    if total_cost == balance:
                        confirm = input("Вы уверены, что хотите потратить весь баланс? (да/нет): ").lower()
                        if confirm != "да":
                            print("Возвращаемся к выбору количества.")
                            continue
                    
                    # Совершаем покупку
                    balance -= total_cost
                    spins += spins_to_buy
                    print(f"Покупка успешна! У вас {spins} спинов. Ваш баланс: {balance}$.")
                
                except ValueError:
                    print("Введите корректное количество спинов.")
                    continue

            else:
                print("Введите 'да' или 'нет'.")
                continue

            # Сохраняем данные
            with open("casino_balance.txt", "w") as file:
                file.write(str(balance))
            with open("casino_fortune.txt", "w") as file:
                file.write(str(spins))

                          
            
    elif menu == "fortune":
            
        while True:
                
            print(f"Вы вошли в режим: 'Колесо фортуны'. У вас {spins} вращений.")
            print("Призы - Деньги в любом количестве от 1$ до 50000$. Хотите прокрутить колесо фортуны? (да/нет)")
            roll = input("Хотите покрутить колесо удачи?: ").lower()
            if roll == "нет":
                print("Выход из режима 'Колесо фортуны'. Приятной игры!")
                break
            elif roll == "exit":
                print("Выходим из режим Колесо фортуны в главное меню")
                break
            
            if spins <= 0:
                print("У вас закончились вращения! Пополните баланс для новых игр.")
                break
            
            spins -= 1
            prize = random.randint(1, 50000)
            balance += prize
            print(f"Вы выиграли {prize}$! Ваш баланс: {balance}$. Осталось {spins} вращений.")
            
            if prize >= 50000:
                print("WIN WIN WIN!!!")
                print(f"Вы сорвали JACKPOT и забираете {prize}$! Ваш баланс {balance}$.")
                break

            with open("casino_fortune.txt", "w") as file:
                file.write(str(spins))
            
            with open("casino_balance", "w") as file:
                file.write(str(balance))
                    
        
    elif menu == "roulet":
        print("Вы вошли в режим Рулетка для выхода в меню (exit)")
        print(f"Ваш текущий баланс: {balance}$")
        
        while True:
        
            bet = input("Введите сумму ставки: ")
            if bet == "exit":
                break
        
            bet = int(bet)
            if bet > balance:
                print(f"На вашем балансе не достаточно денег: {balance}$. Попробуйте снова.")
                continue

            def get_apettes(balance):
                if  balance > 50000:
                    return 6
                elif balance > 100000:
                    return 7
                else:
                    return 5

            apattes = get_apettes(balance)   
            streak = 0
        
    
            bets = []
            while apattes > 0:
                user_bet = input(f"Делайте вашу ставку (число от 0 до 36 или 'красное/черное или 'Even/Odd' или можете выбрать сектор '1st, 2nd, 3rd'). У вас осталось {apattes} ставок: ").lower()
                if user_bet == "exit":
                    break

                if user_bet.isdigit():
                    user_bet = int(user_bet)
                    if user_bet < 0 or user_bet > 36:
                        print("Ошибка - выберите число от 0 до 36")
                        continue
                    elif user_bet not in ["красное", "черное", "even", "odd", "1st", "2nd", "3rd,"]:
                        print("Выберите корректный цвет: 'красное' или 'черное'")
                        continue
            
            
            bets.append(user_bet)
            apattes -= 1
            print(f"Вы сделали ставку. Осталось {apattes} ставок.")
        
            print("Рулетка крутится...")
        
            # Рулетка рандом 

            number_random = random.randint(0, 36)
            color_random = random.choice(["красное", "черное"])
            parity_random = random.choice(["Even, Odd"])
            sector_ramdom = random.choice(["1st", "2nd", "3rd"])
        
            print(f"Выпало число: {number_random}")
            print(f"Выпал цвет: {color_random}")
            print(f"Выпала четность: {parity_random}")
            print(f"Выпал сектор: {sector_ramdom}")

            # Проврка 

            for user_bet in bets:
                if user_bet == number_random:
                    win = bet * 35
                    balance += win
                    print(f"Поздравляем!! Вы угадали число {number_random}. Ваш выигрыш: {win}$, баланс: {balance}$")
                elif user_bet == color_random:
                    win = bet * 2
                    balance += win
                    print(f"Поздравляем!! Вы угадали цвет {color_random}. Ваш выигрыш: {win}$, баланс: {balance}$")
                elif user_bet ==parity_random:
                    win = bet * 2
                    balance += win
                    print(f"Поздравляем!! Вы угадали четность {parity_random}. Ваш выигры: {win}$, баланс {balance}$")
                elif user_bet == sector_ramdom:
                    win = bet * 3
                    balance += bet
                    print(f"Поздравляем!! Вы угадали сектор {sector_ramdom}. Ваш выигращ {win}$, баланс {balance}$ ")
                elif user_bet == sector_ramdom or user_bet == number_random or user_bet == color_random or user_bet == parity_random:
                    streak += 1
                    if streak == 3:
                        print(f'Поздравляем!! Вы выиграли {streak} подряд.')
                        if bet < 1000:
                            print(f"Ваше вознаграждение 500$")
                            balance += 500
                            print(f"Ваш баланс: {balance}$")
                        elif bet < 5000:
                            print(f"Ваше вознагрждение 1500$")
                            balance += 1500
                            print(f"Ваш баланс: {balance}")
                        elif bet <25000:
                            print(f"Ваше вознаграждение 5500$")
                            balance += 5500
                            print(f"Ваш баланс: {balance} ")

                    if win == 50000:
                        if balance >=50000 and balance <100000:
                            player_level = "Silver VIP"
                            apattes = 6
                            print(f"Крупный выиграш. Ваше вознаграждение Silver Vip")
                            print(f"Преимуществе Silver VIP: + 1 ставка (доступно 6 ставок)")

                    elif win == 100000:
                        if balance >=100000 and balance <150000:
                            player_level = "Platinum"
                            apattes = 7
                            print(f"Крупный выиграш. Ваше вознагрждение Platinum VIP")
                            print(f"Преимущества Platinum VIP: +1 ставка ( доступно 7 ставок)")

                else:
                    balance -= bet
                    print(f"Вы проиграли ставку {bet}$. Баланс: {balance}$")

                if balance > 50000:
                    player_level = "Silver VIP"
                    apattes = 6

                elif balance > 100000:
                    player_level = "Platinum"
                    apattes = 7



            with open("casino_balance.txt", "w") as file:
                file.write(str(balance))

            with open("casino_history.txt", "a") as file:
                file.write(f"Ставка {bets}\n, сумма ставки {bet}\n  Число - {number_random}\n Цвет - {color_random}\n Сектор - {sector_ramdom}\n Четность (Even/Odd) - {parity_random}\n ")


            if balance <= 0:
                credit = input("Ваш баланс равен 0. Вы можете взять крдеит. Хотите оформить (да/нет)?").lower()
                if credit == "да":
                    var = input("Вам доступно 3 разных кредита. 'Стандарт' 'Премиум' 'Люкс' какой из кредитов вы хотите взять ?").lower()
                    if var == "стандарт":
                        loan = 5000
                        balance += loan
                        print(f"Вам зачислен кредит. Ваш баланс {balance}$ ")
                        print("Кредит спишется автоматически")
                    elif var == "премиум":
                        loan = 10000
                        balance += loan
                        print(f"Вам зачислен кредит. Ваш баланс {balance}$")
                        print("Кредит спишется автоматически")
                    elif var == "люкс":
                        loan = 20000
                        balance += loan
                        print(f'Вам зачислен кредит. Ваш баланс {balance}$')
                        print("Кредит спишется автоматически")
                    else:
                        print("Введите коректное название кредитного пакета!!!")

            if loan > 0 and balance > 0:
                if balance > loan ** 2:
                    print("Кредит в размере {loan}$ полностью погаше")
                    balance -= loan
                    credit = 0

            with open("casino_credit.txt" "w") as file:
                file.write(str(loan))
                









