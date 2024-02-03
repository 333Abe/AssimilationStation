from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    subtopics = db.relationship('Subtopic', backref='topic', lazy=True)

class Subtopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtopic = db.Column(db.String(100), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    cards = db.relationship('Card', backref='subtopic', lazy=True)
    note = db.relationship('Note', backref='subtopic', lazy=True)

# Association Table for Many-to-Many Relationship between Card and Note
card_notes_association = db.Table('card_note_association',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'))
)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    last_answered_date = db.Column(db.Date)
    last_answered_correct = db.Column(db.Boolean)
    consecutive_correct = db.Column(db.Integer, default=0)
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.id'))
    note = db.relationship('note', secondary=card_notes_association, backref='cards', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.id'))
    cards = db.relationship('Card', secondary=card_notes_association, backref='note', lazy=True)

