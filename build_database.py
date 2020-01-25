import os
from config import db
from models import Fighter
import datetime
import json

FIGHTERS = json.load(open('all_rankings_dicts.json','r'))

if os.path.exists('fighters.db'):
    os.remove('fighters.db')


db.create_all()

str_to_datetime = lambda x: datetime.date(*map(int,x.split('-')))

for fighter in FIGHTERS:
    fighter['date'] = str_to_datetime(fighter['date'])
    f = Fighter(**fighter)
    db.session.add(f)

db.session.commit()
