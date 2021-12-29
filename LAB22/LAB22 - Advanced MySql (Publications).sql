
## Challenge 1 - Most Profiting Authors
USE publications;
SELECT t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
FROM titles t
INNER JOIN sales s on s.title_id = t.title_id
INNER JOIN titleauthor ta on ta.title_id = s.title_id
INNER JOIN authors a on a.au_id = ta.au_id
ORDER BY t.title_id, a.au_id;

SELECT title_id, au_id, au_lname, au_fname, advance, sum(ROYALTIES) as ROYALTIES from (
	SELECT t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
	FROM titles t
	INNER JOIN sales s on s.title_id = t.title_id
	INNER JOIN titleauthor ta on ta.title_id = s.title_id
	INNER JOIN authors a on a.au_id = ta.au_id
) as tmp
GROUP BY au_id, title_id;

SELECT au_id as "AUTHOR ID", au_lname as "LAST NAME", au_fname as "FIRST NAME", sum(advance + ROYALTIES) as PROFITS from (
	SELECT title_id, au_id, au_lname, au_fname, advance, sum(ROYALTIES) as ROYALTIES from (
		SELECT t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
		FROM titles t
		INNER JOIN sales s on s.title_id = t.title_id
		INNER JOIN titleauthor ta on ta.title_id = s.title_id
		INNER JOIN authors a on a.au_id = ta.au_id
	) as tmp
	GROUP BY au_id, title_id
) as tmp2
GROUP BY au_id
ORDER BY PROFITS DESC
LIMIT 3;

## Challenge 2 - Alternative Solution

DROP TEMPORARY TABLE if exists tmp1;

CREATE TEMPORARY TABLE tmp1
SELECT t.title_id, a.au_id, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as sale_royalty
FROM titles t
INNER JOIN sales s on s.title_id = t.title_id
INNER JOIN titleauthor ta on ta.title_id = s.title_id
INNER JOIN authors a on a.au_id = ta.au_id
ORDER BY t.title_id, a.au_id;

DROP TEMPORARY TABLE if exists tmp2;

CREATE TEMPORARY TABLE tmp2
SELECT title_id, au_id, sum(sale_royalty) as ROYALTIES
FROM tmp1
GROUP BY title_id, au_id;

SELECT tmp2.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME", sum(t.advance + ROYALTIES) as PROFITS 
FROM tmp2
INNER JOIN titles t on t.title_id = tmp2.title_id
INNER JOIN authors a on a.au_id = tmp2.au_id
GROUP BY tmp2.au_id
ORDER BY PROFITS DESC
LIMIT 3;