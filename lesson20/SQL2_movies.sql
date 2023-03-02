create table directors (
	--primary key
	id serial primary key,
	name varchar(256) not null,
	birth_date date,
	oscars smallint default 0
);

create table serieses(
	id serial primary key,
	name varchar(256)
);

create table movies (
	--primary key
	id serial primary key,
	name varchar(256) not null,
	release_date date not null,
	description varchar,
	genre varchar(64) not null,
	duration smallint check (duration > 0),
	director_id int not null,
	foreign key (director_id) references directors(id),
	series_id int,
	foreign key (series_id) references serieses(id)
);


INSERT INTO public.serieses
("name")
VALUES('Die Hard');

INSERT INTO public.serieses
("name")
VALUES('Lethal Weapon');

select *
from movies m
full join directors d on d.id =m.director_id  
full join serieses s on s.id =m.series_id ;

select s."name" , count(m.id) 
from serieses s 
left join movies m 
on s.id =m.series_id 
group by s."name" ;

select d."name" , count(m.id) 
from directors d  
left join movies m 
on d.id =m.director_id
group by d."name" ; 


select d."name" , count(m.id), count(distinct(s.id))  
from 
	directors d left join movies m  
	on m.director_id =d.id 
	left join serieses s 
	on m.series_id =s.id 
group by d."name" ;


select m."name" , d."name" ,s."name" 
from movies m join directors d 
on d.id =m.director_id 
right join serieses s 
on s.id =m.series_id 
where s."name" in 
	(select s2."name" from movies m2 join directors d2
					on d2.id =m2.director_id
					right join serieses s2
					on s2.id =m2.series_id 
					group by s2."name" 
					having count(s2.id)>1);

select m."name",  d."name"  
from movies m left join serieses s 
on s.id =m.series_id 
join directors d 
on m.director_id =d.id 
where s."name" is null ;

