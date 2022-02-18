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

select city, sum(order_amount) as total_order_amount from orders group by city order by city;



