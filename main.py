from youtube_dl import YoutubeDL


def start():
    audio_downloader: YoutubeDL = YoutubeDL({'format': 'bestaudio'})

    try:
        print('Youtube Downloader'.center(40, '_'))
        URL = input('Enter youtube url:  ')
        audio_downloader.extract_info(URL)
    except Exception as e:
        print('Couldn\'t download the audio')

    finally:
        print('see you next time')

    option = int(input('\n1. Download again \n2. Exit\n\nEnter you selection:'))

    if option != 1:
        print('enjoy your audio!')
        exit()


if __name__ == '__main__':
    start()
