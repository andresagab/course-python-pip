import matplotlib.pyplot as plt


def generateBarChart(labels, series, filename):

  # define figure and axis
  figure, axis = plt.subplots()
  # set type chart
  axis.bar(labels, series)
  # save chart as png file and close plt
  plt.savefig(f'./imgs/{filename}.png')
  plt.close()


def generatePieChart(labels, series, filename):
  # define figure and axis
  figure, axis = plt.subplots()
  # set type chart
  axis.pie(series, labels=labels)
  # save chart as png file and close plt
  plt.savefig(f'./imgs/{filename}.png')
  plt.close()


if __name__ == '__main__':
  labels = ['A', 'B', 'C']
  series = [10, 40, 800]
  generatePieChart(labels, series)
