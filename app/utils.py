import read_csv


def getPopulation():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values


A = 'Hola'


def populationByContry(data, country):
  result = list(filter(lambda item: item['country'] == country, data))
  return result


def searchCountry(data, country):
  obj = list(filter(lambda item: item['Country/Territory'] == country, data))
  return obj


def getDictionaryPopulationByCountry(country):
  # define population dict
  population = dict()
  # use loop to check each attribute or key of the country
  for key, value in country.items():
    # if key have population and not have world
    if 'population' in key.lower() and 'world' not in key.lower():
      population[key[:key.find(' ')]] = int(value)

  return population


def getDataByColumn(data, colLabel, colValue):
  # define column dict
  colDict = dict()
  # loop data
  for item in data:
    # if item have [colLabel] and [colValues] keys
    if (item[colLabel] and item[colValue]):
      colDict[item[colLabel]] = item[colValue]
  return colDict


if __name__ == '__main__':
  countries = read_csv.readCSV('./app/data.csv')
  data = getDataByColumn(countries, 'Country/Territory',
                         'World Population Percentage')
  print(data)
  # country = searchCountry(countries, 'Colombia')
  # population = getDictionaryPopulationByCountry(country[0])
  # print(population)
