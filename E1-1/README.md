## 1부. 실습 명령어 가이드(터미널에서 직접 실행)
#### 1. 터미널 조작 및 권한 실습
- 현재 위치 확인 및 디렉토리 생성/이동
```bash
jung@MyHomeui-MacBookAir E1-1 % pwd
/Users/jung/Desktop/woochul_codyssey/E1-1
jung@MyHomeui-MacBookAir E1-1 % mkdir -p practice
jung@MyHomeui-MacBookAir E1-1 % cd practice
jung@MyHomeui-MacBookAir practice % 
```

- 파일 생성, 내용 확인, 복사, 이름 변경, 삭제
```bash
jung@MyHomeui-MacBookAir practice % echo "Hello Workstation" > test.txt
jung@MyHomeui-MacBookAir practice % cat test.txt
Hello Workstation
jung@MyHomeui-MacBookAir practice % cp test.txt copy_test.txt
jung@MyHomeui-MacBookAir practice % ls
copy_test.txt	test.txt
jung@MyHomeui-MacBookAir practice % mv copy_test.txt renamed_test.txt
jung@MyHomeui-MacBookAir practice % ls
renamed_test.txt	test.txt
jung@MyHomeui-MacBookAir practice % rm test.txt
jung@MyHomeui-MacBookAir practice % ls -la
total 8
drwxr-xr-x  3 jung  staff   96  8월  5 16:49 .
drwxr-xr-x  4 jung  staff  128  8월  5 16:44 ..
-rw-r--r--  1 jung  staff   18  8월  5 16:49 renamed_test.txt
```

- 권한 변경 실습 (파일 1개, 디렉토리 1개)
```bash
jung@MyHomeui-MacBookAir practice % ehco "Permission Test File" > perm_file.txt
zsh: command not found: ehco
jung@MyHomeui-MacBookAir practice % mkdir perm_dir
jung@MyHomeui-MacBookAir practice % ls -ld perm_file.txt perm_dir
drwxr-xr-x  2 jung  staff  64  8월  5 16:52 perm_dir
-rw-r--r--  1 jung  staff   0  8월  5 16:52 perm_file.txt
jung@MyHomeui-MacBookAir practice % chmod 644 perm_file.txt
jung@MyHomeui-MacBookAir practice % chmod 700 perm_dir
jung@MyHomeui-MacBookAir practice % ls -ld perm_file.txt perm_dir
drwx------  2 jung  staff  64  8월  5 16:52 perm_dir
-rw-r--r--  1 jung  staff   0  8월  5 16:52 perm_file.txt
```

#### 2. Docker 환경 점검 및 기본 명령(OrbStack 실행 상태)
- 버전 및 데몬 상태 점검
```bash
jung@MyHomeui-MacBookAir practice % docker --version
Docker version 29.4.0, build 9d7ad9f
jung@MyHomeui-MacBookAir practice % docker info
Client:
 Version:    29.4.0
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.33.0
    Path:     /Users/jung/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v5.1.2
    Path:     /Users/jung/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 29.4.0
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 301b2dac98f15c27117da5c8af12118a041a31d9
 runc version: bb14dabeb7185bb72c8c86735d090dcb20f36587
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 7.0.14-orbstack-00374-gbbca68e8d741
 Operating System: OrbStack
 OSType: linux
 Architecture: aarch64
 CPUs: 8
 Total Memory: 7.818GiB
 Name: orbstack
 ID: 145ebf22-ee90-4f6b-ae4a-daacff711cad
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http://proxy.orb.internal:8305
 HTTPS Proxy: http://proxy.orb.internal:8305
 No Proxy: localhost,127.0.0.1,127.0.0.0/8,::1,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,0.250.250.0/24,*.orb.internal,*.local,gateway.docker.internal,host.internal,host.docker.internal,host.lima.internal,docker.for.mac.localhost,docker.for.mac.host.internal
 Experimental: true
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64
 Firewall Backend: iptables

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set
```

