import os
from PIL import Image
import matplotlib.pyplot as plt

def load_png_image(file_path):
    try:
        image = Image.open(file_path)
        if image.format != 'PNG':
            raise ValueError("Podany plik nie jest w formacie PNG!")
        return image
    except FileNotFoundError:
        raise ValueError("Podany plik nie istnieje!")
    except Exception as e:
        raise ValueError(f"Wystąpił nieznany błąd: {e}")


def load_result_file():
    # Sprawdzenie istnienia pliku wynikowego
    result_file_name = input("Podaj nazwę pliku do zapisu wyników (domyślnie wyniki.txt): ")
    if not result_file_name:
        result_file_name = "wyniki.txt"

    result_file_path = os.path.join(os.getcwd(), result_file_name)

    if os.path.exists(result_file_path):
        overwrite = input("Plik z wynikami już istnieje. Czy chcesz go nadpisać? (T/N): ")
        if overwrite.lower() == "t":
            os.remove(result_file_path)
        else:
            print("Anulowano zapis wyników.")
            return None

    # Tworzenie nowego pliku wynikowego
    with open(result_file_path, 'w') as result_file:
        result_file.write("Statystyki obrazka\n")

    return result_file_path


def calculate_pixel_statistics(image):
    red_pixels = 0
    green_pixels = 0
    blue_pixels = 0
    gray_pixels = 0
    total_pixels = 0

    for pixel in image.getdata():
        r, g, b = pixel[:3]  # We extract only the RGB values
        max_value = max(r, g, b)
        
        if r == g == b:
            gray_pixels += 1
        elif g == max_value:
            green_pixels += 1
        elif r == max_value:
            red_pixels += 1
        elif b == max_value:
            blue_pixels += 1

        total_pixels += 1

    return red_pixels, green_pixels, blue_pixels, gray_pixels, total_pixels


def write_pixel_image_data(result_file_path, image_name, red_pixels, green_pixels, blue_pixels, gray_pixels, total_pixels):
    # Zapisanie statystyk do pliku wynikowego
    with open(result_file_path, 'a') as result_file:
        result_file.write(f"Nazwa pliku obrazka: {image_name}\n")
        result_file.write(f"Liczba czerwonych pikseli: {red_pixels}\n")
        result_file.write(f"Liczba zielonych pikseli: {green_pixels}\n")
        result_file.write(f"Liczba niebieskich pikseli: {blue_pixels}\n")
        result_file.write(f"Liczba szarych pikseli: {gray_pixels}\n")
        result_file.write(f"Łączna liczba pikseli: {total_pixels}\n")

    print("Statystyki obrazka zostały zapisane poprawnie!")


def show_pie_chart(red_pixels, green_pixels, blue_pixels, gray_pixels):
    # Wykres kołowy z procentowym udziałem kolorów
    labels = ['Czerwony', 'Zielony', 'Niebieski', 'Szary']
    sizes = [red_pixels, green_pixels, blue_pixels, gray_pixels]
    colors = ['red', 'green', 'blue', 'gray']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.set_title("Procentowy udział kolorów pikseli")
    ax.axis('equal')
    plt.show()


def main():
    # Pobranie bieżącego katalogu roboczego
    current_directory = os.getcwd()

    # Pobranie nazwy pliku obrazka od użytkownika
    image_name = input("Podaj nazwę pliku obrazka (PNG): ")

    # Tworzenie pełnej ścieżki do pliku obrazka
    image_path = os.path.join(current_directory, image_name)

    # Wczytanie pliku wynikowego
    result_file_path = load_result_file()

    if result_file_path is None:
        exit()

    # Wczytanie obrazka
    try:
        loaded_image = load_png_image(image_path)
        # Obliczenie statystyk pikseli
        red_pixels, green_pixels, blue_pixels, gray_pixels, total_pixels = calculate_pixel_statistics(loaded_image)

        # Zapisanie statystyk do pliku wynikowego
        write_pixel_image_data(result_file_path, image_name, red_pixels, green_pixels, blue_pixels, gray_pixels, total_pixels)

        # Wyświetlenie wykresu kołowego
        show_pie_chart(red_pixels, green_pixels, blue_pixels, gray_pixels)

    except ValueError as ve:
        print(f"Wystąpił błąd: {ve}")


if __name__ == '__main__':
    main()
