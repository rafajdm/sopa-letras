from word_generator import get_related_words as get_random_words
from word_search_generator import generate_word_search
from pdf_generator import create_pdf
import random
import unicodedata

def normalize_word(word):
    # Eliminar acentos y convertir a mayúsculas
    normalized_word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode('ASCII')
    # Reemplazar ñ por n
    normalized_word = normalized_word.replace('ñ', 'n').replace('Ñ', 'N')
    return normalized_word.upper()

def main():
    num_prompts = 5
    size = 20
    words_to_search_count = 20  # Número de palabras principales que se buscarán
    puzzles = []
    words_list = []

    for _ in range(num_prompts):
        # Obtener palabras desde el word_generator.py
        all_words = get_random_words()  # Esto devuelve entre 20 y 30 palabras

        # Normalizar las palabras
        all_words = [normalize_word(word) for word in all_words]

        # Validar que se obtuvieron suficientes palabras
        if len(all_words) < words_to_search_count:
            words_to_search_count = len(all_words)  # Ajustar el número de palabras a buscar si hay menos de 20

        # Dividir las palabras en dos grupos
        words_to_search = all_words[:words_to_search_count]  # Primeras palabras para buscar
        additional_words = all_words[words_to_search_count:]  # Resto como palabras adicionales

        # Combinar las palabras para el puzzle
        all_words_in_grid = words_to_search + additional_words

        # Generar el puzzle
        puzzle = generate_word_search(all_words_in_grid, size)
        puzzles.append(puzzle)
        words_list.append(words_to_search)

    # Crear el PDF con las sopas de letras generadas
    create_pdf(puzzles, words_list)

if __name__ == "__main__":
    main()