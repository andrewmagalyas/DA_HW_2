"""
Статистика та робота зі зображеннями:
Завантажте зображення (наприклад, за допомогою бібліотеки Pillow).
Перетворіть його в тривимірний NumPy-масив та виведіть інформацію про розмір та тип даних. Проведіть статистичний аналіз:
Знайдіть середнє значення, мінімум та максимум для кожного каналу зображення (R, G, B).
Підрахуйте загальну суму інтенсивності пікселів та виведіть її.
Виконайте нормалізацію зображення, розділивши значення кожного пікселя на максимальне значення.
"""

from PIL import Image
import numpy as np

# Завантаження зображення
image_path = "unnamed.jpg"
img = Image.open(image_path)

# Перетворення зображення в NumPy-масив
img_array = np.array(img)

# Виведення інформації про розмір та тип даних
print(f"Розмір зображення: {img_array.shape}")
print(f"Тип даних: {img_array.dtype}")

# Статистичний аналіз
# Середнє значення, мінімум та максимум для кожного каналу
for i, color in enumerate(['Red', 'Green', 'Blue']):
    channel = img_array[:,:,i]
    print(f"\n{color} канал:")
    print(f"Середнє значення: {np.mean(channel):.2f}")
    print(f"Мінімум: {np.min(channel)}")
    print(f"Максимум: {np.max(channel)}")

# Загальна сума інтенсивності пікселів
total_intensity = np.sum(img_array)
print(f"\nЗагальна сума інтенсивності пікселів: {total_intensity}")

# Нормалізація зображення
max_value = np.max(img_array)
normalized_img = img_array / max_value

print(f"\nМаксимальне значення перед нормалізацією: {max_value}")
print(f"Максимальне значення після нормалізації: {np.max(normalized_img)}")
print(f"Мінімальне значення після нормалізації: {np.min(normalized_img):.4f}")

# Збереження нормалізованого зображення
normalized_img_pil = Image.fromarray((normalized_img * 255).astype(np.uint8))
normalized_img_pil.save("normalized_image.jpg")






