import requests
import os

TOKEN = os.environ.get('SLACK_TOKEN')

'''
List channels created in Slack
'''
def channels():
	url = 'https://slack.com/api/channels.list?token={0}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['channels']]

'''
List all registered users
'''
def users():
	url = 'https://slack.com/api/users.list?token={0}'.format(TOKEN)
	response = requests.get(url).json()
	return [x['name'] for x in response['members']]


'''
List all emojis and the images they point to
'''
def emoji():
	url = 'https://slack.com/api/emoji.list?token={0}'.format(TOKEN)
	response = requests.get(url).json()
	return response['emoji']

	
if __name__ == '__main__':
	print(channels())
	print(users())
	print(emoji())