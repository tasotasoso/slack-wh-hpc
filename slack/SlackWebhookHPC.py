import contextlib
import json
import os
import time
from typing import Iterator

import requests


class Client:
    """Base Class for posts your message to your external app.
    """

    def __init__(self, url_env: str) -> None:
        self.url_env = url_env
        self.common_failed_msg = "Failed to notificate."

    def post(self, text: str) -> str:
        """Post message to external app.
        This function posts your message to your external app.
        URL for post is got by enviroment variable your had set.

        Args:
            text(str): your message for Slack Webhook app.

        Return:
             result_message(str): Result of post. 
        """
        params = {"text": text}

        try:
            url = os.environ[self.url_env]
        except KeyError as e:
            print(
                self.common_failed_msg +
                'catch KeyError:',
                e)
            print("There are no URL, please set.")
            result_message = "ng_key_error"
            return result_message

        try:
            r = requests.post(url, data=json.dumps(params))
        except requests.exceptions.ConnectionError as e:
            print(self.common_failed_msg + 'catch ConnectionError:', e)
        except requests.exceptions.HTTPError as e:
            print(self.common_failed_msg + 'catch HTTPError:', e)
        except requests.exceptions.Timeout as e:
            print(self.common_failed_msg + 'catch Timeout:', e)
        except requests.exceptions.TooManyRedirects as e:
            print(self.common_failed_msg + 'catch TooManyRedirects:', e)
        except BaseException:
            print(self.common_failed_msg + 'catch unexpected Error')

        if r.status_code != 200:
            error_msg = "HTTP {} ERROR!".format(r.status_code)
            print(self.common_failed_msg + "{} error occur.".format(error_msg))

        result_message = r.text
        return result_message


class Slack(Client):
    """Class for Slack webhook app to posts your message.
    """

    def __init__(self, url_env: str) -> None:
        super().__init__(url_env)
        self.common_failed_msg = "Failed to notificate to your slack web hook app."

    @contextlib.contextmanager
    def post_with_time(self, text: str) -> Iterator[None]:
        """Post your message to your Slack webhook app with time in "with" syntax.
        """
        st = time.time()
        try:
            yield
        finally:
            et = time.time()
            text_time = "Whole time: {} s".format(et - st)
            payload = text + "\n" + text_time
            self.post(payload)
