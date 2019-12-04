from num2words import num2words
from transliterate import translit

age = 78
speech_time = 15
immigrate_years = 3
activity_years = 40
age_of_start = 8

numbers_in_speech = [
    age, speech_time, immigrate_years, activity_years, age_of_start]

original_speech = (
    "Ladies and gentlemen, I'm {0} years old and I finally got {1} minutes "
    "of fame once in a lifetime and I guess that this is mine. People have"
    " also told me to make these next few minutes escruciatingly embarrassing "
    "and to take vengeance of my enemies. Neither will happen. More than {2}"
    " years ago I moved to Novo-Novsk, but worked on new Magnetic Storage "
    "for last {3}. \nWhen I was {4}...\n".format(
        numbers_in_speech[0],
        numbers_in_speech[1],
        numbers_in_speech[2],
        numbers_in_speech[3],
        numbers_in_speech[4],
    )
)

transliterated_speech = translit(original_speech, 'ru')

print(transliterated_speech)

for number in numbers_in_speech:
    number_in_word = num2words(number)
    print('{0} - {1}'.format(number, translit(number_in_word, 'ru')))
