# so much faster with yield instead of  list
def partitionGenerator(n, offset=1):
    yield n,
    for i in range(offset, n // 2 + 1):
        for p in partitionGenerator(n - i, i):
            yield p+(i,)



partitions = sorted(partitionGenerator(20), reverse=True)
for p in partitions:
    print(p)