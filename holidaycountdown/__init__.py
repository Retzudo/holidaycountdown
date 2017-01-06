from flask import Flask

from holidaycountdown import holidays

app = Flask(__name__)
app.config['ICS_LOCATION'] = 'holidays.ics'

calendar = holidays.read_holidays(app.config.get('ICS_LOCATION'))
holidays_list = holidays.convert_holidays(calendar)

import holidaycountdown.views
