class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append(0)
            self.matrix.append(row)

    def get_matrix(self):
        return self.matrix

    def set_matrix(self):
        print("Enter the matrix elements row-wise, separated by spaces:")
        for i in range(self.rows):
            while True:
                try:
                    row = list(
                        map(int,
                            input(f"Enter elements for row {i+1}: ").split()))
                    if len(row) != self.columns:
                        raise ValueError(
                            f"Incorrect number of elements in row. Expected {self.columns}, got {len(row)}."
                        )
                    self.matrix[i] = row
                    break
                except ValueError as e:
                    print(f"Error: {e}")

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError(
                "Matrices must have the same dimensions for addition.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication."
            )
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.matrix[i][
                        j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def matrixTranspose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.columns):
            for j in range(self.rows):
                result.matrix[i][j] = self.matrix[j][i]
        return result

    def rank_of_matrix(self):
        """
        Calculates the rank of a matrix without using NumPy.

        Args:
            matrix: A list of lists representing the matrix.

        Returns:
            The rank of the matrix.
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        if rows > cols:
            # correct=Matrix(self.columns,self.rows)
            correct = self.matrixTranspose()
            rank = correct.rank_of_matrix()
            return rank
        #     rank=min(rows,cols)
        #     return f"0 to {rank}"
        # Perform Gaussian Elimination to reduce the matrix to row echelon form
        for i in range(rows):
            # Find the first non-zero element in the current row
            pivot = i
            while pivot < rows and self.matrix[pivot][i] == 0:
                pivot += 1
            if pivot == rows:
                continue  # Row is all zeros, move to the next row
            # Swap the current row with the pivot row
            self.matrix[i], self.matrix[pivot] = self.matrix[
                pivot], self.matrix[i]
            # Normalize the current row by dividing by the pivot element
            pivot_element = self.matrix[i][i]
            for j in range(cols):
                self.matrix[i][j] /= pivot_element
            # Eliminate elements below the pivot
            for k in range(i + 1, rows):
                factor = self.matrix[k][i]
                for j in range(cols):
                    self.matrix[k][j] -= factor * self.matrix[i][j]
        # Count the number of non-zero rows in the row echelon form
        rank = 0
        for row in self.matrix:
            if any(x != 0 for x in row):
                rank += 1
        return rank


while True:
    print()
    print("Enter 0 to Exit Program")
    print("Press 1 for Addition")
    print("Press 2 for Multiplication")
    print("Press 3 for Transpose")
    print("Press 4 for Rank of a Matrix")

    choice = int(input("Enter Your Choice : "))
    match choice:

        case 0:
            print("Thanks For Using My Program ")
            print("\t\t\t--- vikash\n")
            exit(0)

        case 1:
            a = int(input("Enter Number of Rows : "))
            b = int(input("Enter Number of Columns : "))
            print("Enter The First Matrix , ", end='')
            matrix_obj = Matrix(a, b)
            matrix_obj.set_matrix()
            print("The first matrix is:")
            matrix_obj.print_matrix()
            print("Enter The Second Matrix , ", end='')
            matrix_obj1 = Matrix(a, b)
            matrix_obj1.set_matrix()
            print("The  second matrix is:")
            matrix_obj1.print_matrix()
            add_result = matrix_obj.add(matrix_obj1)
            print("Addition result:")
            add_result.print_matrix()

        case 2:
            a = int(input("Enter Number of Rows : "))
            b = int(
                input(
                    "Enter Number of Columns of first matrix and rows of second matrix : "
                ))
            c = int(input("Enter Number of Columns : "))
            print("Enter The First Matrix , ", end='')
            matrix_obj = Matrix(a, b)
            matrix_obj.set_matrix()
            print("The first matrix is:")
            matrix_obj.print_matrix()
            print("Enter The Second Matrix : ", end='')
            matrix_obj1 = Matrix(b, c)
            matrix_obj1.set_matrix()
            print("The second matrix is:")
            matrix_obj1.print_matrix()
            multiply_result = matrix_obj.multiply(matrix_obj1)
            print("Multiplication result:")
            multiply_result.print_matrix()

        case 3:
            a = int(input("Enter Number of Rows : "))
            b = int(input("Enter Number of Columns : "))
            print("Enter The First Matrix , ", end='')
            matrix_obj = Matrix(a, b)
            matrix_obj.set_matrix()
            print("The matrix is:")
            matrix_obj.print_matrix()
            print("Transpose of the matrix is:")
            trasnsposem = matrix_obj.matrixTranspose()
            trasnsposem.print_matrix()

        case 4:
            a = int(input("Enter Number of Rows : "))
            b = int(input("Enter Number of Columns : "))
            print("Enter The First Matrix , ", end='')
            matrix_obj = Matrix(a, b)
            matrix_obj.set_matrix()
            print("The matrix is:")
            matrix_obj.print_matrix()
            print("Rank of the matrix is:", matrix_obj.rank_of_matrix())

        case _:
            print("Enter a Valid Choice Please :)")
            # exit(0)
