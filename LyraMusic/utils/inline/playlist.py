
# Copyright (C) 2022-2023 by NitricXd@Github, < https://github.com/NitricXd >.
#
# This file is part of < https://github.com/NitricXd/LyraMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/NitricXd/LyraMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_1"],
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text=_["PL_B_8"], callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            )
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_9"], 
                url=f"https://t.me/SquadGoalsss", 
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_10"], 
                url=f"https://t.me/gifsgalleryy", 
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_11"], 
                url=f"https://t.me/raamsiiya", 
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"], callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text=_["P_B_2"], callback_data="play_playlist b"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="home_play"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_9"], 
                url=f"https://t.me/SquadGoalsss", 
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_10"], url=f"https://t.me/gifsgalleryy"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_11"], url=f"https://t.me/raamsiiya"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["PL_B_7"],
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
