violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
for song in violator_songs:
    print(song)

semen_choice = input("Enter numbers of tracks via (space): ")
semen_list = semen_choice.split()
time = 0
for i, song in enumerate(violator_songs):
    if str(i + 1) in semen_list:
        semen_list.append(str(song))
        semen_list.remove(str(i + 1))
        for index, timing in enumerate(song):
            if index == 1:
                time += timing


for song in semen_list:
    print(song)
print(time)



