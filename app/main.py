from kafka import KafkaProducer
import json

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

fib_values = [10, 100, 56]
for value in fib_values:
    fib_result = fibonacci(value)
    producer.send('fibonacci_topic', value=fib_result)
producer.flush()