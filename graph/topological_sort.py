# course prerequsite
# O(V+E)
from collections import defaultdict, deque

def find_order(course_to_prereqs):
    # copy list values into a set for faster removal
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

    # start off our to-do list with all courses without prereq
    todo = deque([c for c, p in course_to_prereqs.items() if not p])

    # build graph map prereq to successor courses
    prereq_to_courses = defaultdict(list)
    for course, prereqs in course_to_prereqs.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].append(course)
    result = []

    while todo:
        prereq = todo.popleft()
        result.append(prereq)

        for c in prereq_to_courses[prereq]:
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs:
                todo.append(c)

    # circular dependency
    if len(result) < len(course_to_prereqs):
        return None

    return result