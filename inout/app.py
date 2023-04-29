from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

images = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
    "image5.jpg"
    
]

@app.route('/')
def daily_image():
    # 현재 날짜를 기준으로 무작위 시드 설정
    today = datetime.date.today()
    random.seed(today.toordinal())

    image = random.choice(images)
    return render_template('daily_image.html', image=image)

if __name__ == '__main__':
    app.run(debug=True)