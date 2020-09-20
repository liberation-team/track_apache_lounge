# Track the new Apache HTTP Server announcements on www.apachelounge.com

The python script can help you to get the Slack notification when the new Apache HTTP server Server binaries issued on www.apachelounge.com website (see the https://www.apachelounge.com/Changelog-2.4.html page)


Run the script periodically using cron each 1-2 hours and when the new announcement appears on the changelog web-page, the script will send the notification to the Slack, using webhook URL.

To test script, export the environment variable `SLACK_WEBHOOK_URL` and run it in the console:

```sh
export SLACK_WEBHOOK_URL='https://hooks.slack.com/services/XXXX/YYYY/zzzzz'
./apache_track.py
```
