import requests
import os

TOKEN = os.environ.get('SLACK_TOKEN')

def channels():
	url = 'https://slack.com/api/channels.list?token={}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['channels']]

def users():
	url = 'https://slack.com/api/users.list?token={}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['members']]

def emoji():
	url = 'https://slack.com/api/emoji.list?token={}'.format(TOKEN)
	response = requests.get(url).json()
	return response['emoji']

	
if __name__ == '__main__':
	print(channels())
	print(users())
	print(emoji())