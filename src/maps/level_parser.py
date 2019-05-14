import pandas, os


def read_file(level_name):
    abs_path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '\\resources\\levels\\' + level_name + '.csv'
    return abs_path


def load_level(level_name):
    df = pandas.read_csv(read_file(level_name), header=None).values
    level_data = []
    for row in df:
        level_row = []
        for i in range(len(row)):
            value = str(row[i])
            level_row.append((int(value[0]), value[1:]))
        level_data.append(level_row)

    for r in level_data:
        print(r)

    return level_data

