
def generate_meta(title, brand):
    meta_title = f"{title} — купить с доставкой, {brand}"
    meta_description = f"Купить {title} {brand} с доставкой по РФ. Только сертифицированная продукция. Надежный поставщик Dental First."
    meta_keywords = f"{title.lower()}, {brand.lower()}, купить {title.lower()}, стоматологические материалы"

    return {
        "meta_title": meta_title,
        "meta_description": meta_description,
        "meta_keywords": meta_keywords,
    }