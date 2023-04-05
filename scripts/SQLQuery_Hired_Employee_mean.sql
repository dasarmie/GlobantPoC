-- List of ids that hired more employees than the mean in 2021

DECLARE @mean INT;
/* The mean of employees hired in 2021 */ 
SET @mean =  
(SELECT AVG(hired) AS mean
FROM
(
	SELECT d.id
	 , d.department
	 , COUNT(he.id) AS hired
	FROM dbo.hired_employees AS he
	LEFT JOIN dbo.departments AS d
	ON he.department_id = d.id
	WHERE YEAR(he.datetime) = 2021
	GROUP BY d.id, d.department
) AS MeanHired);

SELECT d.id
	 , d.department
	 , COUNT(he.id) AS hired
FROM dbo.hired_employees AS he
LEFT JOIN dbo.departments AS d
ON he.department_id = d.id
WHERE YEAR(he.datetime) = 2021
GROUP BY d.id, d.department
HAVING COUNT(he.id) >= @mean
ORDER BY hired DESC