
# Homework average:
hw_avg = 0.99
print(f"Homework Average: {hw_avg}")

# Reflection average: 
reflection_avg = 1
print(f"Reflection Average: {reflection_avg}")

# Quiz average: 
Onequiz_scores = [(14 / 20) ,(15 / 17), (10 / 10), (10 / 14), (10 / 10), (20 / 20)]
Twoquiz_scores = [0.7, 0.88, 1, 0.71, 1, 1]
quiz_avg = round((sum(Twoquiz_scores)) / len(Twoquiz_scores), 2)
print(f"Quiz average: {quiz_avg}")

# Exam average: 
exam_scores = [(24 / 40), (32.5 / 40), (19.5 / 40)]
exam_avg = round((sum(exam_scores) / len(exam_scores)), 2)
print(f"Exam Average: {exam_avg}")

# Final exam:
final_avg = 0.50
print(f"Final Score: {final_avg}")

#print(f"Cumulative Grade: {scheme_1(hw_avg, quiz_avg, exam_avg, reflection_avg, final_avg)}")


