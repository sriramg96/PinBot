import discord
import os

# Token will have to be updated accordingly
TOKEN = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    emoji = payload.emoji
    print("Channel: ", channel)
    print("Message: ", message.content)
    print("Is pinned: ", message.pinned)
    print("A reaction has been added: {}".format(str(emoji)))
    if str(emoji) == "📌" and not message.pinned:
        print("About to pin message")
        print(message.type)
        if message.type == discord.MessageType.default:
            await message.pin()
            print("Successfully pinned message")

@client.event
async def on_raw_reaction_remove(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    emoji = payload.emoji
    print("A reaction has been removed: {}".format(str(emoji)))
    if str(emoji) == "📌" and message.pinned:
        pin_check = False
        for react in message.reactions:
            if "📌" == react.emoji:
                pin_check = True
                break
        if not pin_check:
            print("About to unpin message")
            await message.unpin()
            print("Successfully unpinned message")

client.run(TOKEN)
