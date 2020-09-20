#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import yaml
import os.path
from os import environ
from slack_webhook import Slack


if "SLACK_WEBHOOK_URL" in environ and environ["SLACK_WEBHOOK_URL"]:
    slack_webhook_url = environ["SLACK_WEBHOOK_URL"]
else:
    raise Exception("Empty Slack webhook url")

url = "https://www.apachelounge.com/Changelog-2.4.html"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}

date_regex = re.compile(r"\d+-\w+-\d{4}")
apache_regex = re.compile(r"Apache\s2\.4\.\d+")

file_path = "announcements.yaml"

last_dict = dict()
current_dict = dict()
new_announcements = ""


if os.path.isfile(file_path):
    with open(file_path, "r") as in_file:
        last_dict = yaml.load(in_file, Loader=yaml.SafeLoader)

response = requests.get(url, headers=headers)
if response.status_code == requests.codes.ok:
    html_doc = response.content
    soup = BeautifulSoup(html_doc, "html.parser")
    announcements_list = soup.find_all("b")
else:
    response.raise_for_status()

for item in announcements_list:
    match_version = apache_regex.search(str(item))
    match_date = date_regex.search(str(item))
    if match_version and match_version.group() and match_date and match_date.group():
        current_dict[match_date.group()] = match_version.group()

if last_dict:
    for item in current_dict:
        if item not in last_dict:
            new_announcements += f"* {item}: *{current_dict[item]}*\n"

if new_announcements or not os.path.isfile(file_path):
    with open("announcements.yaml", "w") as out_file:
        yaml.dump(current_dict, out_file)
    if new_announcements:
        message = f"Check the new Apache HTTP Server announcements on {url}: \n{new_announcements}"
        slack = Slack(url=slack_webhook_url)
        slack.post(text=message)


