CREATE TABLE Manager(
	ManagerID int AUTO_INCREMENT PRIMARY KEY,	-- 지역관리자 id
    ManagerName VARCHAR(5),						-- 지역관리자 이름
    MobilePhone	VARCHAR(15),					-- 지역관리자 전화번호
    Email VARCHAR(40),							-- 지역관리자 이메일
    AreaName VARCHAR(15),						-- 담당지역명
    Area GEOMETRY SRID 0);						-- 담당지역 폴리곤ALTER
    
INSERT INTO Manager VALUES
(NULL, '존밴이', '011-123-4567', 'johnbann@kinghot.com', '서울 동/북부지역', 
ST_GeomFromText('POLYGON((-90 0, -90 90, 90 90, 90 -90, 0 -90, 0 0, -90 0))')),
(NULL, '당탕이', '010-3213-8945', 'dangtang@kinghot.com', '서울 서부지역', 
ST_GeomFromText('POLYGON((-90 -90, -90 90, 0 90, 0 -90, -90 -90))'));