from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

# 앞서서 트위터 개발자 계정에서 받아온 토큰 입력해놓기 
access_token = "(get your own)" 
access_token_secret =  "(get your own)"
consumer_key =  "(get your own)"
consumer_secret =  "(get your own)"

# tweepy에서는 listener를 만든다. 
class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

#"trump"에 해당하는 스트림을 받아오기. 
stream.filter(track="trump")
