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
    score = float(input("请输入成绩（0～100）："))
    print("成绩等级：", grade(score))