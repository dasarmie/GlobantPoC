-- Number of employees hired by quarter in 2021
SELECT department
	 , job
	 , [Q1]
	 , [Q2]
	 , [Q3]
	 , [Q4]
FROM
(
	SELECT d.department
		 , j.job
         , he.id
		 , CONCAT('Q', DATEPART(QUARTER, he.datetime)) AS quarter_year
	FROM dbo.hired_employees AS he
	LEFT JOIN dbo.departments AS d
	ON he.department_id = d.id
	LEFT JOIN dbo.jobs AS j
	ON he.job_id = j.id
	WHERE YEAR(he.datetime) = 2021
) AS Employees
PIVOT
(
	COUNT(id)
	FOR quarter_year IN ([Q1], [Q2], [Q3], [Q4])
) AS EmployeesQuarter
ORDER BY department, job;
