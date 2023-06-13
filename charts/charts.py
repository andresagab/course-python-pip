import matplotlib.pyplot as plt


def generate_pie_chart():
    # define labels and values of chart
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    # define fig and ax with pylot
    fig, ax = plt.subplots()
    # generate pie chart
    ax.pie(values, labels = labels)
    # save pie chart as png file
    plt.savefig('pie.png')
    # close plt
    plt.close()
