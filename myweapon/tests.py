import json
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from myweapon.models import Myweapon

# Create your tests here.
class MyweaponTestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_save(self):
        data = {
                "name": "TestWeapon",
                "reserve1": "TestReserve1",
                "reserve2": "TestReserve2",
                "reserve3": "TestReserve3",
                "reserve4": "TestReserve4",
                "reserve5": "TestReserve5",
                "status": 1,
                "user": "TestUser",
            }

        response = self.client.post('/myweapon/save', json.dumps(data), content_type='application/json;charset=utf-8')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['message'], '新增成功')
        self.assertEqual(response_data['data'], data)

    def test_update(self):
                myweapon = Myweapon.objects.create(
                    name="OldWeapon",
                    reserve1="OldReserve1",
                    reserve2="OldReserve2",
                    reserve3="OldReserve3",
                    reserve4="OldReserve4",
                    reserve5="OldReserve5",
                    status=1,
                    user="OldUser"
                )

                update_data = {
                    "id": myweapon.id,
                    "name": "NewWeapon",
                    "reserve1": "NewReserve1",
                    "reserve2": "NewReserve2",
                    "reserve3": "NewReserve3",
                    "reserve4": "NewReserve4",
                    "reserve5": "NewReserve5",
                    "status": '2',
                    "user": "NewUser"
                }

                response = self.client.post('/myweapon/update', json.dumps(update_data),
                                            content_type='application/json;charset=utf-8')
                self.assertEqual(response.status_code, 200)
                response_data = json.loads(response.content)
                self.assertTrue(response_data['success'])
                self.assertEqual(response_data['message'], '修改成功')
                self.assertEqual(response_data['data'], update_data)

                updated_myweapon = Myweapon.objects.get(id=myweapon.id)
                self.assertEqual(updated_myweapon.name, update_data['name'])
                self.assertEqual(updated_myweapon.reserve1, update_data['reserve1'])
                self.assertEqual(updated_myweapon.reserve2, update_data['reserve2'])
                self.assertEqual(updated_myweapon.reserve3, update_data['reserve3'])
                self.assertEqual(updated_myweapon.reserve4, update_data['reserve4'])
                self.assertEqual(updated_myweapon.reserve5, update_data['reserve5'])
                self.assertEqual(updated_myweapon.status, update_data['status'])
                self.assertEqual(updated_myweapon.user, update_data['user'])