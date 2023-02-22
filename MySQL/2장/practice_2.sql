-- 실제 테이블은 아니지만 테이블처럼 보이는 VIEW 생성
CREATE VIEW member_view
AS
	SELECT * FROM member;
    
SELECT * FROM member_view;

-- 스토어드 프로시저 만들기
-- 마치 변수를 만드는 것 같은 기능
DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
	SELECT * FROM member WHERE member_name = '나훈아';
	SELECT * FROM product WHERE product_name = '삼각김밥';
END //
DELIMITER ;

CALL myProc();