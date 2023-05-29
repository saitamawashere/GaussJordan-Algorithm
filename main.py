def gauss_jordan(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for pivot_row in range(num_rows):
        pivot_col = pivot_row

        # Cari pivot non-zero pertama di kolom pivot
        while matrix[pivot_row][pivot_col] == 0:
            pivot_row += 1
            if pivot_row == num_rows:
                return None

        # Lakukan pivot pada baris pivot
        matrix[pivot_row], matrix[pivot_col] = matrix[pivot_col], matrix[pivot_row]

        # Normalisasi baris pivot
        pivot_value = matrix[pivot_col][pivot_col]
        for col in range(num_cols):
            matrix[pivot_col][col] /= pivot_value

        # Eliminasi pada baris-baris lain
        for row in range(num_rows):
            if row != pivot_col:
                factor = matrix[row][pivot_col]
                for col in range(num_cols):
                    matrix[row][col] -= factor * matrix[pivot_col][col]

    return matrix

# Membaca input matriks dari pengguna
num_rows = int(input("Masukkan jumlah baris: "))
num_cols = int(input("Masukkan jumlah kolom: "))

matrix = []
for row in range(num_rows):
    print(f"Masukkan elemen-elemen baris ke-{row + 1}:")
    row_elements = list(map(float, input().split()))
    matrix.append(row_elements)

# Menjalankan algoritma Gauss-Jordan
result = gauss_jordan(matrix)

# Mencetak hasil
if result is None:
    print("Tidak ada solusi unik.")
else:
    print("Solusi:")
    for row in result:
        print(row)