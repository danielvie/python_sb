from pytube import Playlist

def main():
    link = 'https://www.youtube.com/playlist?list=PLC3y8-rFHvwgC9mj0qv972IO5DmD-H0ZH'

    p = Playlist(link)

    print(p.title)

    # for url in p.video_urls:
    #     print(url)

    for video in p.videos:
        print(f'Downloading {video.title}')
        # video.streams.get_highest_resolution().download(r'downloads')
        
if __name__ == "__main__":
    
    main()
