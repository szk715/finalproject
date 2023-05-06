
import json
from django.test import TestCase, Client
from django.urls import reverse
from scene.models import Scene
from datetime import datetime

class SceneTestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_save(self):
        data = {
            "matchid": 123,
            "name": "Test Scene",
            "reserve1": "reserve1",
            "reserve2": "reserve2",
            "reserve3": "reserve3",
            "reserve4": "reserve4",
            "reserve5": "reserve5",
            "status": "1",
            "user": "1",
        }
        response = self.client.post('/scene/save', data=json.dumps(data), content_type='application/json;charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['success'])

        scene = Scene.objects.get(name=data['name'])
        self.assertIsNotNone(scene)
        self.assertEqual(scene.matchid, data['matchid'])

    def test_update(self):

        # Create a Scene instance to update
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scene = Scene.objects.create(create_time=now, matchid="123", name="Test Scene", reserve1="reserve1",
                                      reserve2="reserve2", reserve3="reserve3", reserve4="reserve4",
                                      reserve5="reserve5", status="1", user="1")

        # Update the scene data
        update_data = {
            "id": scene.id,
            "matchid": 456,
            "name": "Updated Test Scene",
            "reserve1": "new_reserve1",
            "reserve2": "new_reserve2",
            "reserve3": "new_reserve3",
            "reserve4": "new_reserve4",
            "reserve5": "new_reserve5",
            "status": "2",
            "user": "2",
        }

        response = self.client.post('/scene/update', data=json.dumps(update_data), content_type='application/json;charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['success'])

        # Retrieve the updated scene from the database
        updated_scene = Scene.objects.get(id=scene.id)
        self.assertEqual(updated_scene.matchid, update_data['matchid'])
        self.assertEqual(updated_scene.name, update_data['name'])
        self.assertEqual(updated_scene.reserve1, update_data['reserve1'])
        self.assertEqual(updated_scene.reserve2, update_data['reserve2'])
        self.assertEqual(updated_scene.reserve3, update_data['reserve3'])
        self.assertEqual(updated_scene.reserve4, update_data['reserve4'])
        self.assertEqual(updated_scene.reserve5, update_data['reserve5'])
        self.assertEqual(updated_scene.status, update_data['status'])
        self.assertEqual(updated_scene.user, update_data['user'])

