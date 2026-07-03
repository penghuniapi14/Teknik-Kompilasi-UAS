# ==========================================
# compiler.py
# Program Utama Simulasi Tahapan Kompilasi
# Teknik Kompilasi - UAS
# ==========================================

from lexer import lexical_analysis
from parser import syntax_analysis
from semantic import semantic_analysis
from tac import generate_tac


def garis():
    print("=" * 60)


def tampilkan_tokens(tokens):
    for i, token in enumerate(tokens, start=1):
        print(f"{i:02d}. {token}")


def tampilkan_ast(ast):
    print("\nAbstract Syntax Tree (AST)")
    print("----------------------------")

    if isinstance(ast, dict):
        for key, value in ast.items():
            print(f"{key} : {value}")
    else:
        print(ast)


def main():

    print("\nSIMULASI TAHAPAN KOMPILASI")
    print("Konstruksi : WHILE LOOP")
    garis()

    try:
        with open("contoh_input.txt", "r") as file:
            source_code = file.read()

    except FileNotFoundError:
        print("File contoh_input.txt tidak ditemukan.")
        return

    print("\nSource Code")
    garis()
    print(source_code)

    # ==========================
    # LEXICAL ANALYSIS
    # ==========================
    print("\nTAHAP 1 : LEXICAL ANALYSIS")
    garis()

    tokens = lexical_analysis(source_code)

    tampilkan_tokens(tokens)

    # ==========================
    # SYNTAX ANALYSIS
    # ==========================
    print("\nTAHAP 2 : SYNTAX ANALYSIS")
    garis()

    ast = syntax_analysis(tokens)

    tampilkan_ast(ast)

    # ==========================
    # SEMANTIC ANALYSIS
    # ==========================
    print("\nTAHAP 3 : SEMANTIC ANALYSIS")
    garis()

    semantic_result = semantic_analysis(ast)

    if semantic_result:

        print("✓ Semantic Analysis berhasil")
        print("✓ Tidak ditemukan error semantik")

    else:

        print("✗ Terjadi kesalahan semantik")
        return

    # ==========================
    # TAC
    # ==========================
    print("\nTAHAP 4 : THREE ADDRESS CODE")
    garis()

    tac = generate_tac(ast)

    for line in tac:
        print(line)

    # ==========================
    # SIMPAN OUTPUT
    # ==========================

    with open("output.txt", "w") as file:

        file.write("SIMULASI TAHAPAN KOMPILASI\n")
        file.write("=" * 50 + "\n\n")

        file.write("SOURCE CODE\n")
        file.write(source_code + "\n\n")

        file.write("TOKENS\n")
        for token in tokens:
            file.write(token + "\n")

        file.write("\nAST\n")

        if isinstance(ast, dict):
            for key, value in ast.items():
                file.write(f"{key} : {value}\n")

        else:
            file.write(str(ast))

        file.write("\n\nTHREE ADDRESS CODE\n")

        for line in tac:
            file.write(line + "\n")

    print("\n")
    garis()
    print("Proses kompilasi selesai.")
    print("Output berhasil disimpan ke file output.txt")
    garis()


if __name__ == "__main__":
    main()
