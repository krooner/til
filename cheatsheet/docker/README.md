# Docker Cheatsheet

## Image 이름 변경하기

```bash
$ docker image tag <IMAGE ID or REPOSITIORY:TAG> <REPOSITORY_NAME_YOU_WANT:TAG_NAME_YOU_WANT>
```
- Dockerfile을 수정하고 다시 Build할 때 이전과 동일하게 Tag를 설정하면, 이전 Image의 Repository name은 <none>이 된다. 이전 이미지를 관리하려면 이름을 변경할 필요가 있음. [stackoverflow: Docker how to change repository name or rename image?](https://stackoverflow.com/a/25214186)

## [SOLVED] ERROR

```bash
$ docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
....

Total reclaimed space: 222.6GB
```

- Docker container와 함께 Jupyter Kernel을 띄우려고 하는데 `[Errno 28]: No space left on device` 라는 에러와 함께 Notebook이 실행되지 않는다. `docker system df -v` 명령어를 통해 현재 사용중인 컨테이너, 이미지, 볼륨 등이 얼마나 공간을 차지하고 있는지 파악했고, 캐시 사용 (Build cache usage) 이 너무 많았다. 거의 1년 동안 빌드했던 것들이 모두 캐시에 있었기 때문에 차지하는 용량도 200GB가 넘었다. `docker system prune` 명령어를 통해 시스템 내에서 미사용 중인 컨테이너, 이미지, 볼륨 등을 모두 삭제하니 해결되었다. 
