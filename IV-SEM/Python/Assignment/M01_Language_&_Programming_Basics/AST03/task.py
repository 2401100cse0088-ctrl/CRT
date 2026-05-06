import math

def Student_Grade_System(name: str, n1: float, n2: float, n3: float) -> str:
    avg = (n1 + n2 + n3) / 3
    avg = math.floor(avg * 100) / 100

    if avg.is_integer():
        avg_str = f"{avg:.1f}"
    else:
        avg_str = f"{avg:.2f}"

    status = "Pass" if avg >= 40 else "fail"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input().strip()
    n1, n2, n3 = map(float, input().split())
    print(Student_Grade_System(name, n1, n2, n3))