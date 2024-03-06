import  requests
import threading
import time
import random

def send_request(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    print(f"Время выполнения запроса: {end_time - start_time} секунд")

url = 'http://127.0.0.1:8000/test'  # замените на ваш URL

start_time = time.time()

threads = []

for i in range(1000):
    thread = threading.Thread(target=send_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Общее время выполнения: {end_time - start_time} секунд")
