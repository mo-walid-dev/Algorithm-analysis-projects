import heapq
import random
import time

k = 10

vocab = [f"word{i}" for i in range(1, 50_001)]
words = random.choices(vocab, weights=[1 / i for i in range(1, 50_001)], k=1_000_000)

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

start = time.perf_counter()
heap = []
for word, c in counts.items():
    if len(heap) < k:
        heapq.heappush(heap, (c, word))     
    elif (c, word) > heap[0]:                
        heapq.heapreplace(heap, (c, word))  
top = sorted(heap, reverse=True)             
heap_time = time.perf_counter() - start

for c, w in top:
    print(f"{w:10} {c}")

start = time.perf_counter()
full = sorted(((c, w) for w, c in counts.items()), reverse=True)[:k]
sort_time = time.perf_counter() - start

print(f"\nunique words: {len(counts)}")
print(f"heap:      {heap_time:.4f} s")
print(f"full sort: {sort_time:.4f} s")
print("same result:", top == full)
