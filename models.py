from config import db, ma

class Fighter(db.Model):
    __tablename__ = 'fighter'
    position_id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(32))
    wclass = db.Column(db.String(5))
    rank = db.Column(db.Integer)
    date = db.Column(db.DateTime)

class FighterSchema(ma.ModelSchema):
    class Meta:
        model = Fighter
        sqla_session = db.session
