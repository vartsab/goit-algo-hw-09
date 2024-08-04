import time
import random

# Жадібний алгоритм для видачі решти
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin
    return result

# Динамічне програмування для видачі решти
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація масиву для мінімальної кількості монет
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    # Ініціалізація масиву для відстеження номіналів монет
    coin_count = [{} for _ in range(amount + 1)]

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and min_coins[a - coin] + 1 < min_coins[a]:
                min_coins[a] = min_coins[a - coin] + 1
                coin_count[a] = coin_count[a - coin].copy()
                if coin in coin_count[a]:
                    coin_count[a][coin] += 1
                else:
                    coin_count[a][coin] = 1

    return coin_count[amount]

# Оцінка часу роботи алгоритмів
def evaluate_algorithms(amounts):
    print(f"{'Amount':<10}{'Greedy Time':<15}{'DP Time':<15}")
    print("="*40)

    for amount in amounts:
        start_time = time.time()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.time() - start_time

        start_time = time.time()
        dp_result = find_min_coins(amount)
        dp_time = time.time() - start_time

        print(f"{amount:<10}{greedy_time:<15.6f}{dp_time:<15.6f}")

        print(f"Greedy result for {amount}: {greedy_result}")
        print(f"DP result for {amount}: {dp_result}")
        print("-"*40)

# Основна частина програми
def main():
    # Згенеруємо 5 випадкових чисел amount, які різняться на порядок
    amounts = [random.randint(1, 10**i) for i in range(1, 6)]

    # Оцінка часу роботи алгоритмів
    evaluate_algorithms(amounts)

    # Висновок
    print("\nВисновок:")
    print("Жадібний алгоритм зазвичай швидший для невеликих сум через простоту реалізації, але не завжди оптимальний.")
    print("Алгоритм динамічного програмування завжди знаходить оптимальне рішення, але може бути повільнішим, особливо для великих сум.")

if __name__ == "__main__":
    main()
