# ==========================================
# semantic.py
# Semantic Analyzer
# Teknik Kompilasi - UAS
# ==========================================

VALID_CONDITION_OPERATORS = [
    "<",
    ">",
    "<=",
    ">=",
    "==",
    "!="
]

VALID_ARITHMETIC_OPERATORS = [
    "+",
    "-",
    "*",
    "/"
]


def semantic_analysis(ast):
    """
    Melakukan pengecekan semantik
    terhadap AST hasil parser.
    """

    print("Memulai pengecekan semantik...\n")

    # -----------------------------
    # Ambil bagian AST
    # -----------------------------
    condition = ast["condition"]
    body = ast["body"]

    cond_var = condition["left"]
    cond_operator = condition["operator"]
    cond_value = condition["right"]

    target = body["target"]
    left = body["left"]
    operator = body["operator"]
    right = body["right"]

    # -----------------------------
    # Cek operator kondisi
    # -----------------------------
    if cond_operator not in VALID_CONDITION_OPERATORS:
        raise Exception(
            f"Semantic Error: Operator '{cond_operator}' tidak valid."
        )

    # -----------------------------
    # Cek operator aritmatika
    # -----------------------------
    if operator not in VALID_ARITHMETIC_OPERATORS:
        raise Exception(
            f"Semantic Error: Operator '{operator}' tidak valid."
        )

    # -----------------------------
    # Variabel target harus sama
    # -----------------------------
    if target != left:
        raise Exception(
            "Semantic Error: Variabel assignment tidak konsisten."
        )

    # -----------------------------
    # Variabel kondisi harus sama
    # -----------------------------
    if cond_var != target:
        raise Exception(
            "Semantic Error: Variabel pada kondisi dan body berbeda."
        )

    # -----------------------------
    # Nilai pembanding harus angka
    # -----------------------------
    if not cond_value.isdigit():
        raise Exception(
            "Semantic Error: Nilai pembanding harus berupa angka."
        )

    # -----------------------------
    # Nilai penjumlahan harus angka
    # -----------------------------
    if not right.isdigit():
        raise Exception(
            "Semantic Error: Operand kanan harus berupa angka."
        )

    # -----------------------------
    # Informasi berhasil
    # -----------------------------
    print("✓ Operator kondisi valid")
    print("✓ Operator aritmatika valid")
    print("✓ Variabel kondisi benar")
    print("✓ Variabel assignment benar")
    print("✓ Nilai pembanding valid")
    print("✓ Ekspresi aritmatika valid")

    return True


# ==========================================
# Pengujian Semantic Analyzer
# ==========================================

if __name__ == "__main__":

    sample_ast = {

        "type": "WHILE",

        "condition": {
            "left": "x",
            "operator": "<",
            "right": "10"
        },

        "body": {
            "target": "x",
            "left": "x",
            "operator": "+",
            "right": "1"
        }

    }

    print("===== SEMANTIC ANALYSIS =====\n")

    if semantic_analysis(sample_ast):

        print("\nSemantic Analysis SUCCESS")
