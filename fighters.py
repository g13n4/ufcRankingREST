from flask import (
    make_response,
    abort,
)
from config import db
from models import (
    Fighter,
    FighterSchema,
)
decoded_name = lambda name: ' '.join(name.split('-'))

def read_all(full_name):

    fighter = Fighter.query.with_entities(Fighter.full_name,
                                            Fighter.wclass,
                                            Fighter.rank,
                                            Fighter.date).filter(Fighter.full_name == decoded_name(full_name)).all()

    if fighter is not None:
        fighter_schema = FighterSchema(many=True)
        data = fighter_schema.dump(fighter)
        return data
    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=full_name),
        )
#limit
#order_by
def read_last(full_name):
    fighter = (Fighter.query
               .with_entities(Fighter.full_name,
                                            Fighter.wclass,
                                            Fighter.rank,
                                            Fighter.date)
               .filter(Fighter.full_name == decoded_name(full_name))
               .order_by(Fighter.date.desc())).limit(1).one_or_none()

    if fighter is not None:
        fighter_schema = FighterSchema()
        data = fighter_schema.dump(fighter)
        return data
    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=full_name),
        )


def read_first(full_name):
    fighter = (Fighter.query
               .with_entities(Fighter.full_name,
                                            Fighter.wclass,
                                            Fighter.rank,
                                            Fighter.date)
               .filter(Fighter.full_name == decoded_name(full_name))
               .order_by(Fighter.date.asc())).limit(1).one_or_none()

    if fighter is not None:
        fighter_schema = FighterSchema()
        data = fighter_schema.dump(fighter)
        return data
    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=full_name),
        )
