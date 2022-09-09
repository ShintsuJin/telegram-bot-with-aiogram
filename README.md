# Telegram bot using aiogram library
+ ### Description:
    Suppose you have a duty calendar and people need to know who is on duty today.An example of such a calendar is offered in the "operators" module, the calendar is written as a dictionary, where the key is the day of the month, and the value is information about the person on duty.
    Next, in the "handlers" module, we define a variable so that the code understands what day of the month it is, then we run through our calendar and find the key that is equal to our variable and return the value of this key, namely information about who is on duty today.
    Next, the bot logic is written using the aiogram library so that the bot responds asynchronously. The bot can be added to the chat, or you can write to him personally so that he provides the necessary information. Btw you can screw the buttons as desired in module "buttons".
    The bot is launched via the 'main' module.