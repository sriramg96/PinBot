# PinBot
This is a Python 3 bot which allows anyone to pin messages in Discord (using discordpy)

## Reason
In Discord, the ability to pin messages is such that when a message is pinned,
you can easily access that message by selecting "view pinned messages" at the top
of the channel options, which allows you to see important messages from even years
ago! However, the problem with this particular permission is that giving this 
permission to a user also gives them the permission to manage messages, including
the ability to delete other users' messages. This is a cause of concern in groupchats
which are meant to be professional or any open Discords where it's not desirable
to have everyone have permission to moderate messages.

So the way this bot works is it checks whenever the :pushpin: emoji is added
(📌) and accordingly pins the message if it hasn't been pinned already. Similarly, if the reaction
is removed and no one has reacted to that message, the bot unpins the message.
Currently hosted on Heroku 24/7, can be also hosted locally but you'd have to 
change the Discord token to that of your local bot. No other big requirements.
