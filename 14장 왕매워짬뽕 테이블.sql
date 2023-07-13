CREATE DATABASE KingHotDB;

USE KingHotDB;

CREATE TABLE Restaurant(
	restID int AUTO_INCREMENT PRIMARY KEY,	-- 체인점 ID
    restName VARCHAR(50),					-- 체인점 이름
    restAddr VARCHAR(50),					-- 체인점 주소
    restPhone VARCHAR(15),					-- 체인점 전화번호
    totSales BIGINT,						-- 총 매출액
    restLocation GEOMETRY);					-- 체인점 위치
    
INSERT INTO Restaurant VALUES
(NULL, '왕매워 짬뽕 1호점', '서울 강서구 방화동', '02-111-1111', 1000, ST_GeomFromText('POINT(-80 -30)')),
(NULL, '왕매워 짬뽕 2호점', '서울 은평구 증산동', '02-222-2222', 2000, ST_GeomFromText('POINT(-50 70)')),
(NULL, '왕매워 짬뽕 3호점', '서울 중량구 면목동', '02-333-3333', 9000, ST_GeomFromText('POINT(70 50)')),
(NULL, '왕매워 짬뽕 4호점', '서울 광진구 구의동', '02-444-4444', 250, ST_GeomFromText('POINT(80 -10)')),
(NULL, '왕매워 짬뽕 5호점', '서울 서대문구 북가좌동', '02-555-5555', 1200, ST_GeomFromText('POINT(-10 50)')),
(NULL, '왕매워 짬뽕 6호점', '서울 강남구 논현동', '02-666-6666', 4000, ST_GeomFromText('POINT(40 -30)')),
(NULL, '왕매워 짬뽕 7호점', '서울 서초구 서초동', '02-777-7777', 1000, ST_GeomFromText('POINT(30 -70)')),
(NULL, '왕매워 짬뽕 8호점', '서울 영등포구 당산동', '02-888-8888', 200, ST_GeomFromText('POINT(-40 -50)')),
(NULL, '왕매워 짬뽕 9호점', '서울 송파구 가락동', '02-999-9999', 600, ST_GeomFromText('POINT(60 -50)'));


