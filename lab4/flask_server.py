from flask import Flask, render_template, request, config

app = Flask(__name__)
app.config.update(
    PREFERRED_URL_SCHEME='https',
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hacked", methods=['POST'])
def hack():
    print(request.form)
    return 'Zostałeś zhackowany'


if __name__ == '__main__':
    app.run(
        port=443,
        ssl_context=('certA.crt', 'privkeyA.pem'))
