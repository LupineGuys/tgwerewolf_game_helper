import re
import time
import patterns
from pyrogram import Client, Filters

# application register
app_id = 12345  # get app id in my.telegram.com
app_hash = '12ab34cd56ef78gh9j'  # get app hash in my.telegram.com
app = Client("helper", api_id=app_id, api_hash=app_hash)

# let it True if you want to confirm games with TSWW
confirm_game = True
# let it True if you want to start new game after every game finished
start_new_game = True
# game start with this mode; normal mode is 1 and chaos mode is 2
start_mode = 2
# first game list command for role saver; if you do not need it, let it empty
role_saver_first_game_list = '/new@TsWwPlus_Bot'
# other game list command for role saver; if you do not need it, let it empty
role_saver_other_Game_list = '/tsup@TsWwPlus_Bot'
# let it True if you want to pin #players
pin_players = True
# let it True if you want to use /fillit TSWW option
fill_it = True
# after game started send this message; if you do not need it, let it empty
started_game = "#next"
# after game canceled send this message; if you do not need it, let it empty
canceled_game = ''


@app.on_message(Filters.user([175844556, 198626752]) & Filters.text & ~Filters.reply & ~Filters.edited)
def main_works(client, message):
    msg_id = message.message_id
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # last game list
    if re.search(patterns.game_finish, text):
        if confirm_game:
            client.send_message(
                chat_id=message.chat.id,
                text="/confirm@TsWwPlus_Bot",
                reply_to_message_id=msg_id
            )
            time.sleep(1)
        if start_new_game:
            if start_mode == 1:
                start_mode_text = '/startgame'
            elif start_mode == 2:
                start_mode_text = '/startchaos'
            else:
                start_mode_text = '/startchaos'

            if user_id == 175844556:
                client.send_message(
                    chat_id=message.chat.id,
                    text=start_mode_text + "@werewolfbot"
                )
            elif user_id == 198626752:
                client.send_message(
                    chat_id=message.chat.id,
                    text=start_mode_text + "@werewolfbetabot "
                )

    # first game list
    elif not re.search(patterns.death, text) and re.search(patterns.game_list, text):
        if role_saver_first_game_list:
            client.send_message(
                chat_id=message.chat.id,
                text=role_saver_first_game_list,
                reply_to_message_id=msg_id
            )

    # other game list
    elif re.search(patterns.game_list, text):
        if role_saver_other_Game_list and role_saver_first_game_list:
            client.send_message(
                chat_id=message.chat.id,
                text=role_saver_other_Game_list,
                reply_to_message_id=msg_id
            )

    # start join time message
    elif text.find('#players') != -1:
        if pin_players:
            client.send_message(
                chat_id=message.chat.id,
                text="/pinn@ExecutrixBot",
                reply_to_message_id=msg_id
            )
        if fill_it:
            time.sleep(4)
            client.send_message(
                chat_id=message.chat.id,
                text="/fillit@TsWwPlus_Bot",
                reply_to_message_id=msg_id
            )

    # game started message
    elif re.search(patterns.game_started, text):
        if started_game:
            client.send_message(
                chat_id=message.chat.id,
                text=started_game)

    # game canceled message
    elif re.search(patterns.game_canceled, text):
        if canceled_game:
            client.send_message(
                chat_id=message.chat.id,
                text=canceled_game,
            )


@app.on_message(Filters.user(491459293) & Filters.reply)
def pin_game_started_message_response(client, message):
    chat_id = message.chat.id
    msg_id = message.message_id
    message_inf = message
    if message_inf.reply_to_message.text:
        if message_inf.reply_to_message.from_user.id == app.get_me().id:
            if message_inf.reply_to_message.text == started_game:
                time.sleep(4)
                client.send_message(
                    chat_id=message.chat.id,
                    text="/pin@ExecutrixBot",
                    reply_to_message_id=msg_id
                )


# run application
app.run()
