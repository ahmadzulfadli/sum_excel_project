from sympy import symbols, sympify
import re

nilai = 600.98

rumus = "x*5/60000"

if rumus is None or not rumus.strip():
    print("Rumus kosong")
else:
    rumus = rumus.lower()
    rumus = re.sub(r'\s+', ' ', rumus)

    if re.search(r'[^x0-9+\-*/(). ]', rumus):
        print("Rumus hanya boleh mengandung 'x', angka, dan operator matematika.")
    else:
        try:
            x = symbols('x')

            expr = sympify(rumus)

            result = expr.subs(x, float(nilai))
            print(f"rumus {expr}")
            print("Hasil evaluasi:", result)
        except Exception as e:
            print("Terjadi kesalahan dalam evaluasi rumus:", e)

