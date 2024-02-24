# Practice Line Message API
This project uses conda to manage python and pip on ubuntu22.04, and uses ngrok to establish API services and connect to Line Messaging API.

# Dependent
OS : ubuntu 22.04

Package management : conda (Include python3.10 & pip)

## Step
1. git this code

`git clone this_github_url`

2. Move directory to Line_msg_api_magic

`cd Line_msg_api_magic`

3. Installation Environment

`sh requirements.sh`

If you want to know the details, requirements.sh contains:

3.1 download & install conda

3.2 Create a conda environment(include python3.10 & pip)

3.3 install Flask

3.4 install line-bot-sdk

3.5 install ngrok

4. Run the following command to add your authtoken to the default ngrok.yml

`ngrok config add-authtoken your_token`

You can obtain the above token through ngrok(https://dashboard.ngrok.com/get-started/your-authtoken)

5. Obtain channel secret & channel access token from line developers(https://developers.line.biz/console/)

channel_access_token:
![channel_access_token](https://github.com/Evanston0624/Line_msg_api_magic/blob/main/sample_image/channel_access_token.jpg)

channel_secret:
![channel_secret](https://github.com/Evanston0624/Line_msg_api_magic/blob/main/sample_image/channel_secret.jpg)

Copy the access_token and Channel secret to lines 22 and 24 of line_bot_server.py
```
# channel access token
access_token = 'your channel access token'
        
# LINE Channel secret
secret = 'your channel secret'
```

6. Run the line_bot_server
`sh run_line_bot.sh`

7. Your Webhook URL will be displayed on the terminal, set it on line_developers!

Webhook:
![Webhook](https://github.com/Evanston0624/Line_msg_api_magic/blob/main/sample_image/webhook.jpg)