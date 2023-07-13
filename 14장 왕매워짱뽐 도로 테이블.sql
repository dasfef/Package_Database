CREATE TABLE Road(
	RoadID int AUTO_INCREMENT PRIMARY KEY,	-- 도로 ID
    RoadName VARCHAR(20),					-- 도로 이름
    RoadLine GEOMETRY);						-- 도로 선
    
INSERT INTO Road VALUES
(NULL, '강변북로', ST_GeomFromText('LINESTRING(-70 -70, -50 -20, 30 30, 50 70)'));