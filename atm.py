correct_pin = "1234"
tries = 3
history = []
deposit_count = 0
operation_count = 0
receiver_balance = 0
while True:
    passw = input("Enter your pin-code: ")
    if passw == correct_pin:
        print("Pin-code is correct")
        break
    else:
        tries -= 1
        if tries == 0:
            print("❌ Карта заблокирована.")
            exit()
        else:
            print(f"Неверный PIN. Осталось попыток: {tries}")

balance = 0  # стартовый баланс для проверки налога
print(f"Your balance: {balance}")

print(
    "\n1.Посмотреть баланс"
    "\n2.Пополнить счёт"
    "\n3.Снять деньги"
    "\n4.Выйти"
    "\n5.Показать историю"
    "\n6.Перевести деньги"
    "\n7.Сменить PIN-код"
    "\n8.Сброс истории операций"
)

while True:
    if operation_count >= 10:
        print(f"Лимит операций за сессию исчерпан. Сеанс завершён.")
        break
    if balance > 5000000:
        tax = balance * 0.10
        balance -= tax
        print(f"💰 Внимание! Списан налог на богатство: {tax}")
        print(f"Новый баланс: {balance}")

    choice = int(input("Choice your operation: "))

    if choice == 1:
        print(f"Your balance = {balance}")

    elif choice == 2:
        amount = int(input("Введите сумму пополнения: "))
        if amount > 10000:
            print("❌ Превышена максимальная сумма пополнения (10 000).")
        else:
            balance += amount
            deposit_count += 1
            history.append(f"Пополнение: +{amount}")
            operation_count += 1
            print(f"✅ Баланс пополнен! Текущий баланс: {balance}")

            if deposit_count % 3 == 0:
                bonus = amount * 0.05
                balance += bonus
                history.append(f"Бонус за активность: +{bonus}")
                print(f"🎁 Бонус за активность: +{bonus}")

    elif choice == 3:
        spend = int(input("Enter sum for cash: "))
        if spend > 5000:
            print("❌ Превышена максимальная сумма снятия (5 000).")
        else:
            commission = spend * 0.01
            total_spend = spend + commission
            if balance < total_spend:
                print("❌ Недостаточно средств с учетом комиссии.")
            else:
                balance -= total_spend
                history.append(f"Снятие: -{total_spend}")
                print(f"💸 С вас списано {total_spend} (включая 1% комиссию).")
                print(f"Текущий баланс: {balance}")
                operation_count += 1

    elif choice == 4:
        print("👋 Спасибо за использование банкомата. До свидания!")
        history.append("Exit from system.")
        break

    elif choice == 5:
        if history:
            print("📜 История операций:")
            for h in history:
                print(h)
        else:
            print("История пуста.")
            operation_count += 1
    elif choice == 6:
        recive = int(input("Enter your sum for transfer: "))
        if recive > 15000:
            print("Limit for transaction")
        else:
           commission = recive * 0.01
           total = recive + commission
           if balance < total:
             print(f"Сумма вашего перевода, недоступна по причине недостатка средств на вашем балансе. Ваш баланс составляет: {balance}")
           else:
            balance -= total

            receiver_balance += recive
            operation_count += 1
            print(f"Перевод выполнен успешно! \nПереведенно: {recive}, Kомиссии составила: {commission}")
            print(f"Новый баланс получателя: {receiver_balance}")
            history.append(f"Перевод: -{recive} (комиссия {commission})")
    elif choice == 7:
        pas = input("Введите текущий PIN: ")
        if pas != correct_pin:
                print("❌ Неверный текущий PIN.")
        else:
                new_pass = input("Введите новый PIN: ")
                confirm_pass = input("Подтвердите новый PIN: ")
                if new_pass == confirm_pass and new_pass != correct_pin:
                    correct_pin = new_pass
                    print("✅ PIN-код успешно изменён. Не забудьте его!")
                else:
                    print("❌ Новый PIN-код не совпадает или совпадает со старым.")
    elif choice == 8:
        clear = input(f"Вы уверены, что хотите сделать сброс истории операций?\nЕсли - Да(нажмите Y).\nЕсли вы хотите оставить историю операций (нажмите N):")
        if clear.lower() == "y":
            history.clear()
            print("История успешна очищена!")

        else:
            print("Операция отменена.")
            operation_count += 1
    else:
     print("Неверный выбор. Попробуйте снова.")

