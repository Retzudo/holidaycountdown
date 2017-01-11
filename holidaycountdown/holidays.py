from functools import total_ordering

from icalendar import Calendar
from datetime import date


@total_ordering
class Holiday:
    """A class representing a holiday consisting of its date and name."""
    def __init__(self, holiday_date: date, name: str):
        self.holiday_date = holiday_date
        self.name = name

    def __str__(self):
        return '{} on {}'.format(
            self.name,
            self.holiday_date,
        )

    def __lt__(self, other):
        return self.holiday_date < other.holiday_date

    def __eq__(self, other):
        return self.holiday_date == other.holiday_date


def read_holidays(ics_location: str) -> Calendar:
    """Read a ICS file and return a Calendar object."""
    with open(ics_location) as f:
        ics = f.read()

    return Calendar.from_ical(ics)


def convert_holidays(calendar: Calendar) -> list:
    """Convert dates in a Calendar object to a list of Holiday objects.
    
    Also only include holidays that are not on weeksends and by law.
    """
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
    """Return a Holiday object for the next holiday coming."""
    today = date.today()
    for holiday in holidays:
        if holiday.holiday_date > today:
            return holiday
