select old.cnt - new.cnt from (select count(*) as cnt from old_table) old cross join (select count(*) as cnt from new_table) new;

select column1, record_count, sum(record_count) over() as total_record from (select column1, count(*) as record_count from table1 WHERE column1 like '%AB%' group by column1 union all select column1, count(*) as record_count from table1 WHERE column1 like '%BC%' group by column1 union all select column1, count(*) as record_count from table1 WHERE column1 like '%CD%' group by column1) as t2;

