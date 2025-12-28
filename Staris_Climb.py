# At a time only one or two stairs can be climbed

ladders = int(input("Enter Number of ladders: "))

def cal(n, ladder, steps):
    if n == ladder:
        return steps
    if (ladder - n) >= 2:
        return cal(n + 2, ladder, steps + 1)
    else:
        return cal(n + 1, ladder, steps + 1)

print(cal(0, ladders, 0))
