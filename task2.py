"""
Індексація та вибірка даних:
Створіть двовимірний масив 8x8, який відображає шахову дошку (1 - біла клітина, 0 - чорна клітина).
Використовуйте індексацію для виведення на екран:
Рядок, представляючи 3-й рядок з дошки.
Стовпець, представляючи 5-й стовпець з дошки.
Підмасив, представляючи частину дошки розміром 3x3 в лівому верхньому куті.
"""

import numpy as np

# Створення двовимірного масиву 8x8, заповненого нулями
chess_board = np.zeros((8, 8), dtype=int)

# # Заповнення масиву
chess_board[1::2, ::2] = 1  # 1 на непарних рядках, парних стовпцях
chess_board[::2, 1::2] = 1  # 1 на парних рядках, непарних стовпцях

# Виведення масиву на екран
print(chess_board)
