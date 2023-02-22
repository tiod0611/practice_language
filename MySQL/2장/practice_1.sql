SELECT member_name, member_address FROM member;
SELECT * FROM member WHERE member_name = '아이유';

--  검색 속도를 향상시켜주는 INDEX만들기
-- INDEX를 idx_member_name으로 하는데 member테이블에 있는 member_name으로 해라
CREATE INDEX idx_member_name ON member (member_name);

