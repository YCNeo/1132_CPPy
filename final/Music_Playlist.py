if __name__ == "__main__":
    n = int(input())
    songs = []

    for _ in range(n):
        song_str = input().strip().split(" ")
        songs.append([song_str[0], song_str[1], int(song_str[2])])

    filter = input().strip().split(",")
    duration = int(input())

    play_list = []
    for s in songs:
        if s[1] in filter:
            play_list.append(s)

    if len(play_list) != 0:
        playing = ""
        elapsed = 0
        total = 0
        i = 0
        while True:
            if duration > play_list[i][2]:
                duration -= play_list[i][2]
                if i == len(play_list) - 1:
                    i = 0
                    continue
            elif duration == play_list[i][2]:
                playing = play_list[i][0]
                elapsed = play_list[i][2]
                total = play_list[i][2]
                break
            elif duration < play_list[i][2]:
                playing = play_list[i][0]
                elapsed = duration
                total = play_list[i][2]
                break

            i += 1

        print(f"Now playing: {playing} ({elapsed}/{total})")
    else:
        print("(No song is playing)")
