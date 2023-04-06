-- Create table departments
	/* id INTEGER Id of the department
	   department STRING Name of the department
	*/
CREATE TABLE departments
(
	id INT NOT NULL,
	department NVARCHAR(128) NOT NULL
)

-- Create table jobs
	/* id INTEGER Id of the job
	   job STRING Name of the job
	*/
CREATE TABLE jobs
(
	id INT NOT NULL,
	job NVARCHAR(128) NOT NULL
)
-- Create table hired_employees
	/* id INTEGER Id of the employee
	   name STRING Name and surname of the employee
	   datetime STRING Hire datetime in ISO format
	   department_id INTEGER Id of the department which the employee was hired for
	   job_id INTEGER Id of the job which the employee was hired for
	*/

CREATE TABLE hired_employees
(
	id INT NOT NULL,
	name NVARCHAR(256) NOT NULL,
	datetime NVARCHAR(128) NOT NULL, 
	department_id INT NOT NULL,
	job_id INT NOT NULL
)
