

"""


output for 9 and 27

m = 27
n = 9
m horizontally and n vertically
m is odd, n is 3*n

d = ".|."


------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------



"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

n = int(n) #9 vertically rows.
m = int(m) #27 horizontally columns .

d = ".|."
welcome = "WELCOME"


#top half





#middle

print(.center(welcome, 27))

#bottom half
