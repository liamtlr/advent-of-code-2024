from collections import defaultdict

def extract_left_and_right(path: str) -> list[list[int]]:
    with open(path) as infile:
        lines = infile.readlines()
    DELIMITER = '   '
    lefts, rights = [], []
    for row in lines:
        left, right = row.split(DELIMITER)
        lefts.append(int(left))
        rights.append(int(right))
    return lefts, rights

def task_one() -> int:
    lefts, rights = extract_left_and_right('./day-01/input.txt')
    ordered_lefts, ordered_rights = sorted(lefts), sorted(rights)
    return sum(
        abs(value - ordered_rights[i])
        for i, value in enumerate(ordered_lefts)
    )

def task_two() -> int:
    lefts, rights = extract_left_and_right('./day-01/input.txt')
    similarity_scores = defaultdict(int)
    similarity_scores_totals = defaultdict(int)

    def get_similarity_score(value: int) -> int:
        frequency = sum(
            1 
            for right in rights
            if value == right
        )
        return frequency * value
    
    for left in lefts:
        if left in similarity_scores:
            similarity_score = similarity_scores[left]
        else:
            similarity_score = get_similarity_score(left)
            similarity_scores[left] = similarity_score
        similarity_scores_totals[left] += similarity_score

    return sum(similarity_scores_totals.values())

print(task_one())
print(task_two())
