# Jupyter cheatsheet

## Docker Container 내에서 Jupyter Kernel 실행시키기

[https://stackoverflow.com/a/63715102]

- Docker Image를 만든다.

```bash
# pwd contains Dockerfile 
docker bulild -t <my-docker-image> .
```

- kernelspec을 저장하는 Directory를 만든다.

```bash
mkdir ~/.local/share/jupyter/kernels/<name_what_you_want>
```

- 해당 Directory에 `kernel.json` 파일을 생성하고 해당 파일에 아래와 같이 JSON format으로 작성한다.

```json
{
 "argv": [
  "/usr/bin/docker",
  "run",
  "--network=host",
  "-v",
  "{connection_file}:/connection-spec",
  "<my-docker-image>",
  "python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "/connection-spec"
 ],
 "display_name": "docker-test",
 "language": "python"
}
```