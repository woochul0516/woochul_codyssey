# woochul_codyssey
코디세이 연동용

# 개발 워크스테이션 구축 미션

## 1. 프로젝트 개요
터미널 CLI, OrbStack(Docker), Git/GitHub 환경을 세팅하고 검증하는 워크스테이션 구축 미션입니다.

---

## 2. 실행 환경 및 디렉토리 구조

### 2.1. 실행 환경
- **OS**: macOS
- **Shell**: zsh
- **Docker**: Docker version 28.5.2, build ecc6942
- **Git**: git version 2.55.0

### 2.2. 디렉토리 구조 및 파일 역할 (재현성 가이드)
```text
woochul_codyssey/
├── E1-1/
│   ├── practice/
│   │   ├── Dockerfile              # Nginx 기반 커스텀 웹 서버 이미지 빌드 명세서
│   │   ├── app/
│   │   │   └── index.html          # 컨테이너 웹 서버에 배포할 메인 HTML 파일
│   │   ├── images/
│   │   │   └── port-mapping.png    # 포트 매핑 검증 브라우저 접속 스크린샷
│   │   └── test.txt                # CLI 및 권한(Permission) 테스트용 파일
│   └── README.md                   # E1-1 미션 수행 결과 및 보고서
└── README.md                       # 최상위 프로젝트 README
```

## 3. 수행 체크리스트
- [x] 터미널 기본 조작 및 권한 변경 실습
- [x] Docker 기본 명령어 및 컨테이너 실습
- [x] 웹 서버 Dockerfile 커스텀 이미지 빌드
- [x] 포트 매핑 접속 검증
- [x] 바인드 마운트 및 볼륨 영속성 검증
- [x] Git 설정 및 GitHub 연동

---

## 4. 터미널 조작 및 권한 실습 로그

# 현재 작업 디렉토리 경로 확인
dncjf552523857@c1r4s3 woochul_codyssey % pwd
/Users/dncjf552523857/Documents/woochul_codyssey

# 숨김 파일을 포함한 상세 목록 확인
dncjf552523857@c1r4s3 woochul_codyssey % ls -la
total 8
drwxr-xr-x   4 dncjf552523857  dncjf552523857  128  7 28 20:56 .
drwx------+  4 dncjf552523857  dncjf552523857  128  7 28 20:56 ..
drwxr-xr-x  12 dncjf552523857  dncjf552523857  384  7 28 20:56 .git
-rw-r--r--   1 dncjf552523857  dncjf552523857   42  7 28 20:56 README.md

# 실습용 디렉토리 생성 및 이동
dncjf552523857@c1r4s3 woochul_codyssey % mkdir practice
dncjf552523857@c1r4s3 woochul_codyssey % cd practice

# 빈 테스트 파일 생성 및 확인
dncjf552523857@c1r4s3 practice % touch test.txt
dncjf552523857@c1r4s3 practice % ls
test.txt

# 파일에 텍스트 작성 및 출력
dncjf552523857@c1r4s3 practice % echo "Hello Workstation" > test.txt
dncjf552523857@c1r4s3 practice % cat test.txt
Hello Workstation

# 파일 복사, 이름 변경, 삭제 수행
dncjf552523857@c1r4s3 practice % cp test.txt test_copy.txt
dncjf552523857@c1r4s3 practice % mv test_copy.txt renamed_test.txt
dncjf552523857@c1r4s3 practice % ls
renamed_test.txt  test.txt
dncjf552523857@c1r4s3 practice % rm renamed_test.txt
dncjf552523857@c1r4s3 practice % ls
test.txt

# 파일 권한 확인 및 644 권한 설정
dncjf552523857@c1r4s3 practice % ls -l test.txt
-rw-r--r--  1 dncjf552523857  dncjf552523857  18  7 28 21:03 test.txt
dncjf552523857@c1r4s3 practice % chmod 644 test.txt
dncjf552523857@c1r4s3 practice % ls -l test.txt
-rw-r--r--  1 dncjf552523857  dncjf552523857  18  7 28 21:03 test.txt

# 디렉토리 생성 및 755 권한 설정
dncjf552523857@c1r4s3 practice % mkdir test_dir
dncjf552523857@c1r4s3 practice % ls -ld test_dir
drwxr-xr-x  2 dncjf552523857  dncjf552523857  64  7 28 21:07 test_dir
dncjf552523857@c1r4s3 practice % chmod 755 test_dir
dncjf552523857@c1r4s3 practice % ls -ld test_dir
drwxr-xr-x  2 dncjf552523857  dncjf552523857  64  7 28 21:07 test_dir

rwx 비트 개념: 읽기(r=4), 쓰기(w=2), 실행(x=1) 권한 비트의 합으로 표현되며, 소유자 / 그룹 / 기타 사용자 순서로 적용됩니다.

