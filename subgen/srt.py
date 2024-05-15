def read_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    subtitles = []
    timings = []
    subtitle = None
    for line in lines:
        line = line.strip()
        if not line:
            if subtitle:
                subtitles.append(subtitle['text'])
                timings.append(subtitle['timing'])
                subtitle = None
        elif subtitle is None:
            subtitle = {'text': '', 'timing' : ''}
        elif ' --> ' in line:
            if subtitle:
                subtitle['timing'] = line
            else:
                subtitle = {'timing': line}
            # pass  # Skip time information
        else:
            subtitle['text'] += ' ' + line

    if subtitle:
        subtitles.append(subtitle['text'])
        timings.append(subtitle['timing'])

    return subtitles , timings


# Example usage
 # Change this to your .srt file path


# for subtitle in subtitles:
#     print(f"{subtitle}")

def send_subtitle(file_path):

    subtitles, timing = read_srt(file_path)

    return subtitles[:300] , timing[:300]
