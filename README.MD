# goit-algo-hw-09

# Greedy Algorithms and Dynamic Programming

## Introduction
This project compares the efficiency of the greedy algorithm (`find_coins_greedy`) and the dynamic programming (`find_min_coins`) in solving the problem of giving change with a set of coin denominations [50, 25, 10, 5, 2, 1]. The objective is to evaluate their performance in terms of execution time and computational complexity, especially when dealing with large amounts.

## Algorithms
### Greedy Algorithm (`find_coins_greedy`)
- **Time Complexity**: O(N), where N is the number of coin denominations.
- **Advantages**: Fast and simple to implement.
- **Disadvantages**: Does not always yield the optimal result for certain sets of coin denominations.
- **Performance with Large Amounts**: Generally efficient but dependent on the set of coins.

### Dynamic Programming Algorithm (`find_min_coins`)
- **Time Complexity**: O(N * M), where N is the number of coin denominations and M is the amount to be given as change.
- **Advantages**: Always finds the optimal distribution of coins.
- **Disadvantages**: More complex and requires more memory and time, especially for large amounts.
- **Performance with Large Amounts**: Consistently effective in finding the minimum number of coins.

## Comparison and Conclusions
|Amount|Greedy|DP|
|-----|----------|------|
|Time for 2:|0.000000|0.000000|
|Result for 2:|{2: 1}|{2: 1}|
|Time for 76:|0.000000|0.000000|
|Result 76:|{50: 1, 25: 1, 1: 1}|{1: 1, 25: 1, 50: 1}|
|Time for 635|0.000000|0.005186|
|Result for 635:|{50: 12, 25: 1, 10: 1}|{10: 1, 25: 1, 50: 12}|
|Time for 2479|0.000000|0.002999|
|Result for 2479:|{50: 49, 25: 1, 2: 2}|{2: 2, 25: 1, 50: 49}|
|Time for 61207|0.000000|0.095514|       
|Result for 61207:|{50: 1224, 5: 1, 2: 1}|{2: 1, 5: 1, 50: 1224}|

### Conclusions
The greedy algorithm can be faster for smaller amounts and is easy to implement, but it does not always guarantee an optimal result. On the other hand, the dynamic programming algorithm consistently finds the minimum number of coins needed but may be slower, particularly for larger amounts. Both algorithms have their strengths and weaknesses, and the choice between them depends on the specific requirements of the problem.
