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
    with open("credit_casino.txt", "r") as file:
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
    
try:
    with open("casino_dice_log.txt" "r") as file:
     dice_log = int(file.read().strip())
except FileNotFoundError:
    dice_log = 0

except ValueError:
    dice_log = 0
    
try:
    with open("casino_dice_pc_log.txt" "r") as file:
        dice_log_pc = int(file.read().strip())
except FileNotFoundError:
    dice_log_pc = 0

except ValueError:
    dice_log_pc = 0
    
try:
    with open("casino_log.txt" "r") as file:
        casino_log = int(file.read().strip())
except FileNotFoundError:
    casino_log = 0

except ValueError:
    casino_log = 0
    
    
# Начало

print("Добро пожаловать в Las Vegas Casino!!!")
print("Умножение при выигрышном числа:  36х")
print("Умножение при выпадении (цвета, Even, Odd): 2х")
print("Умножение при выпадении сектора: x3")


while True:
    
    if loan > 0:
        if balance >= 2 * loan:
            balance -= loan
            print(f"Кредит в размере {loan}$ полностью погашен автоматически, так как ваш баланс в два или более раза превышает сумму кредита.")
            loan = 0
        else:
            print(f"Недостаточно средств для автоматического погашения кредита. Ваш баланс: {balance}$, кредит: {loan}$.")
            print("Кредит будет закрыт, когда ваш баланс станет в два или более раза больше суммы кредита.")

    # Сохранение изменений в файлы
    with open("casino_balance.txt", "w") as balance_file:
        balance_file.write(str(balance))

    with open("casino_credit.txt", "w") as credit_file:
        credit_file.write(str(loan))

    # УУууулетаю на гаити 
    print("Навигация\n Рулетка - roulet\n Колесо фортуны - fortune\n Кости - dice\n Купить спины колеса фортуны - shop\n Кредит - credit\n BlakcJack - 21")
    menu = input("Выберите режим из навигации! ").lower()
    if menu == "exit":
        print("Выходим из программы!")
        break
    
    elif menu == "blackjack" or menu == "блекджек" or menu == "21":
        print("Вы вошли в игру BlackJack!")

        while True:
            lop = input("Введите сумму ставки (или введите 'exit' для выхода): ").lower()
            if lop == "exit" or lop == "выйти":
                print("Возвращаем вас в главное меню!")
                break

            try:
                lop = int(lop)
            except ValueError:
                print("Введите корректное число!")
                continue

            if balance < lop:
                print(f"У вас недостаточно денег. Ваш баланс: {balance}$")
                continue

            
            print("Игра начинается!")
            player_hand = [random.randint(1, 11), random.randint(1, 11)]
            dealer_hand = [random.randint(1, 11), random.randint(1, 11)]

            print(f"Ваши карты: {player_hand}, Сумма: {sum(player_hand)}")
            print(f"Первая карта дилера: {dealer_hand[0]}")

            
            while sum(player_hand) < 21:
                action = input("Хотите взять ещё карту? (да/нет): ").lower()
                if action == "да":
                    new_card = random.randint(1, 11)
                    player_hand.append(new_card)
                    print(f"Вам выпала карта: {new_card}, Ваши карты: {player_hand}, Сумма: {sum(player_hand)}")
                    if sum(player_hand) > 21:
                        print("У вас перебор! Вы проиграли.")
                        balance -= lop
                        with open("casino_balance.txt", "w") as file:
                            file.write(str(balance))
                        with open("casino_log.txt", "a") as log_file:
                            log_file.write(f"Проигрыш: {lop}$ | Баланс: {balance}$\n")
                        break
                elif action == "нет":
                    print(f"Вы остались с картами: {player_hand}, Сумма: {sum(player_hand)}")
                    break
                else:
                    print("Введите 'да' или 'нет'.")

            
            if sum(player_hand) <= 21:
                print("Ход дилера!")
                while sum(dealer_hand) < 17:
                    new_card = random.randint(1, 11)
                    dealer_hand.append(new_card)
                    print(f"Дилер взял карту: {new_card}, Карты дилера: {dealer_hand}, Сумма: {sum(dealer_hand)}")

                
                print(f"Ваши карты: {player_hand}, Сумма: {sum(player_hand)}")
                print(f"Карты дилера: {dealer_hand}, Сумма: {sum(dealer_hand)}")

                if sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
                    print("Вы выиграли!")
                    balance += lop
                    with open("casino_balance.txt", "w") as file:
                        file.write(str(balance))
                    with open("casino_log.txt", "a") as log_file:
                        log_file.write(f"Выигрыш: {lop}$ | Баланс: {balance}$\n")
                elif sum(player_hand) < sum(dealer_hand):
                    print("Вы проиграли.")
                    balance -= lop
                    with open("casino_balance.txt", "w") as file:
                        file.write(str(balance))
                    with open("casino_log.txt", "a") as log_file:
                        log_file.write(f"Проигрыш: {lop}$ | Баланс: {balance}$\n")
                else:
                    print("Ничья!")
                    with open("casino_log.txt", "a") as log_file:
                        log_file.write(f"Ничья | Баланс: {balance}$\n")

            print(f"Ваш текущий баланс: {balance}$")

            if balance <= 0:
                print("У вас закончились деньги. Возвращаемся в главное меню.")
                break

            
            play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
            if play_again != "да":
                print("Возвращаемся в главное меню.")
                break

          
    
    elif menu == "credit" or menu == "кредит":
        print("Вы вошли в режим Кредит!")
        print("Здеь вы можете оформить или закрыть кредит досрочно!")
        while True:  
            
            kr = input("Выберите действие (оформить/закрыть)?: ").lower()
            if kr == "exit" or kr == "выход":
                print("Возвращаем в главное меню:")
                break
            
            elif kr == "закрыть":
                if loan <= 0:
                    print("Сейчас у вас нет открытых кредитов. Возвращаем к выбору действий.")
                    break
                else:
                    zin = input(f"Ваш текущий кредит {loan}$. Хотите закрыть? (да/нет): ").lower()
                    if zin == "да":
                        if balance >= loan:
                            balance -= loan
                            loan = 0
                            print(f"Кредит успешно закрыт!\nВаш баланс: {balance}$")
                        else:
                            print(f"У вас недостаточно средств для закрытия кредита. Ваш баланс: {balance}$, кредит: {loan}$")
                    elif zin == "нет":
                        print("Возвращаем к выбору действий.")\
                            
                    
                    elif kr == "оформить":
                        if loan > 1:
                            print(f"У вас уже есть открытый кредит на сумму {loan}$. Сначала закройте прошлый кредит!!!")
                            break
                            
            else:
                klip = input("Для вас доступно 3 пакета кредитов Standart, Premium, Plus: ").lower()
                                
                if klip == "standart" or klip == "стандарт":
                    stan = input("Пакет Standart дает 5000$ в кредит. Хотите оформить ?")
                    if stan == "нет":
                        print("Возвращаем к выбору пакета!")
                        continue
                                    
                    elif stan == "да":
                        loan = 5000
                        balance += loan
                        print(f"(Вы усешно оформили кредит! Такущая ситуация по кредиту {loan})$ - Баланс {balance}$")
                        print("Кредит спишется автоматически или вы можете закрыть его сами!")
                                        
                    elif klip == "premium" or klip == "премиум":
                        stan = ("Пакет Premium дает 10000$ в кредит. Хотите оформить ?")
                        if stan == "нет":
                            print("Возвращаем к выбору пакета!")
                            continue
                                
                    elif stan == "да":
                        loan = 10000
                        balance += loan
                        print(f"(Вы усешно оформили кредит! Такущая ситуация по кредиту {loan})$ - Баланс {balance}$")  
                        print("Кредит спишется автоматически или вы можете закрыть его сами!")
                                        
                    elif klip == "Plus" or klip == "плюс":
                        stan = ("Пакет Plus дает 2000$ в кредит. Хотите оформить ?: ")
                        if stan == "нет":
                            print("Возвращаем к выбору пакета!")
                            continue
                                    
                    elif stan == "да":
                        loan = 20000
                        balance += loan 
                        print(f"(Вы усешно оформили кредит! Такущая ситуация по кредиту {loan})$ - Баланс {balance}$")  
                        print("Кредит спишется автоматически или вы можете закрыть его сами!")
                                    
                                    
                                        
                    with open("credit_casino.txt", "w") as file:
                        file.write (str(loan))
                    break
                    
    elif menu == "dice" or menu == "кости":
            print("Вы вошли в игру  Кости! для выхода (exit)")
            pc = input("Вы можете сыграть в 2 режим котей! 1 - Игра против компьютера 2 - Ставка на выпадение числа в костях (пк/ставка): ").lower()
            while True:
                if pc == "пк":
                    kop = input("Игра против Компьютера - Делайте вашу ставку: ")
        
                    if kop == "еxit" or kop == {"выйти"}:
                        print("Возвращаем вас в главное меню")
                        break
                    
                    kop = int(kop)
                    
                    if balance < kop:
                        print(f"У вас недостаточно денег! Ваш баланс {balance}$")
                        continue
                    
                    else:
                        print("Ваша ставка принята!")
                        
                    pc_random = random.randint(1, 12)
                    kop_random = random.randint(1, 12)
                    
                    if pc_random > kop_random:
                        balance -= kop
                        print(f"Вам выпало {kop_random} - Компьютеру выпало {pc_random}. Вы проиграли!! - Ваш банас {balance}$")
                        continue
                    
                    elif pc_random == kop_random:
                        print(f"Вам выпало {kop_random} - Компьютеру выпало {pc_random}. Ничья!!! Ваш баланс - {balance}$")
                        continue
                    
                    elif pc_random < kop_random:
                        balance += kop
                        print(f"Вам выпало {kop_random} - Компьютеру выпало {pc_random}. Вы выиграли!! Ваш баланс {balance}$")
                        continue
                    
                    if balance <= 0:
                        print(f"Возвращаем вас в главное менюю. Ваш баланс {balance}$ ")
                        break
                    
                    with open("casino_balance.txt", "w") as file:
                        file.write(str(balance))
                    
                    with open("casino_dice_pc_log.txt", "a") as file:
                        file.write(f"Ставка - {nill}\n Число - {popa}\n Выпало - {dice_popa_random}\n Баланс - {balance}\n")
                    
                else:
                    print("Вы выбрали не коректный режим игры! Попробуйте снова")
                    break
                        
                        
                              
                stav = input("Вы в режим кости - угадай число. Вы хотите сделать ставку ? (да/нет)").lower()
                
                if stav == "нет":
                    print("Выходим из игры Кости и возвращаем вас в главное меню!")
                    break
                
                elif stav == "да":
                    nill = input("Введите сумму ставки: ")
                    nill = int (nill)

                    if nill == "exit":
                        print("Возвращаем вас в главное меню!")
                        break
                    elif nill  > balance:
                        print(f"На вашем балансе не достаточно денег: {balance}$. Попробуйте снова.")
                        continue
                    
                    
                    popa = input("Выберите число от 1 до 12: ")
                    popa = int(popa)
                    
                    if popa == "exit":
                        print("Возвращаем вас в главное меню!")
                        break                    
                    
                    elif popa < 1 or popa > 12:
                        print("Ошибка - Введите число от 1 до 12")
                        continue
                            
                    else:       
                        print("Вы сделали ставку!")       
                        print("Бросаем кубики...")
                        
                        dice_popa_random = random.randint(1, 12)
                                
                        print(f"Выпало число {dice_popa_random}")
                        
                        if popa == dice_popa_random:
                            piska = nill * 3
                            balance += piska
                            print(f"Поздравляем вы выиграли. Выпало чиссло {dice_popa_random} -  Ваш текущий баланс {balance}$")
                        else:
                            balance -= nill
                            print(f"Попробуйте снова. Выпало число {dice_popa_random} - Ваш баланс {balance}$ - Вам обьязательно повезет! для выхода (exit)")
                            continue
                        
                        if balance < nill:
                            print(f"У вас недостаточно денег. Ваш баланс {balance}")
                            continue
                        
                
                with open("casino_balance.txt", "w") as file:
                    file.write(str(balance))
                    
                with open("casino_dice_log.txt", "a") as file:
                    file.write(f"Ставка - {nill}\n Число - {popa}\n Выпало - {dice_popa_random}\n Баланс - {balance}\n")
                                
        
    elif menu == "shop" or menu == "магазин":
        while True:
            print("Вы вошли в магазин! для выхода (exit)")
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

                          
            
    elif menu == "fortune" or menu == "колесо вортуны":
            
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
                    
        
    elif menu == "roulet" or menu == "рулетка":
        print("Вы вошли в  игру  Рулетка для выхода в меню (exit)")
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
                
                
                if user_bet.isdigit() and (int(user_bet) < 0 or int(user_bet) > 36):
                    print("Ошибка - выберите число от 0 до 36")
                    continue
                                

                if user_bet not in ["красное", "черное", "even", "odd", "1st", "2nd", "3rd"] and not user_bet.isdigit():
                    print("Выберите корректный цвет: 'красное' или 'черное'")
                    continue    

            
            
            bets.append(user_bet)
            apattes -= 1
            print(f"Вы сделали ставку. Осталось {apattes} ставок.")
                
            print("Рулетка крутится...")
        
            # Рулетка рандом 

            number_random = random.randint(0, 36)
            color_random = random.choice(["красное", "черное"])
            parity_random = random.choice(["Even", "Odd"])
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
                        
                    with open("casino_credit.txt" "w") as file:
                        file.write(str(loan))
                        break

                









