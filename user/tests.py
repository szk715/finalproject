import json
from django.test import TestCase, Client
from django.urls import reverse
from user.models import UserInfo


class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.info_url = reverse('info')
        self.delete_url = reverse('delete')
        self.login_url = reverse('login')
        self.save_url = reverse('save')
#        self.page_url = reverse('page')
        self.update_url = reverse('update')

        self.user1 = UserInfo.objects.create(username="user1", password="pass1", type=1)
        self.user2 = UserInfo.objects.create(username="user2", password="pass2", type=2)



    def test_info(self):
        response = self.client.get('/user/info', {'id': self.user1.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())
        self.assertEqual(response.json()['data']['username'], 'user1')

    def test_delete(self):
        response = self.client.get('/user/delete', {'id': self.user1.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertEqual(UserInfo.objects.filter(id=self.user1.id).count(), 0)

    def test_login(self):
        response = self.client.post('/user/login', json.dumps({"username": "user1", "password": "pass1"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())
        self.assertEqual(response.json()['data']['username'], 'user1')

    def test_save(self):
        response = self.client.post('/user/registry',
                                    json.dumps({"username": "user3", "password": "pass3", "type": 3}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())
        self.assertEqual(UserInfo.objects.filter(username='user3').count(), 1)

    def test_page(self):
        response = self.client.post('/user/page', json.dumps({"pageNum": 1, "pageSize": 2, "username": ""}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())
        self.assertTrue('total' in response.json())
        self.assertEqual(len(response.json()['data']), 2)
        self.assertEqual(response.json()['total'], 2)

    def test_update(self):
        response = self.client.post('/user/update', json.dumps(
            {"id": self.user1.id, "username": "updated_user1", "password": "updated_pass1", "type": 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())

        updated_user = UserInfo.objects.get(id=self.user1.id)
        self.assertEqual(updated_user.username, 'updated_user1')
        self.assertEqual(updated_user.password, 'updated_pass1')
        self.assertEqual(updated_user.type, 1)