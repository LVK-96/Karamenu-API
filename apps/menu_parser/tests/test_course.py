
from django.test import TestCase
from apps.menu_parser.course import Course


class CourseTest(TestCase):
    def setUp(self):
        self.test_category = "Test category"
        self.test_name_fi = "Testi nimi"
        self.test_name_en = "Test name"
        self.test_desc_fi = "Testi kuvaus"
        self.test_desc_en = "Test description"
        self.test_tags = "T, E, S, T"
        self.test_price = "6,60 / 8,90"
        self.course = Course(self.test_category, self.test_name_fi,
                             self.test_name_en, self.test_desc_fi,
                             self.test_desc_en, self.test_tags,
                             self.test_price)
        
        self.course2 = Course(self.test_category, self.test_name_fi,
                              self.test_name_en, self.test_desc_fi,
                              self.test_desc_en, self.test_tags,
                              self.test_price)
    
    def test_category(self):
        self.assertEqual(self.course.category, self.test_category)
    
    def test_name_fi(self):
        self.assertEqual(self.course.name_fi, self.test_name_fi)

    def test_name_en(self):
        self.assertEqual(self.course.name_en, self.test_name_en)

    def test_desc_fi(self):
        self.assertEqual(self.course.desc_fi, self.test_desc_fi)

    def test_desc_en(self):
        self.assertEqual(self.course.desc_en, self.test_desc_en)

    def test_tags(self):
        self.assertEqual(self.course.tags, self.test_tags)

    def test_price(self):
        self.assertEqual(self.course.price, self.test_price)

    def test_equals(self):
        self.assertTrue(self.course == self.course2)
