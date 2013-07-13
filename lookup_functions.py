# finds edit distance between two strings
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def load_answers():
    answers = #query database for answers for this quiz id, ordered by position
    return [answer.split(',') for answer in answers]

#returns true if answer is one word and answer appears in user provided answer
def check_name(user_input,answer):
    if len(answer.split()) != 1:
        return false
    input_words = user_input.split()
    for word in input_words:
        if levenstein(word,answer) < 3:
            return true
    return false

# takes in answers array, user submitted answer, corresponding question number, and boolean to determine if all answers should be checked
# returns positions of questions that were correctly answered
def lookup(answers,submission,qnum,check_all):
    if not check_all:
        for answer in answer[qnum]
            if levenshtein(submission,answer) < 3 or check_name(submission,answer):
                return [qnum]
        return []
    else:
        question_array = []
        length = len(answers)
        for i in range(length):
            for answer in answers[i]:
                if levenshtein(submission,answer) < 3 or check_name(submission,answer):
                    question_array.append(i)
        return question_array

