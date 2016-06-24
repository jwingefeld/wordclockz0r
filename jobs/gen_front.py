from generate import generate
import sys

if __name__ == '__main__':
    arg1 = sys.argv[2:]
    arg2 = sys.argv[1]

    gens = []
    for a in range(5):
        gens.append(generate(arg1,arg2,a))

    print(min(gens, key=len))
