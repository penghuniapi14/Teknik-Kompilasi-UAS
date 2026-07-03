# ==========================================
# lexer.py
# Lexical Analyzer
# Teknik Kompilasi - UAS
# ==========================================

import re

# Daftar token yang dikenali
TOKEN_SPECIFICATION = [
    ("WHILE",      r"\bwhile\b"),
    ("NUMBER",     r"\b\d+\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("OPERATOR",   r"<=|>=|==|!=|<|>|=|\+|-|\*|/"),
    ("LPAREN",     r"\("),
    ("RPAREN",     r"\)"),
    ("LBRACE",     r"\{"),
    ("RBRACE",     r"\}"),
    ("SEMICOLON",  r";"),
    ("COMMA",      r","),
    ("NEWLINE",    r"\n"),
    ("SKIP",       r"[ \t]+"),
    ("MISMATCH",   r"."),
]

# Menggabungkan semua regex
TOKEN_REGEX = "|".join(
    f"(?P<{name}>{pattern})"
    for name, pattern in TOKEN_SPECIFICATION
)


def lexical_analysis(source_code):
    """
    Melakukan analisis leksikal terhadap source code
    dan menghasilkan daftar token.
    """

    tokens = []

    for match in re.finditer(TOKEN_REGEX, source_code):

        kind = match.lastgroup
        value = match.group()

        if kind == "SKIP":
            continue

        elif kind == "NEWLINE":
            continue

        elif kind == "MISMATCH":
            raise SyntaxError(
                f"Karakter tidak dikenali: {value}"
            )

        else:
            tokens.append(f"{kind}({value})")

    return tokens


# ==========================================
# Pengujian Lexer
# ==========================================

if __name__ == "__main__":

    source = """
while (x < 10) {
    x = x + 1;
}
"""

    hasil = lexical_analysis(source)

    print("===== HASIL TOKEN =====")

    for nomor, token in enumerate(hasil, start=1):
        print(f"{nomor:02d}. {token}")
