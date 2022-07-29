def round_scores(student_scores):
    scores = []
    for score in student_scores:
        scores.append(round(score))
    return scores

def count_failed_students(student_scores):
    total = 0
    for score in student_scores:
        if score <= 40:
            total += 1
    return total

def above_threshold(student_scores, threshold):
    scores = []
    for score in student_scores:
        if score >= threshold:
            scores.append(score)
    return scores


def letter_grades(highest):
    gap = int(highest / 4) - 10
    results = []
    for i in range(4):
        results.append(41 + (gap * i))
    return results

def student_ranking(student_scores, student_names):
    ranking = []
    for i in range(len(student_scores)):
        ranking.append(f"{i + 1}. {student_names[i]}: {student_scores[i]}")
    return ranking


def perfect_score(student_info):
    perfect = []
    for name, score in student_info:
        if score == 100:
            perfect.append(name)
            perfect.append(score)
            break
        else:
            pass
    return perfect
