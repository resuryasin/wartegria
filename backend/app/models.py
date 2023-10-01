from app import db

class Warteg(db.Model):
    id = db.Column('warteg_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(100), nullable=True)
    addr = db.Column(db.String(200), nullable=True) 
    dist = db.Column(db.Integer, nullable=True)
    def __init__(self, name, desc, addr, dist):
        self.name = name
        self.desc = desc
        self.addr = addr
        self.dist = dist
