# Docker Cheatsheet

## Image 이름 변경하기
Dockerfile을 수정하고 다시 Build할 때 이전과 동일하게 Tag를 설정하면, 이전 Image의 Repository name은 <none>이 된다. 이전 이미지를 관리하려면 이름을 변경할 필요가 있음. [stackoverflow: Docker how to change repository name or rename image?](https://stackoverflow.com/a/25214186)
```bash
$ docker image tag <IMAGE ID or REPOSITIORY:TAG> <REPOSITORY_NAME_YOU_WANT:TAG_NAME_YOU_WANT>
```
