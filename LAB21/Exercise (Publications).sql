CREATE DATABASE publications;
USE publications;

Select pubs.pub_name, COUNT(titles.title_id) AS Titles
From publications.publishers pubs
LEFT JOIN publications.titles titles
ON pubs.pub_id = titles.pub_id GROUP BY pubs.pub_name;

Select *
From publications.employee emp 
LEFT JOIN publications.jobs job 
ON emp.job_id = job.job_id
UNION
Select *
From publications.employee emp 
RIGHT JOIN publications.jobs job 
ON emp.job_id = job.job_id;
 
Select pubs.pub_name, COUNT(titles.title_id) AS Titles
From publications.publishers pubs
INNER JOIN publications.titles titles
ON pubs.pub_id = titles.pub_id GROUP BY pubs.pub_name;