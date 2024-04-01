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
        plt.title(filename[:-19] +'\nAP firing pattern')
        for sweepNumber in abf.sweepList:
            abf.setSweep(sweepNumber, channel=0)
            i1, i2 = 0, int(abf.sampleRate * 1)
            dataX = abf.sweepX[i1:i2] + .0 * sweepNumber  # .025
            dataY = abf.sweepY[i1:i2] + 15 * sweepNumber  # 15
            plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)

        # plt.xlabel(s.X_AXIS_LABEL)
        plt.gca().axis('off')


        # from matplotlib.offsetbox import AnchoredText

        # at = AnchoredText("Figure 1a",
        #                 prop=dict(size=15), frameon=True, loc='upper left')
        # at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        # plt.add_artist(at)

        # plt.text(0.5, 0.5, "Direction",
        #     ha="center", va="center", rotation=45, size=15,
        #     bbox=dict(boxstyle="rarrow,pad=0.3",
        #               fc="lightblue", ec="steelblue", lw=2))

        plt.text(0, 0,'Step Length.: {}ms\n\nUpper Level: {}pA\nLower Level: {}pA\nDelta Level: {}pA'.format(
                            s.STEP_LENGTH,
                            s.DELTA_LEVEL * abf.sweepCount,
                            s.LOWER_LEVEL,
                            s.DELTA_LEVEL,
                            ),
                        size=8.5,
                        ha="right",
                        bbox=dict(fc="w", lw=1),
                    )
        plt.savefig(path + filename + '_AP-firing.png')   


    except ValueError as e:
        print(e)

    else:
        print(path + filename, '    -done')

def main():

    for i,j in s.FILES_LIST:
        process_abf(s.DIRECTORY,i)

if __name__ == '__main__':
    main()