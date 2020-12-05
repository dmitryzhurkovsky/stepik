with open('/Users/dmitry/downloads/dataset_3363_4.txt', 'r') as infile, open('/Users/dmitry/downloads/2.txt', 'w') as outfile:
    math_score_evri, physics_grade_evri, russian_mark_evri = 0, 0, 0
    for line in infile:
        line = line.strip().split(';')

        math_score = int(line[1])
        math_score_evri += math_score

        physics_grade = int(line[2])
        physics_grade_evri += physics_grade

        russian_mark = int(line[3])
        russian_mark_evri += russian_mark

        average_grade_each_student = (math_score + physics_grade + russian_mark) / 3

        outfile.write(str(average_grade_each_student) + '\n')
    outfile.write(str(math_score_evri / len(line)) + ' ' + str(physics_grade_evri / len(line)) + ' ' + str(russian_mark_evri / len(line)))
