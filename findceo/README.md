# FINDCEO (Find the CEO)

There exists a startup called SHADYLLC. SHADYLLC employs at least one employee.
It follows the following hierarchical structure for its employees.

- The company employs at least one employee.
- The company has a number of managers. Each manager can have upto two immediate subordinates working for him.
- Each subordinate can also be a manager.

The HR of the company has suddenly forgotten who is the CEO of the company. The CEO of the company is the employee who reports to nobody and has no manager.

However the HR has the following information with them.
- The HR knows the salary of each employee.
- The HR also knows the sum of the salaries of every manager's immediate subordinates.
- The HR also had ensured that every employee has a unique salary.

Help them shortlist the possible CEOs of the company.

## Input

The test file will have input cases as:
First line will be T, where T : Number of test cases.
Each test case begins with N, where N : Number of employees in the company,
followed by N lines containing the salary of the employee (X) and the sum of the salary of their immediate subordinates.

## Output

For each test case, output on a line a space separated list of all possible values for the salary of the CEO node in increasing order. It is guaranteed that at least one CEO exists for each test case.


## Constraints:
1 <= T <= 50

1 <= Ni <= 30

X is between 1 and 1000000.


## Sample Test Case:

```
TEST CASE 1

2
1
4000 0
6
1000 5000
4000 0
2000 0
3000 0
5000 5000
6000 5000

SAMPLE OUTPUT

4000
6000

```
