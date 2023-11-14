import globalVariables

file_name = "bow_drawing.txt"


def create_text_file():
    try:
        with open(file_name, 'x') as file:
            pass
    except FileExistsError:
        pass


def read_text_file():
    create_text_file()

    try:
        with open(file_name, 'r') as file:
            value = file.read()

            if test_number(value):
                globalVariables.bow_drawing = float(value)
            else:
                globalVariables.bow_drawing = 1.5

    except Exception as e:
        print(e)


def test_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
