from setuptools import setup

setup(
    name='holidaycountdown',
    packages=['holidaycountdown'],
    include_package_data=True,
    install_requires=[
        'flask',
        'icalendar',
    ],
)
