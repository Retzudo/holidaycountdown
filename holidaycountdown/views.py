from holidaycountdown import app


@app.route('/')
def index():
    return 'Index!'
