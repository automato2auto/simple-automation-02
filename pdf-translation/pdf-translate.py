import fitz
import translators as ts
import sys

doc = fitz.open('مسار_ملف_البي_دي_اف.pdf')

for page in doc:

    text_to_translate = page.get_text('text')

    with open(f'translated_text.txt', 'a', encoding='utf-8') as f:

        sys.stdout = f

        translated_text = ts.translate_text(query_text=text_to_translate,
                                            translator='google', from_language='en', to_language='ar')

        print(translated_text)
