import requests
import os

TOKEN = os.environ.get('SLACK_TOKEN')

'''
List channels created in Slack
'''
def channels():
	url = 'https://www.slack.com/api/channels.list?token={0}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['channels']]

'''
List all registered users
'''
def users():
	url = 'https://www.slack.com/api/users.list?token={0}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['members']]


'''
List all emojis and the images they point to
'''
def emoji():
	# Test token
	url = 'https://www.slack.com/api/emoji.list?token=xoxp-2356228633-2758427903-3769369696-b12b48'
	response = requests.get(url).json()
	return response['emoji']

	
if __name__ == '__main__':
	print(channels())
	print(users())
	print(emoji())