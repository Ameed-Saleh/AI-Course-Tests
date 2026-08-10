'''
Question 4
'''
RED = "\033[0;31m"
YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"
RESET = "\033[0;0m"

list1 = []
while True:
    str1: str = input(f"{YELLOW }enter a string (or 'q' to quit):{RESET} ")
    str1 = str1.lower()
    if str1 == 'q':
        print(f"{RED}you have quit!{RESET}\n")
        break
    if len(str1) == 0:
        print(f"{RED}you entered without string!!{RESET}\n")
        continue
    list1.append(str1)

if len(list1) > len(set(list1)):
    print(f"{CYAN}there were duplicate elements!!{RESET}")
else:
    print(f"{CYAN}there were no duplicate elements!!{RESET} ")


