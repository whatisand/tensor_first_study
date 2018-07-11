from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100,40,30,54,25,3,100,100,100,3,3,4,64,23,6,3,2,32,6,87,47,38,82]
friend_count = Counter(num_friends)


def mean(x: list) -> float:
    return sum(x) / len(x)


def median(x: list) -> int:
    sort = sorted(x)
    return sort[len(x)//2]


def variance(x: list) -> float:
    pass


print(friend_count)

plt_x = range(101)
plt_y = [friend_count[i] for i in plt_x]


max_friends = max(num_friends)
min_friends = min(num_friends)

print("mean : ", mean(num_friends))
print("median", median(num_friends))

plt.bar(plt_x, plt_y)
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()