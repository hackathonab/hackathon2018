from app import db


social_media_identifier = db.Table('social_media_identifier',
                          db.Column('county_id', db.Integer, db.ForeignKey('counties.id')),
                          db.Column('handle_id', db.Integer, db.ForeignKey('handles.id')))

class County(db.Model):
    __tablename__ = 'counties'
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64))

class SocialMediaHandle(db.Model):
    __tablename__ = 'handles'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(64))
    platform = db.Column(db.String(64))