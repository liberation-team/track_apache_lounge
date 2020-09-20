# Track the new Apache HTTP Server announcements on www.apachelounge.com

The python script can help you to get the Slack notification when the new Apache HTTP server Server binaries issued on www.apachelounge.com website (see the https://www.apachelounge.com/Changelog-2.4.html page)


Run the script periodically using cron each 1-2 hours and when the new announcement appears on the changelog web-page, the script will send the notification to the Slack, using webhook URL.

To test script, create isolated Python environment using virtualenv, export the environment variable `SLACK_WEBHOOK_URL` and run it in the console:

```sh
git clone git@github.com:liberation-team/track_apache_lounge.git && cd track_apache_lounge
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
export SLACK_WEBHOOK_URL='https://hooks.slack.com/services/XXXX/YYYY/zzzzz'
./apache_track.py
```
