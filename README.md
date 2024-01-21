<h1>🎦 Video Detector</h1>
동영상 감지 웹사이트<br/><br/>
<blockquote>
   'A' 프로젝트에서 인턴으로 참여하여 개발한 코드를 웹사이트로 구현한 결과물로, 원래 프로젝트의 주제와는 다르게 구성하여 제가 참여한 부분으로만 웹사이트로 형상화하여 선보입니다.
</blockquote>

<h2>목차</h2>
<ol style="margin-top: 0; margin-bottom: 0;">
   <li><a href="#프로젝트-소개">프로젝트 소개</a></li>
   <ul style="list-style-type: square">
     <li><a href="#개발-목표">개발 목표</a></li>
     <li><a href="#기술-스택">기술 스택</a></li>
     <li><a href="#개발-기간">개발 기간</a></li>
     <li><a href="#폴더-구조">폴더 구조</a></li>
    <li><a href="#동영상-감지">동영상 감지</a></li>
   </ul>
   <li><a href="#시작하기">시작하기</a></li>
   <li><a href="#바로가기">바로가기</a></li>
</ol>

<h2 id="프로젝트-소개">🔴 프로젝트 소개</h2>
<h3 id="개발-목표">▹ 개발 목표</h3>
Flask와 Python을 활용하여 주어진 URL에서 동영상의 존재 여부를 감지하고, 해당 URL로 리다이렉트하는 웹사이트를 생성하는 것이 목표입니다.
<h3 id="기술-스택">▹ 기술 스택</h3>
<p>
 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
 <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
 <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
 <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</p>
<h3 id="개발-기간">▹ 개발 기간</h3>
2024.01.16-01.21 <br>
<h3 id="폴더-구조">▹ 폴더 구조</h3>
<pre>
📦web_accelerator
 ┣ 📂app
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┗ 📜index.html
 ┃ ┣ 📜detectors.py
 ┃ ┣ 📜config.py
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜__init__.py
 ┣ 📂venv
 ┣ 📜app.py
 ┗ 📜requirements.txt
</pre>
<h3 id="동영상-감지">▹ 동영상 감지</h3>
<ul>
  <li><b>Video 태그 검출:</b><br/>
    <video> 태그의 존재 여부를 확인하며 발견 시 로그와 콘솔에 메시지를 출력합니다.
  </li>
  <li><b>MP4 파일 URL 검출: </b><br/>
    '.mp4' 확장자를 가진 링크를 찾아내며 발견된 MP4 파일 URL은 로그 및 콘솔에 출력됩니다.
  </li>
  <li><b>Iframe 태그 검출 및 YouTube 동영상 감지:</b><br/>
    <iframe> 태그를 찾아내며 YouTube 동영상이 포함된 경우도 감지합니다.
  </li>
  <li><b>JSON-LD 스크립트 검출 및 VideoObject 파싱:</b><br/>
    'application/ld+json' 유형의 <script> 태그를 찾아내며, VideoObject가 있는 경우도 감지합니다.
  </li>
  <li><b>JavaScript 코드에서 동영상 참조 검사:</b><br/> 
    JavaScript 코드에서 'video' 참조를 확인하며 발견 시 로그와 콘솔에 메시지를 출력합니다.
  </li>
</ul>

<h2 id="시작하기">⏯️ 시작하기</h2>
<pre>
 
 # 가상 환경 생성
 python3.12 -m venv venv
 
 # 가상 환경 활성화 (macOS/Linux)
 source venv/bin/activate
 
 # 가상 환경 활성화 (Windows)
 venv\Scripts\activate
 
 # 필요한 패키지 설치
 pip install -r requirements.txt
 
 # Flask와 Werkzeug 설치 또는 업그레이드
 pip install --upgrade Flask Werkzeug
 
 # requests 패키지 설치
 pip install requests
 
 # BeautifulSoup4 패키지 설치
 pip install beautifulsoup4
 
 # Flask 애플리케이션 실행
 python app.py
 
</pre>

<h2 id="바로가기">🔗 바로가기</h2>
<a href="https://hayeonrjoe.github.io/">배포 링크</a>
