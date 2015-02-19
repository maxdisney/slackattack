from slackattack import slack

def testUsers():
	users = slack.users()
	assert 'max' in users
	assert 'evilmax' not in users

def testChannels():
	channels = slack.channels()
	assert 'dma-ios' in channels
	assert 'dma-ioooooooos' not in channels

def testSharkEmoji():
	emoji = slack.emoji()
	assert 'leftshark' in emoji
	assert 'rightshark' in emoji
	assert 'middleshark' not in emoji
	