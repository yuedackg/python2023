s={i for i in range(2,101)}
print(s)
for lp in range (2,101):
    M={k for k in range(2*lp,101,lp)}
    s=s-M
print(s)
s={k for k in range(2,10001)}
print(s)
for lp in range (2,10001):
    M={k for k in range(2*lp,10001,lp)}
    s=s-M
print(s)