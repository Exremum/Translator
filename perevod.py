from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    print("Добро пожаловать в переводчик!")
    while True:
        print("Выберите направление перевода:")
        print("1. Английский -> Русский")
        print("2. Русский -> Английский")
        print("3. Выход")

        choice = input("Введите номер выбора: ")

        if choice == '1':
            text = input("Введите текст на английском: ")
            translated = translate_text(text, 'en', 'ru')
            print(f"Перевод на русский: {translated}")
        elif choice == '2':
            text = input("Введите текст на русском: ")
            translated = translate_text(text, 'ru', 'en')
            print(f"Перевод на английский: {translated}")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
