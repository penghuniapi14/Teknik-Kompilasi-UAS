# ==========================================
# tac.py
# Three Address Code Generator
# Teknik Kompilasi - UAS
# ==========================================


class TACGenerator:

    def __init__(self):
        self.temp_count = 1
        self.label_count = 1
        self.code = []

    # -----------------------------
    # Membuat Temporary Variable
    # -----------------------------
    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    # -----------------------------
    # Membuat Label
    # -----------------------------
    def new_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    # -----------------------------
    # Generate TAC
    # -----------------------------
    def generate(self, ast):

        condition = ast["condition"]
        body = ast["body"]

        start_label = self.new_label()
        end_label = self.new_label()

        self.code.append(f"{start_label}:")

        self.code.append(
            f"ifFalse {condition['left']} "
            f"{condition['operator']} "
            f"{condition['right']} "
            f"goto {end_label}"
        )

        temp = self.new_temp()

        self.code.append(
            f"{temp} = "
            f"{body['left']} "
            f"{body['operator']} "
            f"{body['right']}"
        )

        self.code.append(
            f"{body['target']} = {temp}"
        )

        self.code.append(
            f"goto {start_label}"
        )

        self.code.append(
            f"{end_label}:"
        )

        return self.code


# ==========================================
# Fungsi yang dipanggil compiler.py
# ==========================================

def generate_tac(ast):

    generator = TACGenerator()

    return generator.generate(ast)


# ==========================================
# Pengujian
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

    tac = generate_tac(sample_ast)

    print("===== THREE ADDRESS CODE =====\n")

    for line in tac:
        print(line)
