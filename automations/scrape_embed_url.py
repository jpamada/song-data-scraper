import time
import pyautogui
import pyperclip

embed_urls = []
pyautogui.PAUSE = 0.8

def browse_spotify(album, press_count=1):
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("spotify.com")
    pyautogui.press("enter")
    time.sleep(3)

    search_bar = pyautogui.locateCenterOnScreen(
        "assets/spotify/search_bar.png",
        confidence=0.8
    )

    pyautogui.click(search_bar)
    pyautogui.write(f"{album} album")
    time.sleep(1)
    pyautogui.press("down", presses=press_count)
    pyautogui.press("enter")
    time.sleep(1)

def scroll(scroll_length):
    title_label = pyautogui.locateCenterOnScreen(
        "assets/spotify/title_label.png",
        confidence=0.8
    )
    pyautogui.moveTo(title_label)
    pyautogui.scroll(scroll_length)

    title_label = pyautogui.locateCenterOnScreen(
        "assets/spotify/title_label.png",
        confidence=0.8
    )
    pyautogui.click(title_label)

def copy_song_embed_url(
    total_songs, 
    copied_songs, 
    visible_songs = 8,
    x_position = 200, 
    y_position = 385,
    gap = 70
):
    song_to_copy = min(visible_songs, total_songs - copied_songs)
    for _ in range(song_to_copy):
        pyautogui.moveTo(x_position, y_position)
        pyautogui.rightClick()

        share_btn = pyautogui.locateCenterOnScreen(
            "assets/spotify/share_btn.png",
            confidence=0.8
        )
        pyautogui.click(share_btn)
        time.sleep(0.5)

        embed_btn = pyautogui.locateCenterOnScreen(
            "assets/spotify/embed_btn.png",
            confidence=0.8
        )
        pyautogui.click(embed_btn)
        time.sleep(0.5)

        copy_btn = pyautogui.locateCenterOnScreen(
            "assets/spotify/copy_btn.png",
            confidence=0.8
        )
        pyautogui.click(copy_btn)
        time.sleep(0.3)
        
        embed_urls.append(pyperclip.paste())
        pyautogui.press("esc")
        copied_songs += 1
        y_position += gap
        print(f"Processing: {copied_songs}/{total_songs} left...")

    return copied_songs

def scrape_embed_url(album, total_songs, press_count):
    copied_songs = 0
    print("Starting to scrape song embed url...")
    browse_spotify(album, press_count)
    scroll(-395)

    while copied_songs != total_songs:
        copied_songs = copy_song_embed_url(total_songs, copied_songs)

        if copied_songs < total_songs:
            scroll(-545)

    if copied_songs == total_songs:
        with open("data/embed_urls.txt", "w", encoding="utf-8") as file:
            for url in embed_urls:
                file.write(url.split("track/")[1].split("?")[0] + "\n")
    
    print("Completed: All Spotify embed URLs are copied.")