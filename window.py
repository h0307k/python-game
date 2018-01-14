# -*- coding:utf-8 -*-
"""
ウィンドウ（画面）の表示
"""
__author__  = "kudo"
__version__ = "1.00"
__date__    = "2018/01/14"

import pygame
from pygame.locals import *
import sys

# 画面縦
SCREEN_LENGTH = 400

# 画面横
SCREEN_WIDTH = 300

# 画面名
SCREEN_NAME = "Test"

# 画面色:赤
RGB_R = 0

# 画面色:緑
RGB_G = 0

# 画面色:青
RGB_B = 0


def resize_screen(length,width):
    """
    指定の画面サイズに変更する
    :param  length  画面縦サイズ
    :param  width   画面横サイズ
    :return:
    """
    return pygame.display.set_mode((length, width))


def main():
    """
    ウィンドウを表示する関数
    :return:
    """
    pygame.init()                                         # 初期化
    screen = resize_screen(SCREEN_LENGTH, SCREEN_WIDTH)   # 大きさ400*300の画面を生成
    pygame.display.set_caption(SCREEN_NAME)               # タイトルバーに表示する文字

    while (1):
        screen.fill((RGB_R, RGB_G, RGB_B))  # 画面を黒色(#000000)に塗りつぶし
        pygame.display.update()             # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # 終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()