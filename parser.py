# ==========================================
# parser.py
# Syntax Analyzer (Parser)
# Teknik Kompilasi - UAS
# ==========================================

def syntax_analysis(tokens):
    """
    Membentuk Abstract Syntax Tree (AST)
    dari token hasil lexical analysis.
    """

    values = []

    for token in tokens:

        if "(" in token:
            token_type = token[:token.index("(")]
            token_value = token[token.index("(")+1:-1]
        else:
            token_type = token
            token_value = ""

        values.append((token_type, token_value))

    # ===============================
    # Validasi struktur while
    # ===============================

    if len(values) < 14:
        raise SyntaxError("Struktur WHILE tidak lengkap.")

    if values[0][0] != "WHILE":
        raise SyntaxError("Program harus diawali keyword WHILE.")

    if values[1][0] != "LPAREN":
        raise SyntaxError("Kurang tanda '(' setelah WHILE.")

    if values[5][0] != "RPAREN":
        raise SyntaxError("Kurang tanda ')'.")

    if values[6][0] != "LBRACE":
        raise SyntaxError("Kurang tanda '{'.")

    if values[-1][0] != "RBRACE":
        raise SyntaxError("Kurang tanda '}'.")

    # ===============================
    # Ambil kondisi
    # ===============================

    condition = {
        "left": values[2][1],
        "operator": values[3][1],
        "right": values[4][1]
    }

    # ===============================
    # Ambil isi body
    # x = x + 1;
    # ===============================

    assignment = {
        "target": values[7][1],
        "left": values[9][1],
        "operator": values[10][1],
        "right": values[11][1]
    }

    # ===============================
    # Bentuk AST
    # ===============================

    ast = {
        "type": "WHILE",

        "condition": condition,

        "body": assignment
    }

    return ast


# ==========================================
# Menampilkan AST
# ==========================================

def print_ast(ast):

    print("WHILE")

    print("├── CONDITION")
    print(f"│     ├── Left      : {ast['condition']['left']}")
    print(f"│     ├── Operator  : {ast['condition']['operator']}")
    print(f"│     └── Right     : {ast['condition']['right']}")

    print("│")

    print("└── BODY")
    print(f"      ├── Target    : {ast['body']['target']}")
    print(f"      ├── Left      : {ast['body']['left']}")
    print(f"      ├── Operator  : {ast['body']['operator']}")
    print(f"      └── Right     : {ast['body']['right']}")


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    sample_tokens = [

        "WHILE(while)",
        "LPAREN(()",
        "IDENTIFIER(x)",
        "OPERATOR(<)",
        "NUMBER(10)",
        "RPAREN())",
        "LBRACE({)",
        "IDENTIFIER(x)",
        "OPERATOR(=)",
        "IDENTIFIER(x)",
        "OPERATOR(+)",
        "NUMBER(1)",
        "SEMICOLON(;)",
        "RBRACE(})"

    ]

    ast = syntax_analysis(sample_tokens)

    print("===== ABSTRACT SYNTAX TREE =====")
    print_ast(ast)
