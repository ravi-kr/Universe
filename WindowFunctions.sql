-- Aggregate Window Functions
-- SUM(), MAX(), MIN(), AVG(), COUNT()
-- Ranking Window Functions
-- RANK(), DENSE_RANK(), ROW_NUMBER(), NTILE()
-- Value Window Functions
-- LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE()

create database universe;
show databases;
use universe;

drop table orders;

create table orders(
order_id INT,
order_date DATE,
customer_name VARCHAR(256),
city VARCHAR(256),
order_amount INT
);

insert into orders
select '1001', '2017-04-01', 'RK', 'Delhi', 10000
union all
select '1002', '2017-04-02', 'PS', 'Kolkata', 20000
union all
select '1003', '2017-04-03', 'PJ', 'Chennai', 50000
union all
select '1004', '2017-04-04', 'SK', 'Bangalore', 15000
union all
select '1005', '2017-04-05', 'AB', 'Chennai', 7000
union all
select '1006', '2017-04-06', 'KK', 'Bangalore', 25000
union all
select '1007', '2017-04-07', 'SP', 'Kolkata', 15000
union all
select '1008', '2017-04-08', 'SM', 'Kolkata', 20000
union all
select '1009', '2017-04-09', 'LG', 'Chennai', 1000
union all
select '1010', '2017-04-10', 'SL', 'Delhi', 500;

select city, sum(order_amount) total_order_amount from orders group by city;

select order_id, order_date, customer_name, city, order_amount, sum(order_amount) over(partition by city) as grand_total from orders;

select order_id, order_date, customer_name, city, order_amount, avg(order_amount) over(partition by city, month(order_date)) as average_order_amount from orders;

select order_id, order_date, customer_name, city, order_amount, min(order_amount) over(partition by city) as minimum_order_amount from orders;

select order_id, order_date, customer_name, city, order_amount, max(order_amount) over (partition by city) as maximum_order_amount from orders;

select city, count(distinct customer_name) number_of_customers from orders group by city;

select order_id, order_date, customer_name, city, order_amount, count(order_id) over (partition by city) as total_orders from orders;

select order_id, order_date, customer_name, city, order_amount, count(distinct customer_name) over(partition by city) as number_of_customers from orders;

select order_id, order_date, customer_name, city, rank() over (order by order_amount desc) rank from orders;

select order_id, order_date, customer_name, city, order_amount, dense_rank() over(order by order_amount desc) rank from orders;

select order_id, order_date, customer_name, city, order_amount, row_number() over(order by order_id) row_number from orders;

select order_id, order_date, customer_name, city, order_amount, row_number() over(partition by city order by order_amount desc) row_number from orders;

select order_id, order_date, customer_name, city, order_amount, ntile(4) over(order by order_amount) row_number from orders;

select order_id, customer_name, city, order_amount, order_date, lag(order_Date,1) over(order by order_Date) prev_order_Date from orders;

select order_id, customer_name, city, order_amount, order_date, lead(order_date, 1) over(order by order_date) next_order_Date from orders;

select order_id, order_Date, customer_name, city, order_amount, first_value(order_Date) over(partition by city order by city) first_order_Date, last_value(order_date) over(partition by city order by city) last_order_date from orders;



