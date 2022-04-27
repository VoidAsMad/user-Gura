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
