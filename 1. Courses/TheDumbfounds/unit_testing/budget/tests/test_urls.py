from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list,project_detail,ProjectCreateView

class TestUrls(SimpleTestCase):
# list
    def test_list_url_resolved(self):
        url=reverse('list')
        self.assertEqual(resolve(url).func,project_list)
# add
    def test_project_create_url_resolved(self):
        url=reverse('add')
        self.assertEqual(resolve(url).func.view_class,ProjectCreateView)
# detail
    def test_project_detail_url_resolved(self):
        url=reverse('detail')
        self.assertEqual(resolve(url).func.view_class,ProjectCreateView)