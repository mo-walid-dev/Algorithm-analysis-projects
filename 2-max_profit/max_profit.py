import pandas as pd

df = pd.read_csv("max profit prices.csv")
prices = df["price"].tolist()
changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

def max_sub(a, lo, hi):
    if lo == hi:
        return a[lo], lo, hi
    mid = (lo + hi) // 2
    left, right = max_sub(a, lo, mid), max_sub(a, mid + 1, hi)

    s, bl, l = 0, float("-inf"), mid        
    for i in range(mid, lo - 1, -1):
        s += a[i]
        if s > bl:
            bl, l = s, i
    s, br, r = 0, float("-inf"), mid + 1     
    for j in range(mid + 1, hi + 1):
        s += a[j]
        if s > br:
            br, r = s, j

    return max(left, right, (bl + br, l, r)) 


profit, buy, end = max_sub(changes, 0, len(changes) - 1)
sell = end + 1  # changes[i] = prices[i+1] - prices[i]
print(f"Divide & conquer: buy {df.date[buy]} ({prices[buy]}), "
      f"sell {df.date[sell]} ({prices[sell]}), profit {profit:.2f}")

low, best = 0, (0, 0, 0)
for i, p in enumerate(prices):
    if p - prices[low] > best[0]:
        best = (p - prices[low], low, i)
    if p < prices[low]:
        low = i

print(f"Linear scan     : buy {df.date[best[1]]} ({prices[best[1]]}), "
      f"sell {df.date[best[2]]} ({prices[best[2]]}), profit {best[0]:.2f}")
