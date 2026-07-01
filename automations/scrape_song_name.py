import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.8
songs = []

def browse_music(album):
    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("music.youtube.com")
    pyautogui.press("enter")
    time.sleep(2)

    search_bar = pyautogui.locateCenterOnScreen(
        "assets/music/search_bar.png",
        confidence=0.8
    )
    pyautogui.click(search_bar)
    pyautogui.write(f"{album} album")
    pyautogui.press("enter")

    time.sleep(2)
    pyautogui.move(50, 250)
    pyautogui.click()
    time.sleep(1)
    pyautogui.scroll(-60)

def copy_song_name(total_songs, copied_songs, visible_songs=8):
    pyautogui.click(clicks=3)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)

    songs.append(pyperclip.paste())
    copied_songs += 1
    print(f"Processing: {copied_songs}/{total_songs} left...")

    if copied_songs < total_songs:
        if copied_songs < visible_songs:
            pyautogui.move(0, 95)
        else:
            pyautogui.scroll(-90)
            time.sleep(0.3)

    return copied_songs

def scrape_song_name(album, total_songs):
    copied_songs = 0
    print("Starting to scrape song name...")
    browse_music(album)
    pyautogui.moveTo(905, 270)

    while copied_songs < total_songs:
        copied_songs = copy_song_name(total_songs, copied_songs)

    with open("data/song_names.txt", "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song.strip() + "\n")

    print("Completed: YouTube Music Song Names Copied.")