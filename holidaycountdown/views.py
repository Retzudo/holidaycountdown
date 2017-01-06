from flask import render_template

from holidaycountdown import app, holidays_list
from holidaycountdown.holidays import get_next_holiday


@app.route('/')
def index():
    next_holiday = get_next_holiday(holidays_list)

    return render_template('index.html', holiday=next_holiday)
