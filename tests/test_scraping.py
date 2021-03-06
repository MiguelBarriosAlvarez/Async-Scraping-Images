import requests
import responses
import unittest


class Test_Request(unittest.TestCase):

    @responses.activate
    def testExample(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'https://www.bing.com/images/search?q="mercedes"&FORM=HDRSC2',
            'body': '{"error": "reason"}',
            'status': 404,
            'content_type': 'application/json',
            'adding_headers': {'X-Foo': 'Bar'}
        })
        response = requests.get('https://www.bing.com/images/search?q="mercedes"&FORM=HDRSC2')
        self.assertEqual({'error': 'reason'}, response.json())
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()