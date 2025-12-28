import random
count_heads = 0
count_tails = 0
history = []
for i in range(1, 1001):
    if random.random() <= 0.5:
        count_heads += 1
        current_average = count_heads / i
        history.append(current_average)
    else:
        count_tails += 1
import matplotlib.pyplot as plt
plt.plot(history)
plt.axhline(0.5, color='r', linestyle='--')

# 3. Add labels so we know what we are looking at
plt.title("Law of Large Numbers: Settling Down")
plt.ylabel("Heads Probability")
plt.xlabel("Number of Flips")

# 4. Show the window
plt.show()