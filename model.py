from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    
    Game.query.delete()

    testgame1 = Game(name='testgame1', description='test game description 1')
    testgame2 = Game(name='testgame2', description='test game description 2')
    testgame3 = Game(name='testgame3', description='test game description 3')

    db.session.add_all([testgame1, testgame2, testgame3])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
