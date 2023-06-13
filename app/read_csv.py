import csv


def readCSV(path):

  # define array for data
  data = []

  # open file with auto close
  with open(path, 'r') as file:
    # define reader with csv module
    reader = csv.reader(file, delimiter=',')
    # define header with first line content
    header = next(reader)

    # use loop to read line to line
    for row in reader:
      # define iterable, creating a tuple array
      iterable = zip(header, row)
      # generate dictionary using comprenhension
      countryDict = {key: value for key, value in iterable}
      # push object into data
      data.append(countryDict)
    return data


if __name__ == '__main__':
  readCSV('./app/data.csv')
