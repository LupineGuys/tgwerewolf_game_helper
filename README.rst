# tgwerewolf_game_helper
game helper for `telegram Werewolf moderator <https://github.com/GreyWolfDev/Werewolf>`_

helper bot for `Lupine guys team <https://telegram.me/lupine_guys>`_


install pyrogram and re
.. code:: shell

    $ pip3 install pyrogram 

    $ pip3 install re
    
these commands are for Linux server. if you use Windows,  use ``pip`` instead of  ``pip3``
.. code:: shell

    $ pip install pyrogram 

    $ pip install re
    
    
edit bot settings according to your needs

.. code:: python
    
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


- ``confirm_game: ثبت امتیاز های بازی توسط بات تسک، برای خاموش کردن، به '' تغیرش دهید``
- ``start_new_game: شروع بازی فاصله بعد از پایان بازی، برای خاموش کردن، به '' تغیرش دهید``
- ``start_mode: نوع شروع بازی، برای بازی عادی 1 و برای بازی آشوب به 2 تغیرش دهید``
- ``role_saver_first_game_list: ثبت لیست اول بازی برای ثبت نقش، برای خاموش کردن به '' تغیرش دهید``
- ``role_saver_other_Game_list: اپدیت لیست بازی برای ثبت نقش، برای خاموش کردن به '' تغیرش دهید``
- ``pin_players:  سنجاق پیام شروع زمان ورود بازی (جوین تایم)، برای خاموش کردن، به '' تغیرش دهید``
- ``fill_it:  برای استفاده از قابلیت پر کردن بازی ربات تسک، برای خاموش کردن، به '' تغیرش دهید``
- ``started_game:  متن پیام ارسال، بعد از شروع بازی، برای خاموش کردن، به '' تغیرش دهید``
- ``canceled_game:  متن پیام ارسال، بعد از کنسل شدن بازی، برای روشن کردن، متن مورد نظر رو وارد کنید``
