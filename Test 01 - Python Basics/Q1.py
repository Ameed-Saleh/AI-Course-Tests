'''
Question 1
'''
RED = "\033[0;31m"
YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"
BLUE = "\033[0;34m"
RESET = "\033[0;0m"
import statistics
valid_grades = []
count = 0
while True:
    try:
        grade = int(input(f"\n{YELLOW}Enter a grade (or -999 to exit): {RESET}"))
        if grade == -999:
            if len(valid_grades) < 10:
                print(f"{RED}Need at least 10 valid grades. keep entering{RESET}")
                continue
            break
        if grade < 0 or grade > 100:
            print(f"{RED}Not in range. skip!{RESET}")
            continue
        count += 1
        print(f"{CYAN}number of your valid grades is {RED}{count}{RESET}")
        valid_grades.append(grade)
    except ValueError:
        print(f"{RED}Invalid grade. keep entering!{RESET}")
        continue
print(f"\n{BLUE}valid_grades  = {valid_grades}{RESET}")
print(f"\n{CYAN}Number of valid grades = {RED}{len(valid_grades)}{RESET}")
print(f"{CYAN}Class average = {RED}{statistics.mean(valid_grades):.2f}{RESET}")
print(f"{CYAN}Highest grade= {RED}{max(valid_grades)}{RESET}")
