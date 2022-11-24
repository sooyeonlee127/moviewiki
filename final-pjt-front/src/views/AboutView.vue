<template>
  <div class="about">
    <div class="about_content">
      <caption>
        발견의 기쁨, 더 나은 경험.
        <br>
        <span>
          MOVIEWIKI
        </span>
        영화 추천
      </caption>
      <p>
        초간단 영화 추천,
        초간단 영화 검색
      </p>
    </div>
    <div class="about_content">
    <p>
      <br>
      <br>
      다양한 영화 정보와 추천 서비스를 즐길 수 있는, <span>MOVIEWIKI</span> 
    </p>
    <caption>
        쉽고 
      <br>
        빠르게
      <br>
        그리고
      <br>
    </caption>
      <caption style="font-style: italic;">
        재미있게
      </caption>  
      <caption>
        영화를 선택하세요. 
      </caption>
    </div>
    <div class="about_content">
      <p>
        .
        <br>
        .
        <br>
        .
        <br>
        <br>
        MOVIEWIKI가
        <br>
        제공합니다.
      </p>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <hr>
    <caption>
      <span style="text-decoration: underline;">
        Search
      </span>
    </caption>
    <p>
    <span>
      눈여겨봐왔던 영화가 있나요?
      <br>
      상단 검색창에서 
      <span style="font-weight: 500;">
        간편</span>하게 
        <span style="font-weight: 500;">
          검색</span>해보세요.
      <br>
      검색 결과 페이지에서 영화를 선택하면 영화 상세페이지로 go go!
    </span>
    </p>
  </div>
  <div class="about_content">
    <caption>
      <span style="text-decoration: underline;">
          Detail
        </span>
      </caption>
      <p>          
      영화의 모든 정보 !!
      <br>
      영화 
      <span style="font-weight: 500;">
        상세 정보</span>
      부터
      <br>
      다른 관객이 남긴 
      <span style="font-weight: 500;">
        리뷰
      </span>
      까지 ... 
      <br>
      <br>
      예고편 보러 유튜브까지 갈 필요 없어요.
      <br> 
      지금 클릭 한 번으로 
      <span style="font-weight: 500;">
        영화 예고편
      </span>
      까지 바로 확인해보세요.
      </p>
    </div>

  <div class="about_content">
    <caption>
      <span style="text-decoration: underline;">
        Choice
      </span>
    </caption>
    <p>    
      <br>
      <span style="font-style: italic;"> 
        "짧은 인생은 시간낭비에 의해 더욱 짧아진다."  - Samuel Johnson -
      </span>
      <br>
      <br>
      우리 시간 낭비는 하지 말아요 ㅜㅜ
      <br>
      날마다 쏟아지는 불필요한 정보 속에서,
      <br>
      당신이 꼭 필요한 영화만 빠르게 찾기를 바라며
      <br>
      <br>
    </p>
    <p>
      MOVIEWIKI는 영화 선택까지 
      <span style="font-weight: 500;">
        단 1분.
      </span>
      몇 가지 질문에 답하고 나면, 
      <br>
      MOVIEWIKI만의 
      <span style="font-weight: 500;">
        알고리즘</span>으로
      <br>
        영화를 
      <span style="font-weight: 500;">
        추천</span>해 드려요 !
      <br>
      <br>
      혹시 추천 결과로 나온 영화가 본 영화라면 ... ?
      <br>
      문제 없어요!
      <br>
      결과로 나온 추천 영화와 
      <span style="font-weight: 500;">
        유사한 영화 목록
      </span>
      제공까지!
      <br>
      MOVIEWIKI 하나면 영화 고르기 끝 ~~~!
    
    </p>
    <p>
      <br>
      <br>
      <br>
      <br>
      시시각각 달라지는 다양한 상황 속에서,
      <br>
      당신의 마음을 정확히 읽고 추천 하기 위해
      <br>
      MOVIEWIKI는
      오늘도 새로워지고 있습니다. : )
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
    </p>
  </div>
      
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>

<style>
.about {
  width: 100%;
  margin: 20px auto;
  height: 100%;
  min-height: 500px;
  background: black;

}

.about_content {
  margin-bottom: 60px;
  height: 100%;;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  margin-top: 200px;

}

.about_content > caption {
  line-height: 60px;
  font-size: 60px;    /* 원래 60*/ 
  color: white;
  font-weight: 700;
 
}
.about_content > caption > span {
  color: rgb(137, 255, 68);
}

.about_content > p {
  line-height: 60px;
  font-size: 30px; 
  color: white;
  font-weight: 1;
  align-items: start;
 
}

</style>