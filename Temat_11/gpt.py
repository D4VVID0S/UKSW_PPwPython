import matplotlib.pyplot as plt

# Tworzenie układu 2x2 (2 wiersze, 2 kolumny)
plt.subplot(2, 2, 1)  # Wykres w pierwszej komórce
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.subplot(2, 2, 2)  # Wykres w drugiej komórce
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])

plt.subplot(2, 2, 3)  # Wykres w trzeciej komórce
plt.plot([1, 2, 3, 4], [4, 3, 2, 1])

plt.subplot(2, 2, 4)  # Wykres w czwartej komórce
plt.plot([1, 2, 3, 4], [1, 3, 5, 7])

plt.show()  # Wyświetlenie wszystkich wykresów
