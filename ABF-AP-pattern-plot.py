import pyabf
import matplotlib.pyplot as plt
import settings as s


def process_abf(path, filename):

    # Перехоплення помилки відсутнього файлу
    try:
        # Відкривання abf файлу

        abf = pyabf.ABF(path + filename)

        # use a custom colormap to create a different color for every sweep
        cm = plt.get_cmap('winter')
        colors = [cm(x/abf.sweepCount) for x in abf.sweepList]
        # colors.reverse()

        plt.figure(figsize=(8, 5))
        plt.title('AP firing pattern')
        for sweepNumber in abf.sweepList:
            abf.setSweep(sweepNumber)
            i1, i2 = 0, int(abf.sampleRate * 1)
            dataX = abf.sweepX[i1:i2] + .0 * sweepNumber  # .025
            dataY = abf.sweepY[i1:i2] + 15 * sweepNumber  # 15
            plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)

        plt.gca().axis('off')
        plt.savefig(path, filename)   


    except ValueError as e:
        print(e)

    else:
        print(path + filename, '    -done')

def main():

    for i,j in s.FILES_LIST:
        process_abf(s.DIRECTORY,i)

if __name__ == '__main__':
    main()