from automations.create_songs import create_songs
from automations.scrape_embed_url import scrape_embed_url
from automations.scrape_song_name import scrape_song_name

def main():
    artist = "Bring Me The Horizon"
    album = "POST HUMAN: NeX GEn"
    total_songs = 16
    press_count = 1

    scrape_song_name(album, total_songs)
    scrape_embed_url(album, total_songs, press_count)
    create_songs(artist, album)

if __name__ == "__main__":
    main()