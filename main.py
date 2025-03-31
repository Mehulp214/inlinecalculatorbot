# import telebot
# from telebot import types
# bot = telebot.TeleBot("7335432995:AAENNEGS3lokRPEsP3RYpxkHIQjzv5tjwY0")
# bot.delete_webhook()

# # Rest of your code...
# # Define the '/start' command


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     user_id = message.from_user.id
#     if user_id not in user_list:
#         user_list.append(user_id)
#         bot.send_message(owner_chat_id, f"<b>New user \n username -:{message.chat.first_name}\n User ID -:</b><code> {message.chat.id}</code>",parse_mode="HTML")
#         print(user_list)
#     # if message.message_id - 1:
#     #    bot.delete_message(chat_id=message.chat.id,message_id=message.message_id - 1)
#     keyboard = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton(
#         'Open Calculator', callback_data='/calc')
#     keyboard.add(button1)
#     first_name = message.from_user.first_name
#     bot.reply_to(message, f"<b>{first_name}, Welcome to my bot!, Please Support Us - @ || @</b>",
#                  parse_mode="HTML", reply_markup=keyboard)
#     # bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

# # Helper function to create the calculator inline keyboard markup


# def create_calculator():
#     markup = types.InlineKeyboardMarkup(row_width=4)
#     markup.add(types.InlineKeyboardButton("7️⃣", callback_data="7"),
#                types.InlineKeyboardButton("8️⃣", callback_data="8"),
#                types.InlineKeyboardButton("9️⃣", callback_data="9"),
#                types.InlineKeyboardButton("➕", callback_data="+"),
#                types.InlineKeyboardButton("4️⃣", callback_data="4"),
#                types.InlineKeyboardButton("5️⃣", callback_data="5"),
#                types.InlineKeyboardButton("6️⃣", callback_data="6"),
#                types.InlineKeyboardButton("➖", callback_data="-"),
#                types.InlineKeyboardButton("1️⃣", callback_data="1"),
#                types.InlineKeyboardButton("2️⃣", callback_data="2"),
#                types.InlineKeyboardButton("3️⃣", callback_data="3"),
#                types.InlineKeyboardButton("✖", callback_data="*"),
#                types.InlineKeyboardButton("•", callback_data="."),
#                types.InlineKeyboardButton("0️⃣", callback_data="0"),
#                types.InlineKeyboardButton("🟰", callback_data="="),
#                types.InlineKeyboardButton("➗", callback_data="/"),
#                types.InlineKeyboardButton("❎ Clear", callback_data="C"),
#                types.InlineKeyboardButton("❌ Off Calulator", callback_data="off"),
#                types.InlineKeyboardButton("⬅️ Cut", callback_data="cut"))

#     return markup

# # Define the callback query handler for all callback queries
# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback(call):
#     if call.data == '/calc':
#         markup = create_calculator()
#         bot.edit_message_text(chat_id=call.message.chat.id,
#                               message_id=call.message.message_id,
#                               text="<b>Use the Calculator below: </b>", reply_markup=markup, parse_mode="HTML")
#         bot.current_expression = ""
#     else:
#         if hasattr(bot, "current_expression"): # check if the bot has the current_expression attribute
#             expression = bot.current_expression
#         else:
#             expression = ""
#         if call.data in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/"]:
#             expression += call.data
#             bot.current_expression = expression
#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.message_id,
#                                   text="<b>Choose Value:</b> {}".format(expression), reply_markup=create_calculator(), parse_mode="HTML")
#             bot.answer_callback_query(
#                 call.id, text="Current value: {}".format(expression))
#         elif call.data == "=":
#             try:
#                 result = eval(expression)
#             except:
#                 result = "Error"
#             bot.current_expression = str(result)
#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.message_id,
#                                   text="Result: {}".format(result), parse_mode="HTML", reply_markup=create_calculator())
#             bot.answer_callback_query(
#                 call.id, text="Result: {}".format(result))
#         elif call.data == "C":
#             bot.current_expression = ""
#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.message_id, parse_mode="HTML",
#                                   text="<b>Choose Value: </b>", reply_markup=create_calculator())
#             bot.answer_callback_query(call.id, text="History cleared.")
#         elif call.data == "cut":
#             expression = bot.current_expression
#             if len(expression) > 0:
#                 expression = expression[:-1]  # cut the last character
#                 bot.current_expression = expression
#                 bot.edit_message_text(chat_id=call.message.chat.id,
#                           message_id=call.message.message_id,text="<b>Choose Value:</b> {}".format(expression), reply_markup=create_calculator(), parse_mode="HTML")
#                 bot.answer_callback_query(call.id, text="Current value: {}".format(expression))

