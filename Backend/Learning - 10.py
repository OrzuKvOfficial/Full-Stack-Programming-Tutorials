from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Oddiy Sahifa</title>
        </head>
        <body>
            <h1>Assalomu alaykum!</h1>
            <p>Bu oddiy Flask yordamida yaratilgan veb-sahifa.</p>
            <a href="/about">Men haqimda</a>
        </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <html>
        <head>
            <title>Men haqimda</title>
        </head>
        <body>
            <h1>Men haqimda</h1>
            <p>Bu sahifa Flask yordamida yaratildi va oddiy ma'lumotni o‘z ichiga oladi.</p>
            <a href="/">Bosh sahifaga qaytish</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
