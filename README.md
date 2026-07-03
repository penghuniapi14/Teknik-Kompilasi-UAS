# Simulasi Tahapan Kompilasi Menggunakan Python

## Nama Mahasiswa
Muhamad Andriyansyah

## Mata Kuliah
Teknik Kompilasi

## Deskripsi Project

Project ini merupakan simulasi sederhana proses kompilasi menggunakan bahasa pemrograman Python. Program dibuat untuk memperlihatkan bagaimana sebuah source code diproses melalui beberapa tahapan compiler, yaitu:

- Analisis Leksikal (Lexical Analysis)
- Analisis Sintaksis (Syntax Analysis)
- Analisis Semantik (Semantic Analysis)
- Generasi Three Address Code (TAC)

Konstruksi sintaksis yang dipilih pada project ini adalah **Perulangan While (While Loop)**.

---

# Tujuan

Tujuan pembuatan project ini adalah:

1. Memahami proses kerja compiler.
2. Mempelajari proses pembentukan token.
3. Mempelajari pembentukan Abstract Syntax Tree (AST).
4. Memahami proses validasi semantik.
5. Menghasilkan Three Address Code (TAC).

---

# Struktur Project

```
Teknik-Kompilasi-UAS
│
├── compiler.py
├── lexer.py
├── parser.py
├── semantic.py
├── tac.py
├── grammar.txt
├── contoh_input.txt
├── output.txt
└── README.md
```

---

# Tahapan Kompilasi

## 1. Lexical Analysis

Tahap pertama compiler adalah memecah source code menjadi token.

Contoh source code:

```c
while (x < 10) {
    x = x + 1;
}
```

Token yang dihasilkan:

```
WHILE
LPAREN
IDENTIFIER(x)
OPERATOR(<)
NUMBER(10)
RPAREN
LBRACE
IDENTIFIER(x)
OPERATOR(=)
IDENTIFIER(x)
OPERATOR(+)
NUMBER(1)
SEMICOLON
RBRACE
```

---

## 2. Syntax Analysis

Tahap kedua adalah membentuk Abstract Syntax Tree (AST).

AST yang dihasilkan:

```
WHILE
├── CONDITION
│     ├── x
│     ├── <
│     └── 10
│
└── BODY
      ├── x
      ├── =
      └── x + 1
```

---

## 3. Semantic Analysis

Tahap ini melakukan pengecekan terhadap:

- Operator valid
- Variabel valid
- Nilai numerik
- Konsistensi assignment

Jika seluruh pemeriksaan berhasil maka program dinyatakan valid.

---

## 4. Three Address Code (TAC)

Kode antara yang dihasilkan adalah:

```
L1:
ifFalse x < 10 goto L2
t1 = x + 1
x = t1
goto L1
L2:
```

---

# Cara Menjalankan Program

Pastikan Python 3 telah terinstall.

Jalankan perintah berikut:

```bash
python compiler.py
```

---

# Output Program

Program akan menampilkan:

- Source Code
- Hasil Lexical Analysis
- Hasil Syntax Analysis
- Hasil Semantic Analysis
- Hasil Three Address Code

Seluruh hasil juga akan disimpan pada file:

```
output.txt
```

---

# Teknologi yang Digunakan

- Python 3
- Regular Expression (Regex)
- Abstract Syntax Tree (AST)
- Three Address Code (TAC)

---

# Kesimpulan

Project ini berhasil mensimulasikan tahapan dasar proses kompilasi mulai dari analisis leksikal, analisis sintaksis, analisis semantik, hingga menghasilkan Three Address Code (TAC). Meskipun masih sederhana, program ini dapat memberikan gambaran mengenai proses kerja compiler pada bahasa pemrograman.
