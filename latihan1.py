def winStreak(poin_player, win_streak, poin_ws):
    if win_streak == 1 or win_streak < 1:
        print("bukan win streak")
    elif win_streak > 1:
        while win_streak > 0:
            poin_player = poin_player + poin_ws
            poin_ws = poin_ws + 100
            win_streak -= 1
        print(f"saya punya poin: {poin_player}")

winStreak(0, 1, 100)
winStreak(1000, 3, 100)
winStreak(9876, 100, 350)
winStreak(500, 5, 1000)
winStreak(100, 7, 300)


