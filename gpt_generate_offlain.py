from gpt4all import GPT4All

gpt = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
gpt.open()

def generate_description_offlain(raw_description, product_title, brand, type_marker='DF'):
    prompt = (
        """Ты SEO-копирайтер. На основе чернового описания товара с сайта конкурентов 
        нужно сгенерировать уникальное, структурированное описание по следующим правилам Figma:\n
        - Заголовки только h3, шрифт 13, выравнивание по ширине\n
        - Разделы: Назначение, Состав, Характеристики, Преимущества (если есть)\n
        - Удалить знаки: ®, ™, °, ×, ±, ≤, ≥ и т. п. Заменить ‘ ’ и “ ” на « »\n
        - H1: «{title}, {brand}»\n
        - H2: короткий слоган\n
        - Description: «Товар от производителя {brand} – это ...» (полужирный, со ссылкой на бренд)\n
        - Комплектация: {title} ({type_marker}-формат — точка или нет)\n
        - Используй маркированные списки и выравнивание по ширине
        Черновик: {description}

        Уникальное описание:"""
    ).format(title=product_title, description=raw_description, brand=brand, type_marker="10 мл." if type_marker == "RS" else "10 мл")
    
    output = gpt.prompt(prompt, max_token=800, temp=0.7)