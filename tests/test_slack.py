import os
import unittest

import responses
from slack import Slack


class TestSlack(unittest.TestCase):

    @responses.activate
    def test_post(self):
        slack_webhook_url = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX"
        os.environ["url_env"] = slack_webhook_url
        responses.add(responses.POST, slack_webhook_url,
                      body="ok", status=200)

        slack = Slack("url_env")
        response_text = slack.post("test")
        self.assertEqual("ok", response_text)

    def test_no_url(self):
        slack = Slack("no_url_env")
        response_text = slack.post("test")
        self.assertEqual("ng_key_error", response_text)


if __name__ == '__main__':
    unittest.main()
