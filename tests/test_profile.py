import unittest
import os
from app import db, create_app
from app.models.profile import Profile

class TestProfileModel(unittest.TestCase):
    
    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        db.create_all()
        
    def tearDown(self):
        db.session.rollback()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_profile_creation(self):
        profile = Profile(user_id = 1, role_id = 1)
        db.session.add(profile)
        db.session.commit()
        
        self.assertEqual(profile.user_id, 1)
        self.assertEqual(profile.role_id, 1)

if __name__ == "__main__":
    unittest.main()