chmod 644 (rw-r--r--): 소유자에게 읽기/쓰기(4+2=6) 권한을 주고, 그룹 및 기타 사용자에게는 읽기 전용(4) 권한만 부여하여 무단 수정 방지.

chmod 755 (rwxr-xr-x): 소유자에게 읽기/쓰기/실행(4+2+1=7) 권한을 부여하고, 그룹 및 기타 사용자에게는 읽기/실행(4+1=5) 권한을 부여하여 디렉토리 탐색(cd) 및 실행을 허용.

## 4.3. Docker 설치 및 기본 점검

### 1) Docker 버전 확인
dncjf552523857@c1r4s3 practice % docker --version
Docker version 28.5.2, build ecc6942

### 2) Docker 데몬 상태 확인
dncjf552523857@c1r4s3 practice % docker info
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/dncjf552523857/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/dncjf552523857/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
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
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: 0adaeff4-7b45-428d-844e-a18da27b5035
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
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

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set

데몬 상태 요약: Docker 데몬(OrbStack)이 정상 작동 중이며, 현재 구동/정지된 컨테이너는 0개, 저장된 이미지 0개, 스토리지 드라이버는 overlay2를 사용 중임을 확인했습니다.

## 4.4) Docker 기본 운영 및 컨테이너 실습
### 1) hello-world 실행
dncjf552523857@c1r4s3 practice % docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
Digest: sha256:c3cbe1cc1aa588a64951ac6286e0df7b27fe2e6324b1001c619bb358770c0178
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
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

 테스트의 의미: hello-world 실행을 통해 Docker 데몬과의 통신, Docker Hub에서의 이미지 다운로드(Pull), 컨테이너 생성 및 실행까지의 엔드투엔드 설치 및 클라이언트-데몬 동작이 정상임을 검증합니다.

### 2) ubuntu 컨테이너 진입 및 내부 명령어 수행
dncjf552523857@c1r4s3 practice % docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
ed819469700f: Pull complete 
a3679419df18: Pull complete 
Digest: sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb
Status: Downloaded newer image for ubuntu:latest
root@c99dc715217e:/# ls -la
total 16
drwxr-xr-x   1 root root   6 Jul 28 12:30 .
drwxr-xr-x   1 root root   6 Jul 28 12:30 ..
-rwxr-xr-x   1 root root   0 Jul 28 12:30 .dockerenv
drwxr-xr-x   1 root root  26 Jul 13 16:06 .rock
lrwxrwxrwx   1 root root   7 Apr 20 08:46 bin -> usr/bin
drwxr-xr-x   1 root root   0 Apr 20 08:46 boot
drwxr-xr-x   5 root root 340 Jul 28 12:30 dev
drwxr-xr-x   1 root root  56 Jul 28 12:30 etc
drwxr-xr-x   1 root root  12 Jul 13 16:06 home
lrwxrwxrwx   1 root root   7 Apr 20 08:46 lib -> usr/lib
lrwxrwxrwx   1 root root   9 Apr 20 08:46 lib64 -> usr/lib64
drwxr-xr-x   1 root root   0 Jul 13 16:05 media
drwxr-xr-x   1 root root   0 Jul 13 16:05 mnt
drwxr-xr-x   1 root root   0 Jul 13 16:05 opt
dr-xr-xr-x 233 root root   0 Jul 28 12:30 proc
drwx------   1 root root  30 Jul 13 16:06 root
drwxr-xr-x   1 root root  22 Jul 13 16:06 run
lrwxrwxrwx   1 root root   8 Apr 20 08:46 sbin -> usr/sbin
drwxr-xr-x   1 root root   0 Jul 13 16:05 srv
dr-xr-xr-x  11 root root   0 Jul 28 12:30 sys
drwxrwxrwt   1 root root   0 Jul 13 16:06 tmp
drwxr-xr-x   1 root root  10 Jul 13 16:05 usr
drwxr-xr-x   1 root root  90 Jul 13 16:06 var
root@c99dc715217e:/# echo "Hello Docker Container"
Hello Docker Container
root@c99dc715217e:/# exit
exit

이미지 불변성 vs 컨테이너 상태:

이미지(Image): 애플리케이션 파일과 실행 환경을 포함하는 읽기 전용(Read-Only) 불변 템플릿입니다.

컨테이너(Container): 이미지 상단에 읽기/쓰기 가변 레이어(Writable Layer)를 올려 실행되는 동적 격리 프로세스입니다.

### 3) 이미지 및 컨테이너 목록 확인
dncjf552523857@c1r4s3 practice % docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    de7345b16e94   2 weeks ago    100MB
hello-world   latest    e2ac70e7319a   4 months ago   10.1kB

