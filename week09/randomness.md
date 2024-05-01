# Randomness

## Comparison Operators
비교 연산의 결과는 bool 값이 나온다.

- assignments statements
- comparison expression
- comparing strings


## Aggregating Comparsion

## Comparing an arry and a value
```jupyterpython
import numpy as np

tosses = np.array(['Tails', 'Head', 'Tails', 'Heads', 'HEadsd'])
tosses == 'Tails'
```
```jupyerpython
np.count_nonzero(tosses == 'Tails')
```


## Random Selection
```jupyterpython
import numpy as np
some_array = [2,3,5]
sample_size = 2
np.random.choice(some_array, sample_size)
```
- select uniformly at random: 모든 원소는 뽑힐 확률이 동일하다(길이가 4이면 25%)
- **with replacement(시험 출제 가능): 첫번째 원소를 선택 후 다시 배열에 집어 넣고 다음 choice 실행**
- from an array,
- a specified number of times: 유한번(size만큼) 반복

```jupyterpython
import numpy as np
a = [2,4,6]
np.random.choice(a, size=None, replace = True, p=None)
```
- a: input
- size: output shape
- **replace: sample replacement(복원 추출)**
- p: probabilities associated with each entry in a, None일경우 uniform distribution

### Uniform Random smaple demo

```jupyterpython
import numpy as np
two_groups = np.array(['treatment','control'])
sum(np.random.choice(two_groups,size=5,replace=True,p=[.6,.4]) == 'control')
```


### Betting on Die
주사위 각각의 숫자가 나올 확률이 동일하다고 생각하는 것이 fiar die이다.

주사위 게임
1. 1~2의 눈: 달러를 잃는다
2. 3~4의 눈: 비김
3. 5~6의 눈: 이김

이 때 function one_bet(x), x = # on the die 를 나타내는 함수를 정의하라
```jupyterpython
def one_bet(x):
    """returns my net gain if the die shows  spots"""
    if x <= 2:
        return -1 # return이 여기서 되지 않는다면 swtich문처럼 계속 내려갈 수도 있다.
    elif x <= 4:
        return 0
    elif x <= 6:
        return 1
```

one roll of fair die
```jupyterpython
np.random.choice(np.arange(1,7))
```

simulating betting on a die

```jupyterpython
one_bet(np.random.choice(np.arange(1,7)))
```

### iteration
```jupyterpython
def bet_on_one_roll():
    """returns my net gain if the die shows  spots"""
    x = np.random.choice(np.arange(1,7))
    if x <= 2:
        return -1 # return이 여기서 되지 않는다면 swtich문처럼 계속 내려갈 수도 있다.
    elif x <= 4:
        return 0
    elif x <= 6:
        return 1

outcomes = np.array([])

for i in range(300):
    outcomes = np.append(outcomes,bet_on_one_roll())
sum(outcomes)

```
**np.append시에 outcomes에 들어가있는 원소의 타입과 bet_on_one_roll()의 타입이 동이랳야 한다.** **np.append(arr, val)의 형태이면 arr에 val을 넣고 np.append(arr1, arr2)의 형식이면 배열 2개를 접붙인다.**

```jupyterpython
import pandas as pd
outcome_table = pd.DataFrame({'Outcome':outcomes})
outcome_table = outcome_table.groupby('Outcome')['Outcome'].count()
outcome_table = outcome_table.reset_index(name='count')
fig = outcome_table.plot.barh(x='Outcome',y='count')
```
pandas를 이용 dataFramd으로 각각의 값들(-1,0,1)이 몇 개가 나왔는지 확인하고 히스토그램을 그릴 수 있다.

## Simulation


## Chance: Basics

- Lowest value: 0, 항상 일어나지 않을 확률
- Highest Values: 1, 항상 일어날 경우
- P(A) = 0.7, A가 일어나지 않을 확률: P(~A) = 1 - 0.7 = 0.3


### Equally likely outcomes

$P(A) = \frac{number\ of\ outcomes\ that\ make\ A\ happen}{totla\number\of\outcomes}$

#### A Question
트럼프 카드 A, K, Q를 가지고 있을 때 Q, K를 차례대로 뽑을 확률(without replacement) 

**Multiplication Rule**
$P(A happens) \times P(B\ happens\ given\ that\ A\ has\ happend)$

Multiplication rule로 인해 계속 조건을 추가하면 확률이 0에 수렴하게 된다. 이러한 문제를 해결하기 위해 log를 이용하여 연산하면 합으로 연산이되므로 0으로 수렴되는 것을 방지할 수 있다.

#### Another Question
카드 A, K, Q가 있을 때 3장 중에서 2장을 뽑았을 때 순서 상관 없이 K 한장 Q 한장을 뽑을 확률은?

**Addition Rule**
$$P(A) = P(first\ way) + P(second\ way)$$

K를 뽑고 Q를 뽑을 확률 + Q를 뽑고 K를 뽑을 확률

### Complement: At Least One Heade
동전 뒤집기를 3번 했을 때 TTT가 나올 확률은 1/8이다. P(TTT) = 1/8, P(~TTT) = 1- P(TTT) = 1- 1/8 - 7/8


### Discussion Question
**Rick and Morty**를 포함하여 100명의 모집단이 있다. 우리는 비복원추출로 2명의 사람을 샘플링한다.

- P(Both Rick and Morty are in sample) = P(first Rick, then Morty) + P(first Morty, then Rick)
= (1/100) * (1/99) + (1/100) * (1/99) = 0.0002

- P(Neither Rick nor Morty is in the sample)
= (98/100) * (97/99) = 0.9602

### The Monty Hall Problem
문 3개 중 1개엔 차가, 2개엔 염소가 있다. 문 하나를 선택한 후 선택하지 않은 문 중 하나를 열어 염소가 있음을 보인 뒤, 다시 선택을 바꿀 수 있는 기회를 주면 바꾸는 것이 유리한가?

처음 고른 문이 당첨일 확률 1/3, 한쪽 문을 연 후 다시 선택을 한다면 해당 확률은 2/3?

복잡한 것은 시뮬레이팅으로 결과를 보자!