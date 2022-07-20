from icrawler.builtin import GoogleImageCrawler

name = input('По какому ключу хотите искать изображения? ')
max_num = int(input('Введите количество изображений для скачивания: '))


def google_img_downloader():
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})

    filters = dict(
        type='photo',
        size='large')

    crawler.crawl(keyword=name,
                  max_num=max_num,
                  overwrite=True,
                  filters=filters)


def main():
    google_img_downloader()


if __name__ == '__main__':
    main()
