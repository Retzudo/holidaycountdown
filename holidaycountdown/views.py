import arrow
from flask import render_template, jsonify

from holidaycountdown import app, holidays_list
from holidaycountdown.holidays import get_next_holiday


@app.route('/')
def index():
    next_holiday = get_next_holiday(holidays_list)

    return render_template(
        'index.html',
        holiday=next_holiday,
        human_date=arrow.get(next_holiday.holiday_date).humanize(locale='de_at')
    )


@app.route('/next.json')
def next_holiday():
    holiday = get_next_holiday(holidays_list)
    arrow_date = arrow.get(holiday.holiday_date)

    return jsonify({
        'date': holiday.holiday_date.isoformat(),
        'name': holiday.name,
        'humanized': {
            'de_at': arrow_date.humanize(locale='de_at'),
            'en_gb': arrow_date.humanize(locale='en_gb'),
        },
    })