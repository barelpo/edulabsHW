select * from superstore_data sd ;

select id from superstore_data sd ;

select * from superstore_data where year_birth < 1940 ;

select kidhome + teenhome as total_children, teenhome ,kidhome  from superstore_data sd ;

select income / 1000.0 from superstore_data sd ;

select now();

--2
select count(*) 
from superstore_data sd ;

--3
select *
from superstore_data sd 
limit 10;

--4
select *
from superstore_data sd 
limit 25
offset 20;

--5
select year_birth , id , marital_status 
from superstore_data sd 
limit 20;

--6
select id, mntwines 
from superstore_data sd 
where mntwines > 1000;

--7
select
(extract (year from now()) - year_birth), marital_status
from 
superstore_data
where 
mntmeatproducts > 500 and mntfishproducts < 500;

--8
select 
count(id)
from
superstore_data sd 
where 
response = 1;

--9
select education, count(id)  
from superstore_data
group by education
order by education ;

--10
select *
from superstore_data sd 
where year_birth = (select max(year_birth) from superstore_data sd2);

--11
select id, marital_status, (extract (year from now()) - year_birth)
from superstore_data sd 
where year_birth = (select min(year_birth) from superstore_data sd2);

--12
select avg(income) 
from superstore_data sd
where complain > 0;

--13
select sum(kidhome)
from superstore_data sd ;

--14
select id, income ,marital_status ,(extract (year from now()) - year_birth), numwebpurchases, numstorepurchases
from superstore_data sd 
where 
numwebpurchases > numstorepurchases ;

--15
select kidhome + teenhome as children, id , recency 
from superstore_data sd 
where 
recency <=30;

--16
select count(id) 
from superstore_data sd
where mntfishproducts =0 or mntmeatproducts =0;

--17
select *
from superstore_data sd 
where mntgoldprods = (select max(mntgoldprods) from superstore_data sd2 );

--18
select id, (extract (year from now()) - year_birth) as age
from superstore_data sd 
where 20<=(extract (year from now()) - year_birth)and (extract (year from now()) - year_birth)<=40
order by age; 

--19
select distinct (year_birth)
from superstore_data sd ;

--20
select *
from superstore_data sd 
order by mntsweetproducts desc  
limit 10;

--21
select count(*), marital_status  
from superstore_data sd 
group by
marital_status ;

--22
select sum(mntsweetproducts), education 
from superstore_data sd 
group by education ;

--23
select (extract (year from now()) - min(year_birth)) as maxage, (extract (year from now()) - max(year_birth)) as minage, marital_status
from superstore_data sd 
group by marital_status;

--24
select count(*), year_birth 
from superstore_data sd 
where response =1 and complain =0
group by year_birth
order by year_birth ;

--25
select (extract (year from now()) - max(year_birth)) as minage, education
from superstore_data sd 
group by education;

--26
select avg(mntwines), avg(mntfruits), avg(mntmeatproducts), avg(mntfishproducts), avg(mntsweetproducts), avg(mntgoldprods), teenhome +kidhome as children 
from superstore_data sd 
group by (teenhome+kidhome)

--27
select (extract (year from now()) - max(year_birth)) as minage, teenhome
from superstore_data sd 
group by teenhome ;

--28
select count(response), response 
from superstore_data sd
group by response ;

--29
select avg(teenhome) as avgteen, avg(kidhome) as avgkid, marital_status  
from superstore_data sd 
group by marital_status ;

--30
select min(income), max(income), avg(income)  , education 
from superstore_data sd 
group by education ;

