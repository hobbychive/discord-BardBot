# discord-BardBot
디스코드 바드봇

GDSC 세션에서 실습했던 디스코드 바드 챗봇을 개선/수정하였다.

공식은 아니지만 [bard-api](https://github.com/dsdanielpark/Bard-API)레포를 참고했다.

### api 설치

```
pip install bardapi
```

bard에서 개발자도구를 켠다음, 쿠키 탭에서 PSID_SECURE_1 에 해당하는 키를 가져와서 .env파일에 BARD_SESSION_ID로 저장한다.

### discord api 설치

```
pip install discord
```

디스코드 api를 설치한 후, [discord developers](https://discord.com/developers/docs/intro)에 들어가서 애플리케이션을 만든다.

토큰을 생성하고 이를 .env 파일에 DISCORD_TOKEN_BARD로 저장한다.

### 봇 초대

디스코드에서 봇을 초대한다. 방금 생성한 봇 디스코드 개발자 화면에서 왼쪽 더보기의 oauth에서 url generator에 들어가 Message와 관련된 권한을 주고 생성된 url을 연다.
초대를 하기 전에 bot intent privilege의 모든 스위치를 enable하는 것이 필요하다.

### 바드 봇 호출

!바드 를 입력하고 이후에 메세지를 입력하는 것으로 사용할 수 있다.
