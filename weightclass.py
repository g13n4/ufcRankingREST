from flask import (
    make_response,
    abort,
)
import datetime
from models import (
    Fighter,
    FighterSchema,
)
decoded_name = lambda name: ' '.join(name.split('-'))


def weightclass_at_date(weight,date):
    date = datetime.datetime(*map(int,date.split('-')))
    fighter = (Fighter.query
               .with_entities(Fighter.full_name,
                                            Fighter.wclass,
                                            Fighter.rank)
               .filter(Fighter.wclass == weight and Fighter.date < date)
               .limit(10).all())

    if fighter is not None:
        fighter_schema = FighterSchema(many=True)
        data = fighter_schema.dump(fighter)
        return data
    else:
        abort(
            404,
            f"The weight class is not found: {weight}",
        )
