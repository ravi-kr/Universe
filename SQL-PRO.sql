select old.cnt - new.cnt from (select count(*) as cnt from old_table) old cross join (select count(*) as cnt from new_table) new;

select column1, record_count, sum(record_count) over() as total_record from (select column1, count(*) as record_count from table1 WHERE column1 like '%AB%' group by column1 union all select column1, count(*) as record_count from table1 WHERE column1 like '%BC%' group by column1 union all select column1, count(*) as record_count from table1 WHERE column1 like '%CD%' group by column1) as t2;

SELECT
palms AS sweaty,
knees AS weak,
arms AS heavy,
MAX(vomit) OVER (PARTITION BY sweater, already, moms_spaghetti) AS nervous,
CASE
WHEN on_the_surface THEN ‘looks calm and ready’
ELSE ‘drop bombs’
END AS keeps_on_forgetting,
what_he_wrote_down,
crowd AS loud,
CASE
WHEN mouth = ‘open’ AND words IS NULL THEN ‘choking’
WHEN everyone = ‘joking’ AND clock = ‘run out’ AND time = ‘up’ THEN ‘over’
ELSE bloah
END,
snap,
back
FROM reality;
