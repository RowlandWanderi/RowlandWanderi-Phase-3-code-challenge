#define a function that returns True if two out of three input numbers are positive
def positives(a,b,c):
#count the number of positive integers(numbers greater than zero)
    count= sum(1 for number in (a,b,c) if number>0)
#if the count is equal to two return true
    if count == 2:
        return True
#if the count is less than two return false
    else:
        return False

result = positives (1,-3,-8)
print(result)