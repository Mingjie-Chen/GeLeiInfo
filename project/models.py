from project import db, app


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict

class Profile(db.Model):
    __tablename__ = 'profile'
    uid = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(64), unique=True)


class Video(db.Model):
    __tablename__ = 'video'
    vid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    uid = db.Column(db.Integer, index = True)
    name = db.Column(db.String(64), unique = True)
    text = db.Column(db.Text)
    language = db.Column(db.String(64))


