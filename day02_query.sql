select * from titles;

select * from titles where title like "senior en%";
select * from employees;
select first_name from employees;


-- VIEW 만들고 조회하기
create view first_name_view as
	select first_name from employees;
select * from first_name_view;

show table status;


-- 조건 SELECT 연습
use sqldb;
select userID, name, addr from usertbl where birthYear >= 1970 and height >= 182;
select userID, name from usertbl where height between 175 and 183;


-- select IN() 사용
select name, addr from usertbl where addr in('경남', '전남', '경북');

select name, height from usertbl order by height desc, name asc;
select * from buytbl;


-- GROUP BY 연습
select userID, sum(amount) from buytbl group by userID;
select userID as '사용자 아이디', sum(amount) as '총 구매개수' from buytbl group by userID order by sum(amount) desc;

create view sum_amount_view as
	select userID as '사용자 아이디', sum(amount) as '총 구매개수' from buytbl group by userID order by sum(amount) desc;
    
select * from sum_amount_view;


-- update 연습
select * from usertbl where name='바비킴';
update usertbl set name='비비킴', birthYear=1980 where userID='BBK';
select * from usertbl;