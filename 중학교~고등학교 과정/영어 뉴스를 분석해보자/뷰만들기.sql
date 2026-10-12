-- 1. 뷰 생성
CREATE VIEW view_news_title_content AS
SELECT 
    "제목",
    "내용"
FROM news_5_articles;

-- 2. 생성한 뷰에서 데이터 조회
SELECT * FROM view_news_title_content;