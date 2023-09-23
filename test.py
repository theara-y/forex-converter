from unittest import TestCase

from app import app

class AppTestCase(TestCase):
    def test_homepage(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Forex Converter', html)

    def test_homepage_display_conversion_result(self):
        with app.test_client() as client:
            resp = client.get('/?cur=USD&amt=100')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Forex Converter', html)
            self.assertIn('&#36; 100.00', html)

    def test_redirect_validation_failure(self):
        with app.test_client() as client:
            resp = client.get('/validate', query_string={'from': '', 'to': '', 'amt': ''})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/")

    def test_follow_redirect_validation_failure(self):
        with app.test_client() as client:
            resp = client.get('/validate', follow_redirects = True, query_string = {'from': '', 'to': '', 'amt': ''})
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Forex Converter', html)
            self.assertIn('is required!', html)

    def test_redirect_validation_success(self):
        with app.test_client() as client:
            resp = client.get('/validate', query_string={'from': 'usd', 'to': 'eur', 'amt': '50'})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/convert?from=USD&to=EUR&amt=50")

    def test_redirect_conversion_success(self):
        with app.test_client() as client:
            resp = client.get('/convert', query_string = {'from': 'usd', 'to': 'eur', 'amt': '1'})

            self.assertEqual(resp.status_code, 302)
            self.assertRegex(resp.location, "/?cur=EUR&amt=\w+")

    def test_redirect_conversion_failure(self):
        with app.test_client() as client:
            resp = client.get('/convert', query_string = {'from': 'usd', 'to': 'eur', 'amt': '0'})
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/")

    def test_follow_redirect_conversion_failure(self):
        with app.test_client() as client:
            resp = client.get('/convert', follow_redirects = True, query_string = {'from': 'usd', 'to': 'eur', 'amt': '0'})
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Error: failed to convert", html)

    def test_currencies(self):
        with app.test_client() as client:
            resp = client.get('/currencies')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("USD", html)
            self.assertIn("EUR", html)