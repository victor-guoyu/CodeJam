def main():
    file_name = "A-small-practice.in"
    file = open(file_name)

    total_cases = int(file.readline())

    for case_number in range(total_cases):
        vector_size = int(file.readline())
        first_vector = map(int, file.readline().split())
        second_vector = map(int, file.readline().split())
        min_scalar_product = _get_min_scalar_product(first_vector, second_vector, vector_size)
        print("Case #%s: %s" % ((case_number + 1), min_scalar_product))


def _get_min_scalar_product(first_vector, second_vector, size):
    min_scalar = 0
    for _ in range(size):
        min_value = min(first_vector)
        max_value = max(second_vector)
        min_scalar += min_value * max_value
        first_vector.remove(min_value)
        second_vector.remove(max_value)

    return min_scalar


if __name__ == "__main__":
    main()
