import csv
import math
from pathlib import Path

FILE = Path("grades.csv")

def ensure_file():
    if not FILE.exists():
        FILE.write_text("name,credits,grade,counts\n", encoding="utf-8")

def load_modules():
    modules = []
    with FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            modules.append({
                "name": row["name"],
                "credits": float(row["credits"]),
                "grade": float(row["grade"]),
                "counts": int(row.get("counts",1))
            })
    return modules

def add_module():
    name = input("Module name: ").strip()
    credits = float(input("Credits (ECTS): ").strip())
    grade = float(input("Grade (1.0 best … 4.0 fail): ").strip())
    counts_input = input("Counts toward final grade? (y/n): ").strip().lower()
    counts = 1 if counts_input == "y" else 0

    # basic validation (adjust if your uni uses other rules)
    if credits <= 0:
        print("Credits must be > 0.")
        return None
    if grade < 1.0 or grade > 4.0:
        print("Grade must be between 1.0 and 4.0.")
        return None

    with FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, credits, grade, counts])

    return {"name": name, "credits": credits, "grade": grade, "counts":counts}  

def calc_weighted_average(modules):
    # modules that affect the grade
    grade_modules = [m for m in modules if m["counts"] == 1]

    grade_credits = sum(m["credits"] for m in grade_modules)
    if grade_credits == 0:
        return None

    weighted_sum = sum(m["credits"] * m["grade"] for m in grade_modules)
    return weighted_sum / grade_credits

def show(modules):
    avg = calc_weighted_average(modules)
    if avg is None:
        print("No modules yet.")
        return

    total_credits = sum(m["credits"] for m in modules)
    print("\n--- Summary ---")
    print(f"Modules: {len(modules)}")
    print(f"Total ECTS: {total_credits:g}")
    portal_avg = math.floor(avg * 10) / 10   # truncate to 1 decimal
    print(f"Weighted average (German, 2 decimals): {avg:.2f}")
    print(f"Weighted average (Portal style, 1 decimal trunc): {portal_avg:.1f}")

def main():
    ensure_file()
    modules = load_modules()

    while True:
        print("\n1) Add module")
        print("2) Show average")
        print("3) List modules")
        print("4) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            m = add_module()
            if m:
                modules.append(m)
        elif choice == "2":
            show(modules)
        elif choice == "3":
            if not modules:
                print("No modules yet.")
            else:
                for i, m in enumerate(modules, 1):
                    print(f"{i:>2}. {m['name']} | {m['credits']:g} ECTS | grade {m['grade']}")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()