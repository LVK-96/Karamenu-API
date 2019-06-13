from django.test import TestCase
from apps.menu_parser.serializers import CourseSerializer
from apps.menu_parser.course import Course


class CourseSerializerTest(TestCase):
    def setUp(self):
        self.course1 = Course("Test category", "Testi nimi", "Test name",
                              "Testi kuvaus", "Test description", "T, E, S, T",
                              "6,60 / 8,90") 
        self.course2 = Course("FROM THE ÄIJÄT :D", "Tomi Björk :D",
                              "Tom Bjoercks :D", "RSÄ :D", "RSA :D", "R, S, Ä",
                              "5 / 5")
        serializer = CourseSerializer([self.course1, self.course2], 
                                      many=True).data
        self.serializer_data1 = serializer[0]
        self.serializer_data2 = serializer[1]

    def test_contains_correct_fiels(self):
        self.assertCountEqual(self.serializer_data1.keys(),
                              ['category', 'name_fi', 'name_en', 'desc_fi',
                               'desc_en', 'tags', 'price'])

        self.assertCountEqual(self.serializer_data2.keys(),
                              ['category', 'name_fi', 'name_en', 'desc_fi',
                               'desc_en', 'tags', 'price'])

    def test_category_content(self):
        self.assertEqual(self.course1.category,
                         self.serializer_data1['category'])
        self.assertEqual(self.course2.category,
                         self.serializer_data2['category'])

    def test_name_fi_content(self):
        self.assertEqual(self.course1.name_fi,
                         self.serializer_data1['name_fi'])
        self.assertEqual(self.course2.name_fi,
                         self.serializer_data2['name_fi'])

    def test_name_en_content(self):
        self.assertEqual(self.course1.name_en,
                         self.serializer_data1['name_en'])
        self.assertEqual(self.course2.name_en,
                         self.serializer_data2['name_en'])

    def test_desc_fi_content(self):
        self.assertEqual(self.course1.desc_fi,
                         self.serializer_data1['desc_fi'])
        self.assertEqual(self.course2.desc_fi,
                         self.serializer_data2['desc_fi'])

    def test_desc_en_content(self):
        self.assertEqual(self.course1.desc_en,
                         self.serializer_data1['desc_en'])
        self.assertEqual(self.course2.desc_en,
                         self.serializer_data2['desc_en'])

    def test_tags_content(self):
        self.assertEqual(self.course1.tags,
                         self.serializer_data1['tags'])
        self.assertEqual(self.course2.tags,
                         self.serializer_data2['tags'])

    def test_price_content(self):
        self.assertEqual(self.course1.price,
                         self.serializer_data1['price'])
        self.assertEqual(self.course2.price,
                         self.serializer_data2['price'])