#         elif call.data == "off":
#             keyboard = types.InlineKeyboardMarkup()
#             button1 = types.InlineKeyboardButton(
#                 'Open Calculator', callback_data='/calc')
#             keyboard.add(button1)
#             first_name = call.message.from_user.first_name
#             text = f"<b>{first_name}, Welcome to my bot!, Please  Support Us - @KaranCoder || @TGBotsCode</b>"
#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.message_id, parse_mode="HTML",
#                                   text=text, reply_markup=keyboard)
# owner_chat_id = "5337150824"
# user_list = []
# # Define the message handler for all other text messages
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     try:
#         if message.message_id is not None and message.message_id != 0:
#                 bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)

#         keyboard = types.InlineKeyboardMarkup()
#         button1 = types.InlineKeyboardButton(
#         'Open Calculator', callback_data='/calc')
#         keyboard.add(button1)
#         first_name = message.from_user.first_name
#         bot.reply_to(message, f"<b>{first_name}, Welcome to my bot!, Please Support Us - @KaranCoder || @TGBotsCode</b>",
#                  parse_mode="HTML", reply_markup=keyboard)
#         if message.message_id:
#             bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
#     except:
#         bot.reply_to(message, "<b>Please contact @kswami9 for a error</b>",parse_mode="HTML")



# # Start the bot
# bot.polling(non_stop=True)

from pyrogram.types import Client, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import CallbackQuery
import logging

logging.basicConfig(level=logging.INFO)

# Replace with your bot's token
API_ID = "13216322"
API_HASH = "15e5e632a8a0e52251ac8c3ccbe462c7"
BOT_TOKEN = "7335432995:AAENNEGS3lokRPEsP3RYpxkHIQjzv5tjwY0"

app = Client("calculator_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# A dictionary to store user-specific data (like current expression)
user_data = {}

# Helper function to create the calculator layout
def create_calculator():
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("7", callback_data="7"), InlineKeyboardButton("8", callback_data="8"), InlineKeyboardButton("9", callback_data="9"), InlineKeyboardButton("➕", callback_data="+")],
        [InlineKeyboardButton("4", callback_data="4"), InlineKeyboardButton("5", callback_data="5"), InlineKeyboardButton("6", callback_data="6"), InlineKeyboardButton("➖", callback_data="-")],
        [InlineKeyboardButton("1", callback_data="1"), InlineKeyboardButton("2", callback_data="2"), InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("✖", callback_data="*")],
        [InlineKeyboardButton("•", callback_data="."), InlineKeyboardButton("0", callback_data="0"), InlineKeyboardButton("🟰", callback_data="="), InlineKeyboardButton("➗", callback_data="/")],
        [InlineKeyboardButton("❎ Clear", callback_data="C"), InlineKeyboardButton("❌ Off", callback_data="off")]
    ])
    return markup

@app.on_message()
def handle_start(client, message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = ""  # Initialize an empty expression for the user

    markup = create_calculator()
    first_name = message.from_user.first_name
    app.send_message(
        chat_id=message.chat.id,
        text=f"<b>{first_name}, Welcome to the Calculator Bot!</b>\n\nUse the calculator below:",
        parse_mode="HTML",
        reply_markup=markup
    )

@app.on_callback_query()
def handle_callback(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    current_expression = user_data.get(user_id, "")

    if callback_query.data == "off":
        app.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Calculator turned off.",
            reply_markup=None
        )
    elif callback_query.data == "C":
        user_data[user_id] = ""
        app.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Choose Value: ",
            reply_markup=create_calculator()
        )
    elif callback_query.data == "=":
        try:
            result = eval(current_expression)
            user_data[user_id] = str(result)
            app.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=f"Result: {result}",
                reply_markup=create_calculator()
            )
        except Exception as e:
            app.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text="Error in calculation!",
                reply_markup=create_calculator()
            )
    else:
        user_data[user_id] = current_expression + callback_query.data
        app.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=f"Choose Value: {user_data[user_id]}",
            reply_markup=create_calculator()
        )

    app.answer_callback_query(callback_query.id)

if __name__ == "__main__":
    app.run()
