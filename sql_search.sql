with tmp as
(SELECT employee, salary, max(date)
FROM salaries
GROUP BY employee
limit 1)

select head, e.employee, salary from employees as e
RIGHT join tmp
on e.employee = tmp.employee