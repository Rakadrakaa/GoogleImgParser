from icrawler.builtin import GoogleImageCrawler

name = input('По какому ключу хотите искать изображения? ')
max_num = int(input('Введите количество изображений для скачивания: '))
rewrite = input('Перезаписать ранее найденные фото? \n Введите да или нет: ')

if rewrite == 'Да' or 'да':
    rewrite = True
elif rewrite == 'Нет' or 'нет':
    rewrite = False
else:
    print('Ошибка, файлы не будут перезаписаны. ')
    rewrite = False


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
