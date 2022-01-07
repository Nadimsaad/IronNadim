CREATE DATABASE Lab3_Module2;

USE Lab3_Module2;

CREATE TABLE Score_of_Students (student_id INT, score INT);
 
INSERT INTO Score_of_Students (student_id, score) VALUES 
(1,91),
(2,72),
(3,98),
(4,62),
(5,62),
(6,95),
(7,83),
(8,86),
(9,56),
(10,97),
(11,58),
(12,71),
(13,87),
(14,83),
(15,98);

SELECT AVG(score), MIN(score), MAX(score), SUM(score), STDDEV(score), VARIANCE(score) FROM Score_of_Students ;
