from openai import OpenAI


client = OpenAI(api_key="")

def generate_description_onlain(raw_description, product_title, brand, type_marker='DF'):
    system_prompt = (
        "Ты SEO-копирайтер. На основе чернового описания товара с сайта конкурентов "
        "нужно сгенерировать уникальное, структурированное описание по следующим правилам Figma:\n"
        "- Заголовки только h3, шрифт 13, выравнивание по ширине\n"
        "- Разделы: Назначение, Состав, Характеристики, Преимущества (если есть)\n"
        "- Удалить знаки: ®, ™, °, ×, ±, ≤, ≥ и т. п. Заменить ‘ ’ и “ ” на « »\n"
        "- H1: «{title}, {brand}»\n"
        "- H2: короткий слоган\n"
        "- Description: «Товар от производителя {brand} – это ...» (полужирный, со ссылкой на бренд)\n"
        "- Комплектация: {title} ({type_marker}-формат — точка или нет)\n"
        "- Используй маркированные списки и выравнивание по ширине"
    ).format(title=product_title, brand=brand, type_marker="10 мл." if type_marker == "RS" else "10 мл")
    
    response = client.chat.completions.create(
        model='omni-moderation-latest',
        messages=[
            {'role':'system', 'content': system_prompt},
            {'role':'user', 'content': raw_description},
            ],
        stream=True,

    )
    # print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()

