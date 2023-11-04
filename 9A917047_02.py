student_info = {
    "sid": "9A123456",
    "sname": "王小明",
    "fchina": float(input("請輸入您的國文成績：")),
    "fmath": float(input("請輸入您的數學成績：")),
    "finfo": float(input("請輸入您的電腦成績："))
}

# 計算總分和平均分數
total_score = student_info["fchina"] + student_info["fmath"] + student_info["finfo"]
average_score = total_score / 3

# 判定是否合格
if average_score >= 60:
    result = "合格"
else:
    result = "不及格"

# 格式化輸出
print("-" * 30)
print(f"{student_info['sname']}({student_info['sid']})同學您好：")
print(f"以下是您的各科成績與分數評定\n")
print(f"國文：{student_info['fchina']} / 數學：{student_info['fmath']} / 電腦：{student_info['finfo']}")
print(f"總分：{total_score} / 平均：{round(average_score, 2)}")
print("-" * 30)
print(f"成績判定：{result}")