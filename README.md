# arca-slow-cleaner
느린 아카라이브 글삭제기

크롤러를 이용한 글 삭제기입니다. CAPCHA에 의해 안걸리도록 매우 느린 속도로 삭제가 되며(글 하나 삭제에 15초 정도)
따라서 클리너를 키고 잠을 자러 간다던지를 추천드립니다(...)
단 글 전부 삭제시의 종료 조건이 구현이 안되어 있어서, 모든 글을 밀면, 공지글을 삭제할려고 계속 시도하므로 주의해주세요.
해당 동작이 아카라이브 서버에서 밴당하는지는 확인해보지 못했습니다.
해당 코드는 [컴퓨터 공학 채널의 글](https://arca.live/b/programmers/42355472?p=1)을 기반으로 수정하여 작성되었습니다.