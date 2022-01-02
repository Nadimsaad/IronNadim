CREATE database cancellation_rate;
USE cancellation_rate;

CREATE TABLE users (user_id INT NOT NULL, action VARCHAR(20) NOT NULL, date Date);

INSERT INTO users (user_id, action, date)
VALUES 	(1, 'start','2020-01-01'),
		(1, 'cancel','2020-02-01'),
		(2, 'start','2020-03-01'),
		(2, 'publish','2020-04-01'),
		(3, 'start','2020-06-01'),
		(3, 'cancel','2020-07-01'),
		(4, 'start','2020-07-01');

## Task 1: Write a query to return the publication & cancellation rate for each user

SELECT * FROM users;
SELECT user_id, (sum(action = 'publish')/ sum(action = 'start')) AS publishing_rate, 
				(sum(action = 'cancel')/ sum(action = 'start')) AS cancelling_rate FROM users
GROUP BY user_id;

## Task 2: Time difference between latest actions

CREATE TABLE time_difference 
(user_id INT, 
action VARCHAR(20), 
action_date Date);

INSERT INTO time_difference (user_id, action, action_date)
VALUES  (1, 'start', CAST('2020-02-12' AS Date)),
		(1, 'cancel', CAST('2020-02-13' AS Date)),
		(2, 'start', CAST('2020-02-11' AS Date)),
		(2, 'publish', CAST('2020-02-14' AS Date)),
		(3, 'start', CAST('2020-02-15' AS Date)),
		(3, 'cancel', CAST('2020-02-15' AS Date)),
		(4, 'start', CAST('2020-02-18'AS Date)),
		(1, 'publish', CAST('2020-02-19' AS Date));

## I don't how to proceed from here :(

## Task 3: Create an SQL query that shows the TOP 3 authors who sold the most books in total

CREATE TABLE authors (author_name CHAR(50), book_name CHAR(50));

INSERT INTO authors (author_name, book_name)
VALUES 	('author_1', 'book_1'),
		('author_1', 'book_2'), 
		('author_2', 'book_3'), 
		('author_2', 'book_4'), 
		('author_2', 'book_5'), 
		('author_3', 'book_6');

CREATE TABLE books (book_name CHAR(50), sold_copies CHAR(50));

INSERT INTO books (book_name, sold_copies)
VALUES 	('book_1', 1000),
		('book_2', 1500), 
		('book_3', 34000), 
		('book_4', 29000), 
		('book_5', 40000), 
		('book_6', 4400);

SELECT author_name, sum(sold_copies) as total_sold_copies from authors
LEFT JOIN books AS books
ON authors.book_name = books.book_name
GROUP BY author_name
ORDER by total_sold_copies DESC
LIMIT 3;

## Task 4: Show every department where the average salary per employee is lower than $500

CREATE TABLE employees (department_name CHAR(50), employee_id INT, employee_name CHAR(50));

INSERT INTO employees (department_name, employee_id, employee_name)
VALUES 	('Sales', 123, 'John Doe'),
		('Sales',211, 'Jane Smith'),
		('HR',556, 'Billy Bob'),
		('Sales',711,'Robert Hayek'),
		('Marketing',235,'Edward Jorgson'),
		('Marketing', 236, 'Christine Packard');

CREATE TABLE salaries (salary INT, employee_id INT, employee_name CHAR(50));

INSERT INTO salaries (salary, employee_id, employee_name)
VALUES 	(500,123,'John Doe'),
		(600,211,'Jane Smith'),
		(1000,556,'Billy Bob'),
		(400,711,'Robert Hayek'),
		(1200,235,'Edward Jorgson'),
		(200,236,'Christine Packard');

## Look in every department where avg sal/ empl <= $500

SELECT department_name, avg(salary) AS average_salary
FROM employees
JOIN salaries AS salaries 
ON employees.employee_id = salaries.employee_id
GROUP BY department_name
HAVING AVG(salary) < 500; ## From the given sample only Sales has an average salary of 500.
## However, the above formula is valid for the 546 rows of the dataset as we assume that the answer will
## be different 
