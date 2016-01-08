class Cell(object):
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.value = 0
        self.visited = False


class DynamicGrid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.table = []
        for i in range(rows):
            self.table.append([])
            for j in range(columns):
                self.table[i].append(Cell(i, j))

    def operation_m(self, row_num, col_num, value):
        """Change a number in one cell of the grid to 0 or 1"""
        self.table[row_num][col_num].value = value

    def operation_q(self):
        """Determine the number of different connected regions of 1s"""
        # reset the board every time preform the q operation
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j].visited = False

        regions_count = 0
        for row_num in range(self.rows):
            for col_num in range(self.columns):
                cell = self.table[row_num][col_num]
                if cell.value == 1 and not cell.visited:
                    regions_count += 1
                    self._visit_region(row_num, col_num)

        print(regions_count)

    def _visit_region(self, row_num, col_num):
        cell = self.table[row_num][col_num]
        cell.visited = True
        # find all the neighbor cells
        neighbours = filter(None, [
            self._get_cell_left(cell),
            self._get_cell_top(cell),
            self._get_cell_right(cell),
            self._get_cell_below(cell),
        ])

        for neighbour in neighbours:
            if neighbour.value == 1 and not neighbour.visited:
                self._visit_region(neighbour.row_num, neighbour.col_num)

    def _get_top_left_cell(self, cell):
        top_left_row = cell.row_num - 1
        top_left_col = cell.col_num - 1
        if top_left_col >= 0 and top_left_row >= 0:
            return self.table[top_left_row][top_left_col]

        return None

    def _get_top_right_cell(self, cell):
        top_right_row = cell.row_num - 1
        top_right_col = cell.col_num + 1
        if top_right_row >= 0 and top_right_col < self.columns:
            return self.table[top_right_row][top_right_col]

        return None

    def _get_bottom_left_cell(self, cell):
        bottom_left_row = cell.row_num + 1
        bottom_left_col = cell.col_num - 1
        if bottom_left_row < self.rows and bottom_left_col >= 0:
            return self.table[bottom_left_row][bottom_left_col]

        return None

    def _get_bottom_right_cell(self, cell):
        bottom_right_row = cell.row_num + 1
        bottom_right_col = cell.col_num + 1
        if bottom_right_col < self.columns and bottom_right_row < self.rows:
            return self.table[bottom_right_row][bottom_right_col]

        return None

    def _get_cell_top(self, cell):
        upper_row_num = cell.row_num - 1
        upper_col_num = cell.col_num

        if upper_row_num >= 0:
            return self.table[upper_row_num][upper_col_num]

        return None

    def _get_cell_left(self, cell):
        left_row_num = cell.row_num
        left_col_num = cell.col_num - 1

        if left_col_num >= 0:
            return self.table[left_row_num][left_col_num]

        return None

    def _get_cell_right(self, cell):
        right_row_num = cell.row_num
        right_col_num = cell.col_num + 1

        if right_col_num < self.columns:
            return self.table[right_row_num][right_col_num]

        return None

    def _get_cell_below(self, cell):
        below_row_num = cell.row_num + 1
        below_col_num = cell.col_num

        if below_row_num < self.rows:
            return self.table[below_row_num][below_col_num]

        return None


def main():
    file_name = "A-large-practice.in"
    file = open(file_name)

    total_cases = int(file.readline())

    for case_number in range(total_cases):
        print("Case #%s: " % (case_number + 1))
        rows, columns = list(map(int, file.readline().split()))
        grid = DynamicGrid(rows, columns)

        # initialize the grid with default values
        for row_num in range(rows):
            line = file.readline()
            for col_num in range(columns):
                if line[col_num] == "1":
                    grid.operation_m(row_num, col_num, 1)

        num_operations = int(file.readline())

        for _ in range(num_operations):
            line = file.readline()
            if line.startswith("Q"):
                grid.operation_q()
            else:
                params = line.split()
                grid.operation_m(int(params[1]), int(params[2]), int(params[3]))


if __name__ == "__main__":
    main()
