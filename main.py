from icrawler.builtin import GoogleImageCrawler

name = input('По какому ключу хотите искать изображения? ')
max_num = int(input('Введите количество изображений для скачивания: '))
rewrite = input('Перезаписать ранее найденные фото? \n Введите да или нет: ')


while rewrite != 'да' or 'нет' or 'Да' or 'Нет':
    print('Ошибка. Введите нужное значение')
    rewrite = input(
        'Перезаписать ранее найденные фото? \n Введите да или нет: ')
    if rewrite == 'да' or 'Да':
        rewrite = True
        break
    if rewrite == 'нет' or 'Нет':
        rewrite = False
        break


def google_img_downloader():
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})

    filters = dict(
        type='photo',
        size='large')

    crawler.crawl(keyword=name,
                  max_num=max_num,
                  overwrite=rewrite,
                  filters=filters)


def main():
    google_img_downloader()


if __name__ == '__main__':
    main()
