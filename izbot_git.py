import discord

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		await client.delete_message(message)	

@client.event
async def on_voice_state_update(before, after):
	voicechannel = after.voice_channel
	print(after, "is in", voicechannel)
	print("after", type(after.voice_channel))
	print("before", type(before.voice_channel))
	if before.voice_channel == after.voice_channel:
		return
	if before.voice_channel is None:
		for channel in after.server.channels:
			if channel.type.name == "text" and channel.name == "general":
				print(channel, channel.type.name, "set as text channel")
				msg = after.name + " joined channel"
				await client.send_message(channel, msg, tts=True)
	elif after.voice_channel is None:
		for channel in after.server.channels:
			if channel.type.name == "text" and channel.name == "general":
				print(channel, channel.type.name, "set as text channel")
				msg = after.name + " left channel"
				await client.send_message(channel, msg, tts=True)
	else:
		return
	
	
		
@client.event
async def on_ready():  
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('[REDACTED]')