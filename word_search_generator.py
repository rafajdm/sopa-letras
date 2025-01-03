import random

def generate_word_search(words, size=20):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    for word in words:
        placed = False
        attempts = 0
        max_attempts = 100  # Limitar el número de intentos para colocar una palabra
        while not placed and attempts < max_attempts:
            direction = random.choice(directions)
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if can_place_word(grid, word, row, col, direction, size):
                place_word(grid, word, row, col, direction)
                placed = True
            attempts += 1
        if not placed:
            raise ValueError(f"No se pudo colocar la palabra '{word}' en el grid después de {max_attempts} intentos.")
    
    fill_empty_spaces(grid, size)
    return grid

def can_place_word(grid, word, row, col, direction, size):
    try:
        for i in range(len(word)):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size or grid[new_row][new_col] != ' ':
                return False
        return True
    except IndexError as e:
        print(f"Error al verificar si se puede colocar la palabra: {e}")
        return False

def place_word(grid, word, row, col, direction):
    try:
        for i in range(len(word)):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            grid[new_row][new_col] = word[i]
    except IndexError as e:
        print(f"Error al colocar la palabra en el grid: {e}")

def fill_empty_spaces(grid, size):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        for row in range(size):
            for col in range(size):
                if grid[row][col] == ' ':
                    grid[row][col] = random.choice(letters)
    except Exception as e:
        print(f"Error al llenar los espacios vacíos: {e}")