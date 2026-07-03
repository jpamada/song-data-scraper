import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.8

def add_input(artist, album, total_songs):
    created_songs = 0
    skipped_songs = 0

    with open("data/song_names.txt") as song_file, open("data/embed_urls.txt") as embed_file:
        for song, embed in zip(song_file, embed_file):
            song = song.strip()
            embed = embed.strip()

            time.sleep(1)
            add_song_btn = pyautogui.locateCenterOnScreen(
                "assets/personal/add_new_song_btn.png",
                confidence=0.75
            )
            pyautogui.click(add_song_btn)

            song_name_label = pyautogui.locateCenterOnScreen(
                "assets/personal/song_name_label.png",
                confidence=0.75,
            )
            pyautogui.moveTo(song_name_label)
            pyautogui.move(0,40)
            pyautogui.click()
            pyperclip.copy(song)
            pyautogui.hotkey("ctrl", "v")
            
            artist_label = pyautogui.locateCenterOnScreen(
                "assets/personal/artist_label.png",
                confidence=0.75
            )
            pyautogui.moveTo(artist_label)
            pyautogui.move(0,40)
            pyautogui.click()
            pyautogui.write(artist)
            time.sleep(0.5)
            pyautogui.move(0, 60)
            pyautogui.click()

            album_label = pyautogui.locateCenterOnScreen(
                "assets/personal/album_label.png",
                confidence=0.75,
                region=(0,300, 500, 500)
            )
            pyautogui.moveTo(album_label)
            pyautogui.move(0,40)
            pyautogui.click()
            pyautogui.write(album)
            time.sleep(0.5)
            pyautogui.move(0, 60)
            pyautogui.click()

            spotify_url_label = pyautogui.locateCenterOnScreen(
                "assets/personal/spotify_url_label.png",
                confidence=0.75
            )
            pyautogui.moveTo(spotify_url_label)
            pyautogui.move(0,40)
            pyautogui.click()
            pyautogui.write(embed)

            add_song_btn = pyautogui.locateCenterOnScreen(
                "assets/personal/add_song_btn.png",
                confidence=0.75
            )
            pyautogui.click(add_song_btn)
            time.sleep(0.5)

            try:
                duplicate_error = pyautogui.locateCenterOnScreen(
                    "assets/personal/duplicate_error.png",
                    confidence=0.75
                )
            except pyautogui.ImageNotFoundException:
                duplicate_error = None

            if duplicate_error:
                back_btn = pyautogui.locateCenterOnScreen(
                    "assets/personal/back_btn.png",
                    confidence=0.75
                )
                pyautogui.click(back_btn)
                skipped_songs += 1
            else:
                created_songs += 1

            print(f"Processing: {created_songs}/{total_songs} created, skipped {skipped_songs}")


    pyautogui.hotkey("alt", "tab")
    print("Completed: Created Songs.")
        
def create_songs(artist, album, total_songs):
    print("Starting to add new songs...")
    pyautogui.hotkey("ctrl", "1")
    add_input(artist, album, total_songs)