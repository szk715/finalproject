import json
from django.test import TestCase, RequestFactory
from matchuser.models import Matchuser
from .views import save, update

class MatchuserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.matchuser_data = {
            'matchid': 1,
            'name': 'Test User',
            'reserve1': 'reserve1_value',
            'reserve2': 'reserve2_value',
            'reserve3': 'reserve3_value',
            'reserve4': 'reserve4_value',
            'reserve5': 'reserve5_value',
            'status': 'status_value'
        }

    def test_save(self):
        request = self.factory.post(
            '/matchuser/save',
            content_type='application/json',
            data=json.dumps(self.matchuser_data)
        )
        response = save(request)
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content.decode())
        self.assertTrue(content['success'])
        self.assertEqual(content['message'], '新增成功')

        saved_matchuser = Matchuser.objects.get(name='Test User')
        self.assertIsNotNone(saved_matchuser)
        self.assertEqual(saved_matchuser.matchid, 1)

    def test_update(self):
        matchuser = Matchuser.objects.create(**self.matchuser_data)
        updated_data = {**self.matchuser_data, 'id': matchuser.id, 'name': 'Updated User'}

        request = self.factory.post(
            '/matchuser/update',
            content_type='application/json',
            data=json.dumps(updated_data)
        )
        response = update(request)
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content.decode())
        self.assertTrue(content['success'])
        self.assertEqual(content['message'], '修改成功')

        updated_matchuser = Matchuser.objects.get(id=matchuser.id)
        self.assertIsNotNone(updated_matchuser)
        self.assertEqual(updated_matchuser.name, 'Updated User')