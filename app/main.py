import utils
import read_csv
import charts
import pandas as pd


def run(onlyCountry=True):

  if onlyCountry:

    # get data from csv file
    data = read_csv.readCSV('./data.csv')
    # get search value from user input
    search = input('Type country => ')
    # search country
    country = utils.searchCountry(data, search)
    # if country was fund
    if (len(country) > 0):
      # set county wiht first item of list
      country = country[0]
      # get population of country
      population = utils.getDictionaryPopulationByCountry(country)
      # generate bar chart
      charts.generateBarChart(population.keys(), population.values(), country['Country/Territory'])

  else:

    # read csv
    dataFrame = pd.read_csv('data.csv')
    # input search
    key = input("Type country: ")
    # filter data frame by key at 'Continent'
    dataFrame = dataFrame[dataFrame['Continent'] == key]
    # load countries of continent
    countries = dataFrame['Country/Territory'].values
    # load percentages or world population
    percentages = dataFrame['World Population Percentage'].values
    # generate chart
    charts.generatePieChart(countries, percentages, key)

# enable execute from terminal
if __name__ == '__main__':
  run(False)
  run(True)
