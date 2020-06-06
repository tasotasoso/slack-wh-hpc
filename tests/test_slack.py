import unittest

from slack import Slack


class TestSlack(unittest.TestCase):

    def test_post(self):
        slack = Slack("slack_webhook_url")
        response_text = slack.post("test")
        self.assertEqual("ok", response_text)

    def test_no_url(self):
        slack = Slack("no_url_env")
        response_text = slack.post("test")
        self.assertEqual("ng_key_error", response_text)

if __name__ == '__main__':
    unittest.main()
