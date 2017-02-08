n = int(input())
a = [ (lambda x: {list(x.split())[0]:list(x.split())[1]})(input()) for i in range(n)]
print(a[0].get('aa'))