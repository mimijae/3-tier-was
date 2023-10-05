# thesis-test-was

## db 마이그레이트
```bash
docker-compose run web python manage.py migrate
```
## 데이터 삽입 명령어
```bash
sudo docker-compose exec web python manage.py seed_fruits
```
## Ubuntu(도커 환경설정)

1. 시스템의 패키지 리스트를 최신 상태로 업데이트:
```bash
sudo apt-get update
```

2. 시스템에 설치된 이전 Docker 버전들을 제거 (만약 설치되어 있다면):
```bash
sudo apt-get remove docker docker-engine docker.io
```

3. Docker를 설치:
```bash
sudo apt install docker.io
```

4. Docker 서비스를 시작:
```bash
sudo systemctl start docker
```

5. 부팅 시 Docker가 자동으로 시작되도록 설정:
```bash
sudo systemctl enable docker
```

6. 설치된 Docker의 버전을 확인:
```bash
docker --version
```

7. docker-compose 설치:
```bash
sudo apt install docker-compose
```
