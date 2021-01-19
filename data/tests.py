from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase

client = Client()


class TestCategories(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
                        "name": "Category 1",
                        "children": [
                            {
                                "name": "Category 1.1",
                                "children": [
                                    {
                                        "name": "Category 1.1.1",
                                        "children": [
                                            {
                                                "name": "Category 1.1.1.1"
                                            },
                                            {
                                                "name": "Category 1.1.1.2"
                                            },
                                            {
                                                "name": "Category 1.1.1.3"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Category 1.1.2",
                                        "children": [
                                            {
                                                "name": "Category 1.1.2.1"
                                            },
                                            {
                                                "name": "Category 1.1.2.2"
                                            },
                                            {
                                                "name": "Category 1.1.2.3"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Category 1.2",
                                "children": [
                                    {
                                        "name": "Category 1.2.1"
                                    },
                                    {
                                        "name": "Category 1.2.2",
                                        "children": [
                                            {
                                                "name": "Category 1.2.2.1"
                                            },
                                            {
                                                "name": "Category 1.2.2.2"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
        cls.get_2 = {
                        "id": 2,
                        "name": "Category 1.1",
                        "children": [
                            {
                                "id": 3,
                                "name": "Category 1.1.1"
                            },
                            {
                                "id": 7,
                                "name": "Category 1.1.2"
                            }
                        ],
                        "parents": [
                            {
                                "id": 1,
                                "name": "Category 1"
                            }
                        ],
                        "siblings": [
                            {
                                "id": 11,
                                "name": "Category 1.2"
                            }
                        ]
                    }
        cls.get_8 = {
                        "id": 8,
                        "name": "Category 1.1.2.1",
                        "children": [],
                        "parents": [
                            {
                                "id": 7,
                                "name": "Category 1.1.2"
                            },
                            {
                                "id": 2,
                                "name": "Category 1.1"
                            },
                            {
                                "id": 1,
                                "name": "Category 1"
                            }
                        ],
                        "siblings": [
                            {
                                "id": 9,
                                "name": "Category 1.1.2.2"
                            },
                            {
                                "id": 10,
                                "name": "Category 1.1.2.3"
                            }
                        ]
                    }

        client.post(
            reverse('categories'),
            data=cls.data,
            content_type='application/json'
        )

    def test_2_get_2(self):
        response = client.get(reverse('category', args=[2]))
        self.assertEqual(response.data, self.get_2)

    def test_get_8(self):
        response = client.get(reverse('category', args=[8]))
        self.assertEqual(response.data, self.get_8)
