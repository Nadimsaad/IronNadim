Select order_id, product_id, price from olist.order_items 
order by price DESC 
limit 1;
Select order_id, product_id, price from olist.order_items 
order by price ASC 
limit 1;

Select shipping_limit_date from olist.order_items 
order by shipping_limit_date DESC;

Select customer_state, customer_city, count(customer_unique_id) from olist.customers 
where customer_state = 'SP' 
group by customer_city 
order by count(customer_unique_id) DESC;

Select customer_state, customer_city, count(customer_unique_id) from olist.customers 
where customer_state = 'SP' 
group by customer_city 
order by count(customer_city) DESC;

Select business_segment, count(business_segment) from olist.closed_deals 
WHERE business_segment <> "NULL" 
group by business_segment;

Select sum(declared_monthly_revenue), business_segment from olist.closed_deals 
where declared_monthly_revenue >0 
group by business_segment 
order by sum(declared_monthly_revenue) DESC limit 3;

Alter Table olist.order_reviews
ADD review_desc text First;
Select review_score, count(distinct review_id) from olist.order_reviews 
group by review_score;

Select count(review_desc), review_desc, review_score from olist.order_reviews 
Group by review_desc
Order by count(review_desc) DESC
Limit 1;

Select review_id, review_score, count(distinct review_id) from olist.order_reviews group by review_score;