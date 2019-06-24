from django.test import TestCase
from django.urls import reverse, resolve
# # django 1.*: from django.core.urlresolvers import reverse

# from .views import home, topics, new_topic
# from .models import Board, User, Topic, Post
# from .forms import TopicForm

# Create your tests here.
# class HomeTests(TestCase):

#     def setUp(self):
#         self.board = Board.objects.create(name='Django', description='Django board.')
#         url = reverse('home')
#         self.response = self.client.get(url)


#     def test_home_view_status_code(self):
#         self.assertEquals(self.response.status_code, 200)


#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, home)


#     def test_home_view_contains_link_to_topics_page(self):
#         topics_url = reverse('topics', kwargs={'id':self.board.id})
#         self.assertContains(self.response, f'href="{topics_url}"')



# class TopicsTests(TestCase):

#     def setUp(self):
#         Board.objects.create(name='Django', description='Django board.')


#     def test_topics_view_status_code(self):
#         url = reverse('topics', kwargs={'id':1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


#     def test_topics_view_not_found(self):
#         url = reverse('topics', kwargs={'id':99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)


#     def test_topics_url_resolves_topics_view(self):
#         view = resolve('/topics/1/')
#         self.assertEquals(view.func, topics)


#     def test_topics_view_contains_navigation_links(self):
#         url = reverse('topics', kwargs={'id':1})
#         response = self.client.get(url)

#         home_url = reverse('home')
#         new_topic_url = reverse('new_topic', kwargs={'id':1})
        
#         self.assertContains(response, f'href="{home_url}"')
#         self.assertContains(response, f'href="{new_topic_url}"')



# class NewTopicTests(TestCase):
    
#     def setUp(self):
#         Board.objects.create(name='Django', description='Django board.')
#         User.objects.create_user(username='john', email='john@doe.com', password='123')


#     def test_new_topic_view_status_code(self):
#         url = reverse('new_topic', kwargs={'id':1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


#     def test_new_topic_view_not_found(self):
#         url = reverse('new_topic', kwargs={'id':99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)


#     def test_new_topic_url_resolves_new_topics_view(self):
#         view = resolve('/topics/1/new/')
#         self.assertEquals(view.func, new_topic)


#     def test_new_topic_view_contains_link_to_topics_page(self):
#         url = reverse('new_topic', kwargs={'id':1})
#         topics_url = reverse('topics', kwargs={'id':1})
#         response = self.client.get(url)
#         self.assertContains(response, f'href="{topics_url}"')


#     def test_csrf(self):
#         url = reverse('new_topic', kwargs={'id': 1})
#         response = self.client.get(url)
#         self.assertContains(response, 'csrfmiddlewaretoken')
    

#     def test_new_topic_valid_post_data(self):
#         url = reverse('new_topic', kwargs={'id': 1})
#         data = {
#             'subject': 'Test title',
#             'message': 'Lorem ipsum dolor sit amet'
#         }
#         response = self.client.post(url, data)
#         self.assertTrue(Topic.objects.exists())
#         self.assertTrue(Post.objects.exists())


#     def test_new_topic_invalid_post_data(self):
#         '''
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         '''
#         url = reverse('new_topic', kwargs={'id': 1})
#         response = self.client.post(url, {})
#         form = response.context.get('form')
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(form.errors)


#     def test_new_topic_invalid_post_data_empty_fields(self):
#         '''
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         '''
#         url = reverse('new_topic', kwargs={'id': 1})
#         data = {
#             'subject': '',
#             'message': ''
#         }
#         response = self.client.post(url, data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFalse(Topic.objects.exists())
#         self.assertFalse(Post.objects.exists())


#     def test_new_topic_contains_form(self):
#         url = reverse('new_topic', kwargs={'id': 1})
#         response = self.client.get(url)
#         form = response.context.get('form')
#         self.assertIsInstance(form, TopicForm)



