from flask_testing import TestCase
from .db_setup import setup_default
from app.main import db
from manage import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()
        setup_default(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()