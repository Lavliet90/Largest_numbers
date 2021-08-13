'''
The input to the program is a natural number n, and then n different natural numbers, each on a separate line. Write a
program that prints the largest and second largest numbers in a sequence.

Input data format
The input to the program is a natural number n≥2, and then nn different natural numbers, each on a separate line.

Output data format
The program should print the two largest numbers, each on a separate line.
'''
larges=0
last_larges=0
a=int(input())
for i in range(a):
    i=int(input())
    if i>last_larges:
        last_larges = i
    if last_larges>larges:
        larges, last_larges=last_larges, larges
print(larges)
print(last_larges)