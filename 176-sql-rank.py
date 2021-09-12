"""
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
SELECT SecondHighestSalary FROM
(
SELECT Salary as SecondHighestSalary, rank() over (partition by Salary order by Salary asc) as r
FROM Employee
) a
where r = 2
"""