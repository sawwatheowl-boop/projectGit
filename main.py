liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}

def add_3_songs(dic):
    for i in range(3):
        song = input("Enter the song that you want: ")
        if song not in dic:
            i += 1
            print("Already in playlist!")
        else:
            artist = input("Enter the singer: ")
            set_d = set()
            minutes = int(input("Enter min of the song: "))
            set_d.add(minutes)
            sec = int(input("Enter min of the song: "))
            set_d.add(sec)
            genre = input("Enter the genre: ")
            dic[song] = {"artist": artist, "duration": set_d, "genre": genre}

    print(dic)

def del_song(dic):
    song = input("Enter the song that you want to check: ")
    if song in dic:
        print("Do you want to delete")
        del dic[song]
    else:
        print("This song is not in playlist!")

def main():
    pass

main()