- hello-world 컨테이너 실행
```bash
jung@MyHomeui-MacBookAir practice % docker run --name hello-test hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
58dee6a49ef1: Pull complete 
c3bdf82c34d1: Download complete 
Digest: sha256:7f4da0fc94bcece205a8c0b6f4d11c8196924654ffe5c4d1aa439b7f632048b2
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

- ubuntu 컨테이너 실행 및 내부 명령어 조작 (exec/attach 개념 이해)
```bash
jung@MyHomeui-MacBookAir practice % docker run -d --name my-ubuntu ubuntu sleep infinity
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
557836a62b76: Pull complete 
d73407a274fb: Pull complete 
277f396f91f3: Download complete 
Digest: sha256:678c6550cc43645e08669028bc177f50be4e7c5b8cca677067b1914d4afc7a03
Status: Downloaded newer image for ubuntu:latest
5cadf0e64c843b2826d9a31fd7c7965d1c22466e275f7be697f57b0a1cbc3e17
jung@MyHomeui-MacBookAir practice % docker exec -it my-ubuntu bash -c "ls -la &&echo 'Inside Ubuntu Container'"
total 12
drwxr-xr-x   1 root root   6 Aug  5 08:01 .
drwxr-xr-x   1 root root   6 Aug  5 08:01 ..
-rwxr-xr-x   1 root root   0 Aug  5 08:01 .dockerenv
drwxr-xr-x   1 root root  26 Jul 24 13:05 .rock
lrwxrwxrwx   1 root root   7 Apr 20 08:46 bin -> usr/bin
drwxr-xr-x   1 root root   0 Apr 20 08:46 boot
drwxr-xr-x   5 root root 320 Aug  5 08:01 dev
drwxr-xr-x   1 root root  56 Aug  5 08:01 etc
drwxr-xr-x   1 root root  12 Jul 24 13:05 home
lrwxrwxrwx   1 root root   7 Apr 20 08:46 lib -> usr/lib
drwxr-xr-x   1 root root   0 Jul 24 13:02 media
drwxr-xr-x   1 root root   0 Jul 24 13:02 mnt
drwxr-xr-x   1 root root   0 Jul 24 13:02 opt
dr-xr-xr-x 217 root root   0 Aug  5 08:01 proc
drwx------   1 root root  30 Jul 24 13:05 root
drwxr-xr-x   1 root root  22 Jul 24 13:05 run
lrwxrwxrwx   1 root root   8 Apr 20 08:46 sbin -> usr/sbin
drwxr-xr-x   1 root root   0 Jul 24 13:02 srv
dr-xr-xr-x  11 root root   0 Aug  5 08:01 sys
drwxrwxrwt   1 root root   0 Jul 24 13:03 tmp
drwxr-xr-x   1 root root  10 Jul 24 13:01 usr
drwxr-xr-x   1 root root  90 Jul 24 13:05 var
Inside Ubuntu Container
```

- 이미지 및 컨테이너 리소스/로그 확인
```bash
jung@MyHomeui-MacBookAir practice % docker images
                                                                              i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   7f4da0fc94bc       18.5kB         10.3kB    U   
ubuntu:latest        678c6550cc43        178MB         44.4MB    U   
jung@MyHomeui-MacBookAir practice % docker ps -a
CONTAINER ID   IMAGE         COMMAND            CREATED         STATUS                     PORTS     NAMES
5cadf0e64c84   ubuntu        "sleep infinity"   5 minutes ago   Up 5 minutes                         my-ubuntu
39a91085e37e   hello-world   "/hello"           9 minutes ago   Exited (0) 9 minutes ago             hello-test
jung@MyHomeui-MacBookAir practice % docker logs my-ubuntu
jung@MyHomeui-MacBookAir practice % docker stats --no-stream
CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O     PIDS
5cadf0e64c84   my-ubuntu   0.00%     2.203MiB / 7.818GiB   0.03%     1.13kB / 126B   16.2MB / 0B   1
```

#### 3. 커스텀 웹 서버 빌드 및 포트 매핑 실습
- 프로젝트 폴더 세팅
```bash
jung@MyHomeui-MacBookAir practice % mkdir -p app
jung@MyHomeui-MacBookAir practice % ls
app			perm_dir		perm_file.txt		renamed_test.txt
```

- 웹 서버에 띄울 HTML 작성
```bash
jung@MyHomeui-MacBookAir practice % cat << 'EOF' > app/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dev Workstation</title>
</head>
<body>
    <h1>Dev Workstation Container Running!</h1>
    <p>Powered by OrbStack & Nginx</p>
