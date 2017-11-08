import random


def generate_test_file(filename: str, n_lines: int):
    with open(filename, 'w') as f:
        for _ in range(n_lines):
            print(random.randint(100, 120), file=f)


if __name__ == '__main__':
    generate_test_file('test_data', 1000000)
