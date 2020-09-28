
### 환경 설정 

-	트위터 개발자 계정을 만들어서 key(consumer Key, secret key), token(access token, secret token)을 갖고 있어야 함  
-	필요 패키지 설치 
$ pip install kafka-python
$ pip install python-twitter
$ pip install tweepy
*	tweepy 이용  (tweepy 3.6 버전 이하는 “RuntimeError: No active exception to reraised” 에러가 발생하기 때문에, 최신 버전을 이용하는지 확인한다. pip freeze를 입력하면 버전을 확인할 수 있다. 버전업이 필요한 경우 pip install --upgrade tweepy 를 입력한다.)

### tweepy로 kafka streaming 시작 및 실행
* ssh 시작 <br> 
  $	sudo service ssh start

* 주키퍼 시작(kafka 설치 경로로 들어가서 명령어 입력) <br> 
  $ bin/zookeeper-server-start.sh config/zookeeper.properties

* 카프카 시작 (ver 2.11) <br>
  $ bin/kafka-server-start.sh config/server.properties

* 토픽 생성 <br>
  $ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic trump

* 파이썬 파일 실행 <br>
  $ 파이썬 파일 경로/tweepy_kafka.py

파이썬 파일을 실행하면 다음과 같이 콘솔창에서 어떤 데이터가 수집되는지를 볼 수 있다. 이 때, 가져오는 데이터 형식은 json이다. 

* topic에서 어떤 데이터를 publish하고 있는지 확인하면 마찬가지로 가져오는 데이터 json 파일을 볼 수 있다. <br>
  $ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic trump --from-beginning
