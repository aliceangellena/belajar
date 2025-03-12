def WinStreak(poin_player, win_streak, poin_ws):
    
    if win_streak <= 1:
        print("bukan win streak")
    else:
        for i in range(win_streak):
            poin_player = poin_player + poin_ws
            poin_ws = poin_ws + 100
        print(f"saya punya poin: {poin_player}")
        
WinStreak(0,1,100)
WinStreak(100,3,100)
WinStreak(1000,0,300)
WinStreak(100,7,300)