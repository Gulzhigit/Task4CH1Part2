def time(h1,h2,m1,m2,s1,s2):
    hour = ((h1-h2) * 3600) + ((m1- m2) * 60) + (s1 - s2)
    print(hour)
time(6, 6, 2, 1, 10, 30)