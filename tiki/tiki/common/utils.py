from pathlib import Path


def get_product_id(tiki_product_url: str) -> str:
    id = tiki_product_url.split('.html')[0].split('-')[-1][1:]
    return id


def get_variant_infos(variants):
    required_variant_infos = []
    for variant in variants:
        required_variant_infos.append({
            'variant_title': variant['name'],
            'variant_price': variant['price'],
            'variant_url': variant['images'][0]['medium_url']
        })
    return required_variant_infos


def get_image_urls(images):
    image_urls = []
    for image in images:
        image_urls.append(image['medium_url'])
    return image_urls


def get_image_infos(image_urls):
    images = []
    for url in image_urls:
        filename = Path(url).name
        images.append({
            'image_url': url,
            'image_name': filename
        })
    return images
