from input import *
from solver import NeedlemanWunshSolver
from solution_generator import SolutionGenerator
from output import * 

if __name__ == '__main__':

    args = parse_args()
    
    try:
        config = parse_config(args.config)
        seq_a = read_sequence(args.seq_a, config['MAX_SEQ_LENGTH'])
        seq_b = read_sequence(args.seq_b, config['MAX_SEQ_LENGTH'])
        solver = NeedlemanWunshSolver(config['SAME'], config['DIFF'], config['GAP_PENALTY'])
        score_mat, directions, final_score = solver.solve(seq_a, seq_b)
        solution_generator = SolutionGenerator(directions, seq_a, seq_b, config['MAX_NUMBER_PATHS']) 
        save_solutions(args.output_path, final_score, solution_generator)

    except (KeyError, ValueError) as e:
        print(e)