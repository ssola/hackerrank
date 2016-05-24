# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_balanced(test_case):
    stack = []
    reversed = {')': '(', ']': '[', '}': '{'}
    
    for char in test_case:
        if char in('(', '[', '{'):
            stack.append(char)

        if char in(')', ']', '}'):
            # Check if we have any open character
            if stack.count(reversed[char]):
                stack.pop()
            else:
                stack.append(char)
            
    if not stack:
        return True
    
    return False

num_tests = int(raw_input())

for _ in xrange(num_tests):
    test_case = raw_input()
    if is_balanced(test_case):
        print 'YES'
    else:
        print 'NO'
