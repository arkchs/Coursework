from flask import Flask, render_template, request
from pyngrok import ngrok
import threading
import time
app = Flask(__name__)
def print_numbers(thread_name):
    for i in range(1, 11):
        print(f"{thread_name}: {i}")
        time.sleep(1)   
@app.route('/')

@app.route('/', methods= ['GET','POST'])
def index():
    if request.method == 'GET':
        thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
        thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))
        thread1.start()
        thread2.start()
        return render_template('home.html')
    if request.method == 'POST':
       return 'In the post route'
ngrok_tunnel = ngrok.connect(5000)
print("Public URL:", ngrok_tunnel.public_url)

if __name__ == '__main__':
 app.run(debug=True)