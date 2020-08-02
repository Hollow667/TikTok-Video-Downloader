import os
import random
import requests

os.system('cls && title [TikTok Video Downloader]')
downloaded = 0
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

if not os.path.exists('Downloaded'):
    os.makedirs('Downloaded')

while True:
    video_url = input('> TikTok Video URL: ')

    try:
        response = requests.get(video_url, headers=HEADERS).text
    except Exception as e:
        print(f'Error: {e}')
    else:
        try:
            download_url = response.split('urls":["')[1].split('"]')[0]
        except IndexError:
            print(
                'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/vide'
                'o/1234567891234567891'
            )
        else:
            name = (
                '{}{}.mp4'.format(
                    response.split('pageUrl":"/@')[1].split('/video')[0],
                    ''.join(random.choice('0123456789') for _ in range(6))
                )
            )  # For readability purposes avoiding an f-string here.
            video = requests.get(download_url)

            if (status := video.status_code) == 200:
                with open(f'Downloaded/{name}', 'wb') as f:
                    f.write(video.content)

                print(f'Successfully downloaded: .\\Downloaded\\{name}')
                downloaded += 1
                os.system(f'title [TikTok Video Downloader] - Downloaded: {downloaded}')
            else:
                print(f'Error: {video.text} | Status Code: {status}')

    print()
