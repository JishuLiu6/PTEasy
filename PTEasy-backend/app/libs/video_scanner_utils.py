import re

data = """
Greta 2018 1080p NOR Blu-ray AVC DTS-HD MA 5.1-CultFilms™
"""

# 分割示范数据，每行表示一个视频
video_data = data.strip().split("\n")

# 定义用于提取视频信息的正则表达式
# title_pattern = re.compile(r"(?P<title>[\w\s]+)")
# (S\d{1,2}E\d{1,2})|(\d{4})'
# title_pattern = re.compile(r"(?P<title>.+?) [(?=\d{4}) | (S\d{1,2})]")
title_pattern = re.compile(r"(?P<title>.+?)(?:\s(?:S\d{1,2})|(?:\d{4}))")
year_pattern = re.compile(r"(?P<year>19[1-9]\d|2\d{3})")
season_pattern = re.compile(r"S(?P<season>\d{1,2})")
episode_pattern = re.compile(
    r"((E(?P<start_episode>\d{1,3})(?:-(?:E)?(?P<end_episode>\d{1,3}))?))")
# resolution_pattern = re.compile(r"(?P<resolution>\d{3,4}[ip])")
resolution_pattern = re.compile(r"(?P<resolution>\d{3,4}[ip])", re.IGNORECASE)

source_pattern = re.compile(r"(?P<source>(?:web-dl|hdtv|bluray|uhd|web|blu-ray|bdrip))", re.IGNORECASE)

codec_pattern = re.compile(r"(?P<codec>h\.?264|h\.?265|x264|x265|avc|vc1|vp9|vp8|xvid|divx|wmv|hevc|hvec|hvc)", re.IGNORECASE)
audio_pattern = re.compile(r"(?P<audio>ddp[a-z]*\s*[\d.]+|mp2|aac|flac[\d.]?|pcm|prores|dd 2audios|dd\s*[\d.]+|ddp|dts(?:-hd)?(?:\s*ma)?\s*[\d.]+|dts|truehd|ac3[\d.]+|ac3|opus|vorbis|wma|dolby)", re.IGNORECASE)

# release_group_pattern = re.compile(r'(?:[-@])(?P<release_group>[A-Za-z0-9]+)$')
release_group_pattern = re.compile(r'(?:[-@]\s*)(?P<release_group>[A-Za-z0-9]+)\s*$')
# release_group_pattern = re.compile(r'(?:[-@]\s*)(?P<release_group>[\w\u4e00-\u9fa5]+)\s*$')




# 遍历每行数据，提取视频信息
for video in video_data:
    title = title_pattern.search(video)
    year = year_pattern.search(video)
    season = season_pattern.search(video)
    episode = episode_pattern.search(video)
    resolution = resolution_pattern.search(video)
    source = source_pattern.search(video)
    codec = codec_pattern.search(video)
    audio = audio_pattern.search(video)
    release_group = re.search(release_group_pattern, video)

    # 输出视频信息
    print(f"Video: {video}")
    print(f"Title: {title.group('title') if title else 'N/A'}")

    print(f"Year: {year.group('year') if year else 'N/A'}")
    print(f"Season: {season.group('season') if season else '01'}")
    # print(episode)
    if episode:
        start_episode = episode.group('start_episode')
        end_episode = episode.group('end_episode')
        print(f"Episodes: {start_episode}{ '-'+end_episode if end_episode else ''}")
    # else:
    #     print("Episode: N/A")

    print(f"Resolution: {resolution.group('resolution') if resolution else 'N/A'}")
    print(f"Source: {source.group('source') if source else 'N/A'}")
    print(f"Video Codec: {codec.group('codec') if codec else 'N/A'}")
    print(f"Audio Codec: {audio.group('audio') if audio else 'N/A'}")
    print(f"Release Group: {release_group.group('release_group') if release_group else 'N/A'}")
    print("-" * 40)
