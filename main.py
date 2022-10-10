numbers = list(map(int, input().split()))
sum = 0
for i in range(len(numbers)):
    sum += i
average = sum/len(numbers)
dist = []
for x in range(len(numbers)):
    if average > numbers[x]:
        dist.append(int(average - numbers[x]))
    else:
        dist.append(int(numbers[x] - average))
for j in range(len(numbers)):
    print(f'{dist[j]:.2f}', end=" ")
# ******************************
# Make your Code
# ******************************


# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