dncjf552523857@c1r4s3 practice % docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
c99dc715217e   ubuntu        "bash"     3 minutes ago   Exited (0) 2 minutes ago             peaceful_poitras
99b24f417dc9   hello-world   "/hello"   4 minutes ago   Exited (0) 4 minutes ago             competent_shirley

## 4.5 커스텀 웹 서버 이미지 빌드 및 포트 매핑

### 1. Dockerfile 내용
```dockerfile
FROM nginx:alpine
COPY app/index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

### 2. 터미널 실행 결과
dncjf552523857@c1r4s3 practice % mkdir -p app
dncjf552523857@c1r4s3 practice % cat << 'EOF' > app/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Dev Workstation</title>
</head>
<body>
    <h1>개발 워크스테이션 웹 서버 구축 성공!</h1>
    <p>Dockerfile 기반 커스텀 NGINX 컨테이너가 정상 구동 중입니다.</p>
</body>
</html>
EOF

dncjf552523857@c1r4s3 practice % cat << 'EOF' > Dockerfile
FROM nginx:alpine
COPY app/index.html /usr/share/nginx/html/index.html
EXPOSE 80
EOF

dncjf552523857@c1r4s3 practice % docker build -t my-web:1.0 .
# ... (빌드 성공 로그) ...
 => naming to docker.io/library/my-web:1.0

# 컨테이너 실행
dncjf552523857@c1r4s3 practice % docker run -d -p 8080:80 --name my-web-8080 my-web:1.0
0c9b4665970f25f0cbd367c4abfb72eb0de23ab39936a4fb91e2f90b9ffdae94

# 포트 매핑 접속 검증 (curl)
dncjf552523857@c1r4s3 practice % curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Dev Workstation</title>
</head>
<body>
    <h1>개발 워크스테이션 웹 서버 구축 성공!</h1>
    <p>Dockerfile 기반 커스텀 NGINX 컨테이너가 정상 구동 중입니다.</p>
</body>
</html>

-d (Detached): 컨테이너를 백그라운드 프로세스로 실행.

-p 8080:80 (Port Mapping): 호스트의 8080 포트로 들어오는 요청을 컨테이너 내부 80 포트로 전달.

### 3. 브라우저 접속 화면
![포트 매핑 접속 화면](./practice/images/port-mapping.png)

## 4.6 바인드 마운트 및 볼륨 영속성 검증

### 1. 바인드 마운트 (실시간 변경 반영)
# 호스트의 상대 경로 파일(app/)을 컨테이너 내부 웹 경로로 바인드 마운트
dncjf552523857@c1r4s3 practice % docker run -d -p 8081:80 -v $(pwd)/app:/usr/share/nginx/html --name bind-test my-web:1.0
222471b1f2c71b5550c6c2daa98ae671007a340ce6d4708e7a9d14cddb52ca15

# 접속 테스트
dncjf552523857@c1r4s3 practice % curl http://localhost:8081

### 2. Docker 볼륨 (컨테이너 삭제 후 데이터 유지 검증)
# 1) 볼륨 생성 및 첫 번째 컨테이너 데이터 쓰기
dncjf552523857@c1r4s3 practice % docker volume create mydata
mydata
dncjf552523857@c1r4s3 practice % docker run -d --name vol-test1 -v mydata:/data ubuntu sleep infinity
74fd44c975be0dac4e3f3b1337f49945be9b0d26b0bdcba248f0a69fc7ad5685
dncjf552523857@c1r4s3 practice % docker exec vol-test1 bash -c "echo 'Persisted Data' > /data/test.txt"
dncjf552523857@c1r4s3 practice % docker exec vol-test1 cat /data/test.txt
Persisted Data

# 2) 첫 번째 컨테이너 삭제 후 새 컨테이너에서 데이터 유지 확인
dncjf552523857@c1r4s3 practice % docker rm -f vol-test1
vol-test1
dncjf552523857@c1r4s3 practice % docker run -d --name vol-test2 -v mydata:/data ubuntu sleep infinity
26d5f9b3850d2c9519877c5ce062d7872faff22365b7f54ca044c85de9db554f
dncjf552523857@c1r4s3 practice % docker exec vol-test2 cat /data/test.txt
Persisted Data

## 5. 고급 컨테이너/네트워크/경로/백업 기술 가이드

### 5.1. 컨테이너 포트 노출(Port Exposure)과 보안 고려사항
필요성: 컨테이너는 독립된 네트워크 네임스페이스(Namespace)를 가지고 있어 기본적으로 외부와 격리됩니다. 외부 요청을 받으려면 -p 옵션을 통해 호스트 포트와 명시적으로 바인딩해야 합니다.

보안 및 접속 장애 시 점검 항목:

바인딩 범위 제한: 외부 노출이 불필요한 경우 -p 127.0.0.1:8080:80으로 설정하여 호스트 내부 통신만 허용.

방화벽 및 호스트 바인딩: macOS/Linux 방화벽 설정 및 AWS Security Group 규칙 확인.

포트 중복 확인: 호스트에서 이미 사용 중인 포트인지 점검.

### 5.2. 경로(Path) 선택 기준 (절대 경로 vs 상대 경로)
상대 경로 (Relative Path): 프로젝트 단위의 이동성을 높여주므로 Dockerfile 작성, 프로젝트 빌드 컨텍스트 지정 시 재현성을 확보하는 데 유리합니다. (예: docker build -t my-web .)

절대 경로 (Absolute Path): 스크립트 실행 위치에 관계없이 일관성을 유지해야 하거나, 바인드 마운트 지정 시 의도치 않은 위치 참조를 방지하기 위해 사용합니다. (예: -v $(pwd)/app:/data 또는 -v /Users/.../app:/data)

### 5.3. 포트 충돌 진단 및 해결 순서
포트 충돌(Bind for 0.0.0.0:8080 failed: port is already allocated) 발생 시 아래 순서로 진단 및 해결합니다.

포트 사용 확인: lsof -i :8080 또는 ss -tuln | grep 8080 (Linux) 명령으로 점유 여부 확인.

프로세스 확인: 포트를 점유 중인 프로세스의 PID 및 이름 확인.

프로세스 종료 또는 포트 변경:

기존 프로세스 종료: kill -9 <PID>

실행 포트 변경: docker run -d -p 8082:80 ...

### 5.4. 데이터 백업 및 스냅샷 전략
Docker 볼륨(mydata)을 외부 아카이브로 안전하게 백업 및 복원하는 방안입니다.

볼륨 백업 (Archive Backup):

Bash
docker run --rm -v mydata:/volume -v $(pwd):/backup ubuntu tar cvf /backup/mydata_backup.tar -C /volume .
볼륨 복원 (Restore):

Bash
docker run --rm -v mydata:/volume -v $(pwd):/backup ubuntu tar xvf /backup/mydata_backup.tar -C /volume

## 6. Git 및 GitHub 동기화 및 트러블슈팅

### 6.1. 트러블슈팅 내역
1) 하위 디렉토리 .git 충돌 해결
문제 가설 및 증상: practice/ 디렉토리 내부의 독립된 .git으로 인해 상위 디렉토리에서 git add . 실행 시 서브모듈 인덱싱 에러 발생 (error: 'practice/' does not have a commit checked out).

조치 과정:

Bash
dncjf552523857@c1r4s3 woochul_codyssey % rm -rf practice/.git
dncjf552523857@c1r4s3 woochul_codyssey % git rm --cached practice 2>/dev/null
dncjf552523857@c1r4s3 woochul_codyssey % git add .
결과: practice/ 하위 파일들이 최상위 저장소(woochul_codyssey) 단일 Git 구조로 정상 등록(Staging)됨.

2) GitHub 인증 실패 해결 (PAT 적용)
문제 가설 및 증상: GitHub 비밀번호 인증 중단 정책으로 인해 git push 실패 (Invalid username or token. Password authentication is not supported).

조치 과정: GitHub Developer Settings에서 Personal Access Token(PAT, repo 권한)을 발급받아 비밀번호 입력 창에 토큰 값을 입력.

결과: 원격 저장소(origin/main) 푸시 성공.

Bash
dncjf552523857@c1r4s3 woochul_codyssey % git push origin main
Username for '[https://github.com](https://github.com)': woochul0516
Password for '[https://woochul0516@github.com](https://woochul0516@github.com)': 
To [https://github.com/woochul0516/woochul_codyssey](https://github.com/woochul0516/woochul_codyssey)
   2540f4a..c4fcc1c  main -> main

## 7. 문제 해결 이력 요약

문제 유형,원인 (가설),조치 명령,결과
Git 서브모듈 충돌,practice/.git 중복 존재,rm -rf practice/.gitgit rm --cached practice,최상위 저장소로 단일 통합 성공
GitHub Push 인증 오류,계정 비밀번호 인증 방식 중단,PAT(Personal Access Token) 발급 후 입력,원격 저장소 푸시 성공

## 8. 최종 제출 명령
# 변경 사항 스테이징 및 커밋
git add .
git commit -m "docs: 개발 워크스테이션 미션 보고서 작성 및 Git 설정 오류 해결"

# 원격 저장소 최종 푸시 (비밀번호 입력 창에 토큰(PAT) 입력)
git push origin main