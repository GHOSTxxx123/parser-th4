from dental_first import get_descriptions
from gpt_generate_onlain import generate_description_onlain
from gpt_generate_offlain import generate_description_offlain
from google_sheet_writer import write_to_sheet
from meta_generator import generate_meta
import time


def main():
    start = time.time()

    # 1 Сбор всех описаний с Dental First
    print("Сбор всех описаний с Dental First.")
    start_1 = time.time()
    competitor_data = get_descriptions()
    print(f"Сбор всех описаний с Dental First. Завершено за {time.time() - start_1:.2f}сек")

    print("Генерация мета и Сбор строки для таблици.")
    start_2 = time.time()
    final_row = []
    for product in competitor_data:
        
        title = product['title']
        code_product = product['Код товара']
        article = product['Артикул']
        id_product = product['ID']
        brand = product['brand']
        raw_description = product['description']
        
        # 2 Генерация уникального описания по макету Figma 
        
        # Есть два способа первое если у вас есть API то можно через generate_description_onlain
        # unique_desc = generate_description_onlain(raw_description=str(raw_description), product_title=title, brand=brand)
        
        # Вторе через загрузку модели она бесплатна 
        unique_desc = generate_description_offlain(raw_description=str(raw_description), product_title=title, brand=brand)

        # 3 Генерация мета
        meta = generate_meta(title, brand)
        

        # 4 Сбор строки для таблици
        start_3 = time.time()
        row = [title, article, code_product, id_product, meta['meta_title'], meta['meta_description'], meta['meta_keywords'], str(unique_desc)]
        final_row.append(row)
        

    print(f"Генерация мета и Сбор строки для таблици. Завершено за {time.time() - start_2:.2f}сек")
    
    # 5 Запись в Google Таблицу
    print("Запись в Google Таблицу.")
    start_3 = time.time()
    write_to_sheet(final_row)
    print(f"Запись в Google Таблицу. Завершено за {time.time() - start_3:.2f}сек")
    



if __name__ == "__main__":
    main()
    