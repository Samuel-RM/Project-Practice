import matplotlib.pyplot as plt

def main():
    labels = ['A', 'B', 'C']
    valuea = [2000, 5444, 5555]

    fig, ax = plt.subplots()
    ax.pie(valuea, labels=labels)
    plt.savefig('pie.png')
    plt.close()

