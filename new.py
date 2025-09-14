import argparse
import os

# Argumentlarni pars qilish
parser = argparse.ArgumentParser(description="Yangi Codeforces problem fayl yaratish")
parser.add_argument("platform", type=str, help="Platform nomi, masalan: codeforces")
parser.add_argument("contest_number", type=str, help="Contest raqami, masalan: 2020")
parser.add_argument("problem_letter", type=str, help="Problem harfi, masalan: A")
args = parser.parse_args()

# Fayl nomini yaratish
plt = args.platform.lower()
contest = args.contest_number
problem = args.problem_letter.upper()  # katta harfga o'tkazamiz
file_name = f"{plt}_{contest}_{problem}.py"

# Fayl yaratish va shablon yozish (agar mavjud bo'lmasa)
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write(f"""# {file_name}

def main():
    pass

if __name__ == "__main__":
    main()
""")
    print(f"{file_name} yaratildi!")
else:
    print(f"{file_name} allaqachon mavjud.")