</body>
</html>
EOF
jung@MyHomeui-MacBookAir practice % ls app
index.html
```

- Dockerfile 작성 (Nginx 베이스)
```bash
jung@MyHomeui-MacBookAir practice % cat << 'EOF' > Dockerfile
FROM nginx:alpine
LABEL maintainer="student"
LABEL description="Custom Nginx Web Server for Dev Workstation"
```

- 정적 파일 교체
```bash
heredoc> COPY app/index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
EOF
```

- 커스텀 이미지 빌드
```bash
jung@MyHomeui-MacBookAir practice % docker build -t my-custom-web:1.0 .
[+] Building 5.0s (7/7) FINISHED                                                   docker:orbstack
 => [internal] load build definition from Dockerfile                                          0.0s
 => => transferring dockerfile: 247B                                                          0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                               2.8s
 => [internal] load .dockerignore                                                             0.0s
 => => transferring context: 2B                                                               0.0s
 => [internal] load build context                                                             0.1s
 => => transferring context: 280B                                                             0.0s
 => [1/2] FROM docker.io/library/nginx:alpine@sha256:4a73073bd557c65b759505da037898b61f1be6c  1.9s
 => => resolve docker.io/library/nginx:alpine@sha256:4a73073bd557c65b759505da037898b61f1be6c  0.0s
 => => sha256:977aedb192ade9f4f62ce4c6df02d8f62abe1e8710e006854398f8a7cda0 19.85MB / 19.85MB  0.9s
 => => sha256:ba4be3b26f08037fa63337d7a425d3253b887bff559447733e71759f65b0f8 1.40kB / 1.40kB  0.2s
 => => sha256:e1f13a453c9dd406f331a3efefeb846cd18b068d73177c0d57c6f3d5169eac 1.21kB / 1.21kB  0.7s
 => => sha256:c4a042f5cf717d2e64d2176a41624344a2f1ad0475f6ac6dae092aefbbd07b37 405B / 405B    0.7s
 => => sha256:d0e9565ba4ff139c848073b3358bb2c9b31a93cb9b744a5b0903b22f5a3ddc0f 956B / 956B    0.5s
 => => sha256:e42993d4c6ecb26b388e945cbe5f03be1f7858226750c1f8375883db2aae1243 626B / 626B    0.2s
 => => sha256:7b1fb50ff9dc606dba8c8c0e8eb4e98c650c5b289506f01724309ebf71a69d 1.91MB / 1.91MB  0.3s
 => => sha256:5de55e5ef9c033997441461efe7ba23a986db059c0bb78b38f84ee0d72b991 4.18MB / 4.18MB  0.5s
 => => extracting sha256:5de55e5ef9c033997441461efe7ba23a986db059c0bb78b38f84ee0d72b99167     0.1s
 => => extracting sha256:7b1fb50ff9dc606dba8c8c0e8eb4e98c650c5b289506f01724309ebf71a69d45     0.0s
 => => extracting sha256:e42993d4c6ecb26b388e945cbe5f03be1f7858226750c1f8375883db2aae1243     0.0s
 => => extracting sha256:d0e9565ba4ff139c848073b3358bb2c9b31a93cb9b744a5b0903b22f5a3ddc0f     0.0s
 => => extracting sha256:c4a042f5cf717d2e64d2176a41624344a2f1ad0475f6ac6dae092aefbbd07b37     0.0s
 => => extracting sha256:e1f13a453c9dd406f331a3efefeb846cd18b068d73177c0d57c6f3d5169eacb4     0.0s
 => => extracting sha256:ba4be3b26f08037fa63337d7a425d3253b887bff559447733e71759f65b0f8c8     0.0s
 => => extracting sha256:977aedb192ade9f4f62ce4c6df02d8f62abe1e8710e006854398f8a7cda030e7     0.2s
 => [2/2] COPY app/index.html /usr/share/nginx/html/index.html                                0.1s
 => exporting to image                                                                        0.1s
 => => exporting layers                                                                       0.1s
 => => exporting manifest sha256:2b46de599cdd5f82d0df782c65d15e6d220b75e9f210d308fdca576f7f5  0.0s
 => => exporting config sha256:fef7a35b27ea485ec80fb80b0b09dfea987b433ba950e49f14bf103631a31  0.0s
 => => exporting attestation manifest sha256:e6c569c5709fc0f30c049f4dd8e956a71ec8c2f79db1986  0.0s
 => => exporting manifest list sha256:5216378750a75fdd35ba0cf22dc9116c307c0dafda041c5a76f0f9  0.0s
 => => naming to docker.io/library/my-custom-web:1.0                                          0.0s
 => => unpacking to docker.io/library/my-custom-web:1.0                                       0.0s
