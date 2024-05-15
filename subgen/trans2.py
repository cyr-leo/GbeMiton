from subgen import srt
import time
from googletrans import Translator


# Enregistrer le temps de départ
start_time = time.time()

print('start translation')


def write_srt(file_path, subtitles, timings):
    with open(file_path, 'w', encoding='utf-8') as file:
        for idx, subtitle in enumerate(subtitles, start=1):
            file.write(str(idx) + '\n')
            file.write(timings[idx - 1] + '\n')
            file.write(subtitle + '\n\n')



# Enregistrer le temps d'arrêt
end_time = time.time()

# Calculer la durée d'exécution
execution_time = end_time - start_time

# Afficher le temps d'exécution
print("Le script a mis {:.2f} secondes pour s'exécuter.".format(execution_time))


def trans(src_file_path):
    translator = Translator()

    subtitles, timings = srt.send_subtitle(src_file_path)

    for subtitle in subtitles:
        print(f"{subtitle}")

    for timing in timings:
        print(timing)

    translator = Translator()
    translations = translator.translate(subtitles, dest='yo')

    for translation in translations:
        print(translation.origin, ' -> ', translation.text)

    output_file_path = src_file_path +  "yo_"   # Change this to your desired output file path
    write_srt(output_file_path, [translation.text for translation in translations], timings)






