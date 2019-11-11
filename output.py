def write_score(file, score):
    file.write(f'SCORE: {score}\n')

def write_solution(file, solution):
    file.write('\n' + solution.dumps())

def save_solutions(path, final_score, solution_generator):
    with open(path, '+w') as file:
        write_score(file, final_score)

        for solution in solution_generator:
            write_solution(file, solution) 
