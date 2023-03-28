# 1번
def grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C" 
    elif score >= 60 and score <= 69:
        return "D" 
    else:
        return "F"

# 2번
def quadrant(x, y):
    if x >0:
        if y>0:
            return "제 1사분면"
        else:
            return "제 4사분면"
    else:
        if y>0:
            return "제 2사분면"
        else:
            return "제 3사분면"

# 3번
def leapYear(year):
    if int(year)%4 == 0:
        if int(year)%100 == 0 and int(year)%400 != 0:
            return "윤년이 아닙니다."
        else:
            return "윤년입니다."
    else: 
        return "윤년이 아닙니다."

# 4번
def dice(a, b, c):
    if a==b and b==c:
        return 10000+1000*a
    elif a==b:
        return 1000+100*a
    elif b==c:
        return 1000+100*b
    elif a==c:
        return 1000+100*a
    elif a!=b and b!=c and c!=a:
        return max([a,b,c])*100

# 5번
def alarm(time):
    time = str(time)
    if len(time) == 3:
        time = "0"+time
    elif len(time) == 2:
        time = "00"+time
    elif len(time) == 1:
        time = "000"+time
    h,m=int(time[0:2]),int(time[2:4])
    if m-45<0:
        m = m+15
        if h-1<0:
            return "23시 "+str(m)+"분"
        else: 
            return str(h-1)+"시 "+str(m)+"분"
    else: 
        return str(h)+"시 "+str(m-45)+"분"
