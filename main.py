from automations.clear_previous_data import clear_previous_data
from automations.scrape_embed_url import scrape_embed_url
from automations.scrape_song_name import scrape_song_name
from automations.create_songs import create_songs

def main():
    artist = "Tame Impala"
    album = "The Slow Rush"
    total_songs = 12
    press_count = 1

    clear_previous_data()
    scrape_song_name(album, artist, total_songs)
    scrape_embed_url(album, artist, total_songs, press_count)
    create_songs(artist, album, total_songs)

if __name__ == "__main__":
    main()