```

- 포트 매핑 컨테이너 실행 (8080 포트)
```bash
jung@MyHomeui-MacBookAir practice % docker run -d -p 8080:80 --name web-8080 my-custom-web:1.0
07d7fa0bbb1d639a6c68ecb41dbe73769a7735c98cfb15a37448fc1ab559d48d
```

- 접속 검증 (curl 및 브라우저에서 http://localhost:8080 접속)
```bash
jung@MyHomeui-MacBookAir practice % curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dev Workstation</title>
</head>
<body>
    <h1>Dev Workstation Container Running!</h1>
    <p>Powered by OrbStack & Nginx</p>
</body>
</html>
```

#### 4. 바인드 마운트 & Docker 볼륨 영속성 실습
- 바인드 마운트 실습 (호스트의 app 폴더를 컨테이너에 실시간 연결)
```bash
jung@MyHomeui-MacBookAir practice % docker run -d -p 8081:80 --name web-bind -v $(pwd)/app:/usr/share/nginx/html nginx:alpine
Unable to find image 'nginx:alpine' locally
alpine: Pulling from library/nginx
Digest: sha256:4a73073bd557c65b759505da037898b61f1be6cbcc3c2c3aeac22d2a470c1752
Status: Downloaded newer image for nginx:alpine
07afd8a4849762aaf267ed0a1a22a5bf1099dd67bfde61da48e5fea8af358036
```

- 호스트 파일 변경 전 확인
```bash
jung@MyHomeui-MacBookAir practice % curl http://localhost:8081
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dev Workstation</title>
</head>
<body>
    <h1>Dev Workstation Container Running!</h1>
    <p>Powered by OrbStack & Nginx</p>
</body>
</html>
```

- 호스트 파일 수정
```bash
jung@MyHomeui-MacBookAir practice % echo '<h1>Updated via Bind Mount!</h1>' > app/index.html
```

- 호스트 파일 변경 후 컨테이너 자동 반영 확인
```bash
jung@MyHomeui-MacBookAir practice % curl http://localhost:8081
<h1>Updated via Bind Mount!</h1>
```

- Docker 볼륨 영속성 검증
- 볼륨 생성
```bash
jung@MyHomeui-MacBookAir practice % docker volume create my-app-data
my-app-data
```

- 컨테이너 1 생성 후 볼륨에 데이터 쓰기
```bash
jung@MyHomeui-MacBookAir practice % docker run -d --name vol-container-1 -v my-app-data:/data ubuntu sleep infinity
0984d150eeacb9728753a79fce6825c4d70e232825635f420a4c58c4409cbd87
jung@MyHomeui-MacBookAir practice % docker exec vol-container-1 bash -c "echo 'Persistent Data Saved' > /data/persistence.txt"
jung@MyHomeui-MacBookAir practice % docker exec vol-container-1 cat /data/persistence.txt
Persistent Data Saved
```

-컨테이너 1 강제 삭제
```bash
jung@MyHomeui-MacBookAir practice % docker rm -f vol-container-1
vol-container-1
```

- 컨테이너 2 생성 후 동일 볼륨 연결하여 데이터 유지 검증
```bash
jung@MyHomeui-MacBookAir practice % docker run -d --name vol-container-2 -v my-app-data:/data ubuntu sleep infinity
ebe08aff8cb9a343ce558a98f38546083b4cf98883aa51219884cc3e6ca5a19e
jung@MyHomeui-MacBookAir practice % docker exec vol-container-2 cat /data/persistence.txt
Persistent Data Saved
```

-테스트 정리
```bash
jung@MyHomeui-MacBookAir practice % docker rm -f vol-container-2
vol-container-2
```

#### 5. Git 설정 점검
- Git 사용자 및 기본 브랜치 설정
```bash
jung@MyHomeui-MacBookAir practice % git config --global user.name "woochul0516"
jung@MyHomeui-MacBookAir practice % git config --global user.email "dncjf55252@gmail.com"  
jung@MyHomeui-MacBookAir practice % git config --global init.defaultBranch main
```

- 설정 목록 확인 및 출력
```bash
jung@MyHomeui-MacBookAir practice % git config --list
credential.helper=osxkeychain
init.defaultbranch=main
user.name=woochul0516
user.email=dncjf55252@gmail.com
init.defaultbranch=main
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/woochul0516/woochul_codyssey
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
branch.main.vscode-merge-base=origin/main
```