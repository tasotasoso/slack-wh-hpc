![](https://github.com/<OWNER>/<REPOSITORY>/workflows/<WORKFLOW_NAME>/badge.svg)

# slack-wh-hpc

Slack incoming-webhook client tool for people doing high performance computing.

This client is created to have the following features.
- The client reads Webhook URL from preset enviroment variable. You don't worry about accidentally publishing your webhook-URL.
- The client provides useful functions to those who are using slack for high performance computing

## How to install
To install from source:
<pre>
sudo python setup.py install
</pre>

## Usage
Simplly notification to your slack webhook app:
<pre>
import slack-wh-hpc

#You must be set slack webhook-URL to "slack_wh_url" in advance.
slack_wh_hpc = slack-wh-hpc("slack_wh_url")

slack_wh_hpc.post("This calculation is finished!")
</pre>

Notification with calculate time:
<pre>
import slack-wh-hpc

slack_wh_hpc = slack-wh-hpc("slack_wh_url")

with slack_wh_hpc.post_with_time("This calculation is finished!"):
    #Your calculation
</pre>
