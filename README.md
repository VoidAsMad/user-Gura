# Gura
[Gura](https://github.com/VoidAsMad/Gura)의 유저용으로 개발된 봇으로 서버관리를 지원합니다.

[<img src="https://img.shields.io/badge/python-4374D9?style=for-the-badge&logo=python&logoColor=white">](https://discord.gg/B98msXGRB7)

# Release_note
# [2022-04-26]
1. `/docs`명령어가 추가되었습니다.<br/>
## 태그목록
```
[1](role)
[2](user)
[3](send)
[4](warn)
```
## 1. Role
1. `/addrole [role] [user]`으로 유저에게 역할을 부여할 수 있습니다.
2. `/remove_role [role] [user]`으로 유저에게 역할을 제거 할 수 있습니다.

## 2. User
1. `/kick [user] (reason)`으로 유저를 추방할 수 있습니다(재입장 가능)
2. `/ban [user] (reason)`으로 유저를 차단할 수 있습니다(재입장 불가능)

# [2022-04-27]
대규모 업데이트
## 1. Send
1. `/send [channel] [message]`을 통해 메세지를 보낼 수 있습니다.
2. `/embed [channel] [title] [description] (name) (value)`를 통해 임베드를 보낼수 있습니다.

## 2. Warn
1. `/warn [user]`를 통해 유저를 경고합니다.(경고 3회가 채워질 시 차단처리가 이루어집니다.)
2. `/unwarn [user]`를 통해 유저가 받은 경고를 삭제합니다.
3. `/warns (user)`를 통해 받은 경고 횟수를 확인합니다.

## 3. Language
`/language (select)`를 통해 언어를 변경할 수 있습니다.<br/>
만약 select가 비어있다면 지원언어 목록을 불러옵니다.

# [2022-05-01]
1. `/clear [amount]`를 통해 메세지를 삭제합니다.
2. `/avatar (user)`를 통해 프로필 사진을 로드합니다

# [2022-05-06]
## 미니게임추가
`/lvup`을 통해 구라를 레벨업 할 수 있습니다
### 확률표
성공 : 80%<br/>
실패 : 15%<br/>
초기화 : 5%<br/>


# [2022-05-07]
## note기능 추가
1. `/note [user] (memo)`를 사용해서 유저에 대한 정보, 점수등을 기록합니다.(만약 memo가 비어있을시 작성된 기록을 출력합니다)
2. `/note_reset [user]`를 사용해서 유저에게 기록된 정보를 삭제합니다.
