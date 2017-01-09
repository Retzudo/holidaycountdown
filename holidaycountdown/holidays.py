from functools import total_ordering

from icalendar import Calendar
from datetime import date


@total_ordering
class Holiday:
    def __init__(self, holiday_date: date, name: str):
        self.holiday_date = holiday_date
        self.name = name

    def __str__(self):
        return '{} on {}.{}.{}'.format(
            self.name,
            self.holiday_date.year,
            self.holiday_date.month,
            self.holiday_date.day,
        )

    def __lt__(self, other):
        return self.holiday_date < other.holiday_date

    def __eq__(self, other):
        return self.holiday_date == other.holiday_date


def read_holidays(ics_location: str) -> Calendar:
    with open(ics_location) as f:
        ics = f.read()

    return Calendar.from_ical(ics)


def convert_holidays(calendar: Calendar) -> list:
    holidays = []
    today = date.today()

    for item in calendar.walk():
        if 'DTSTART' in item:
            holiday_date = item.decoded('DTSTART')
            by_law = '§' in item.get('SUMMARY')
            is_weekday = holiday_date.weekday() not in [5, 6]
            if holiday_date > today and by_law and is_weekday:
                holidays.append(Holiday(
                    holiday_date,
                    item.get('SUMMARY').replace(' (§)', '')
                ))

    return sorted(holidays)


def get_next_holiday(holidays: list) -> Holiday:
    today = date.today()
    for holiday in holidays:
        if holiday.holiday_date > today:
            return holiday
