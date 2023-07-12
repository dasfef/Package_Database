CREATE SCHEMA shopdb;

-- create table memberTBL
CREATE TABLE memberTBL(
	memberID CHAR(8) NOT NULL PRIMARY KEY,
	memberName CHAR(5) NOT NULL,
	memberAddress CHAR(20) NULL
) ENGINE=INNODB;

-- create table productTBL
CREATE TABLE productTBL(
	productName CHAR(4) NOT NULL PRIMARY KEY,
	cost INT NOT NULL,
	makeDate DATE NULL,
	company CHAR(5) NULL,
	amount INT NOT NULL
) ENGINE=INNODB;

-- insert table values memberTBL
INSERT INTO membertbl VALUES("Dang", "당탕이", "경기도 부천시 중동");
insert into membertBl VALUES("JEE", "지운이", "서울 은평구 증산동");
insert into membertbl values("Han", "한주연", "인천 남구 주안동");
insert inTO MEMBertbl values("Sang", "상달이", "경기 성남시 분당구");

-- iNSERT tABLE values proDUCTTBL
inserT into producTtbl values("컴퓨터", 10, "2021-01-01", "삼성", 17);
insert into producttBL VALuES("세탁기", 20, "2022-09-01", "LG", 3);
Insert into prOducttbl vAlUES("냉장고", 5, "2023-02-01", "대우", 22);

-- praCtICE select SQL
sElect * FRom MEMBErTBL;
select * frOM PRODucttbl;
selEcT * from producTtbl where cOMPany="삼성";
select productNaME, COsT FROM producttbl WHERE cOmPANY="삼성";


-- INDEX
drop table if exists indextbl;
create table indexTBL (
	first_name varchar(14), 
    last_name varchar(16),
    hire_date date);
    
insert into indexTBL(
	select first_name, last_name, hire_date
    from employees
    limit 500);
    
select * from indexTBL;

create index idx_indexTBL_firstname on indexTBL(first_name);
create index idx_indexTBL_firstname on employees(first_name);
select * from employees where first_name='Mary';


-- VIEW
create view uv_membertbl as select memberName, memberAddress from memberTBL;
select * from uv_memberTBL;


-- PROCEDURE
delimiter //
drop procedure if exists myProc1;
create procedure myProc1()
begin
	select * from memberTBL where memberName='당탕이';
    select * from productTBL where productName='냉장고';
end //
delimiter ;

call myProc1();


-- TRIGGER
create table deletedmemberTBL (
	old_memberID varchar(10) not null primary key,
    old_memberName varchar(10) not null,
    old_memberAddress varchar(25) not null,
    dTime date);
    
delimiter //
create trigger trigger_deletedmemberTBL
	after delete
    on memberTBL
    for each row
begin
	insert into deletedmemberTBL values(memberID, memberName, memberAddress, CURDATE());
end //
delimiter ;

select * from membertbl;
delete from membertbl where memberID="Han";
select * from deletedmemberTBL;


-- pymysql 파이썬 연동
create table test (
	id char(10) not null primary key,
    pw char(10) not null);
    
select * from test;