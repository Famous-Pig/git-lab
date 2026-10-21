def grade(score):
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 70:
        return "中等"
    if score >= 60:
        return "及格"
    return "不及格"


if __name__ == "__main__":
    try:
        score = float(input("请输入成绩（0～100）："))
    except ValueError:
        print("输入错误：请输入数字。")
    else:
        if not 0 <= score <= 100:
            print("范围错误：成绩必须在0～100之间。")
        else:
            print("成绩等级：", grade(score))