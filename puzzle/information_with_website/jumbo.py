import requests
from bs4 import BeautifulSoup as bs


def information_with_jumbo(url_website):
    url = url_website

    # creating request objects
    html = requests.get(url).content
    data = bs(html, 'html.parser')

    # find name
    name = data.find('article', attrs={'class': 'single-product'}).find('header').find('h1')
    name = name.get_text()

    # finding product-info
    parents = data.find('div', attrs={'class': "product-info"})

    # get description
    try:
        description = parents.find('div', attrs={'class': 'single-content'}).find_all('p')
        description_text = ''
        for i in description:
            description_text += i.get_text()
        description = description_text
        del description_text
    except AttributeError:
        print("This product doesn't have description")
        description = None

    # get number of pieces, article number, ean,
    product_information = parents.find('div', attrs={'class': 'single-details'}).find('ul').find_all('li')
    nop, an, ean = '', '', ''

    for line in product_information:
        line = line.get_text()
        if "Number of pieces:" in line:
            nop = line[len("Number of pieces:"):].replace(' ', '')
        elif "Article number:" in line:
            an = line[len("Article number:"):].replace(' ', '')
        elif "EAN code:" in line:
            ean = line[len("EAN code:"):].replace(' ', '')

    # get image

    all_images = data.find_all('img')
    corrent_image = []
    # `<img alt="" height="150" src="https://www.jumbo.eu/wp-content/uploads/2018/05/W`ASGIJ-150x150.png" width="150">
    for img in all_images:
        img = img.get('src')
        if an + '_1' in img:
            corrent_image.append(img)
    if corrent_image:
        image = corrent_image[0]
    else:
        image = None
    #Simple downolad image and add to media

    if image:
        from datetime import datetime
        name_image = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") +'.jpg'
        img_data = requests.get(image).content
        with open(f'media\\images\\{name_image}', 'wb') as hadler:
            hadler.write(img_data)
    payload = {
        'name': name,
        'number_of_pieces': nop,
        'ean_code': ean,
        'description': description,
        'company': "Jumbo",
        'product_code': an,
        'image': f'images/{name_image}' if image else image,
        'website': url_website
    }
    return payload
