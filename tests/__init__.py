import unittest
from jsona import flatten, JsonAPIError


class JsonaTest(unittest.TestCase):
    """Test Cases for Cloud Realty"""
    jsona = None

    def load_sample(self, sample_name):
        sample_file = open('tests/samples/{}.json'.format(sample_name), 'r')
        sample = sample_file.read()
        self.jsona = flatten(sample)

    def test_flatten_list(self):
        self.load_sample('valid_listobject')
        self.assertIsInstance(self.jsona, list)

    def test_flatten_dict(self):
        self.load_sample('valid_singleobject')
        self.assertIsInstance(self.jsona, dict)

    def test_flatten_errors(self):
        with self.assertRaises(JsonAPIError):
            self.load_sample('errors')

    def test_single_expected_results(self):
        self.load_sample('valid_singleobject')
        result = {
            'id': '1',
            'title': 'JSON API paints my bikeshed!',
            'body': 'The shortest article. Ever.',
            'author': {
                'id': '42',
                'name': 'John'
            },
        }
        self.assertDictEqual(self.jsona, result)

    def test_list_expected_results(self):
        self.load_sample('valid_listobject')
        result = [{
            'id': '1',
            'title': 'JSON API paints my bikeshed!',
            'author': {
                'id': '9',
                'first-name': 'Dan',
                'last-name': 'Gebhardt',
                'twitter': 'dgeb',
            },
            'comments': [
                {'id': '5', 'body': 'First!'},
                {'id': '12', 'body': 'I like XML better'}],
        }]
        self.assertListEqual(self.jsona, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
