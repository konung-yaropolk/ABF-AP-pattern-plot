import pyabf
import matplotlib.pyplot as plt

abf = pyabf.ABF('F:\\Lab Work Files\\Patch-clamp data\\TRP project\\2024_03_26_M2\\2024_03_26_0006.abf')

# use a custom colormap to create a different color for every sweep
cm = plt.get_cmap('winter')
colors = [cm(x/abf.sweepCount) for x in abf.sweepList]
# colors.reverse()

plt.figure(figsize=(8, 5))
plt.suptitle('AP firing pattern')
for sweepNumber in abf.sweepList:
    abf.setSweep(sweepNumber)
    i1, i2 = 0, int(abf.sampleRate * 1)
    dataX = abf.sweepX[i1:i2] + .0 * sweepNumber  # .025
    dataY = abf.sweepY[i1:i2] + 15 * sweepNumber  # 15
    plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)

plt.gca().axis('off')
plt.savefig('F:\\Lab Work Files\\Patch-clamp data\\TRP project\\2024_03_26_M2\\2024_03_26_0006.png')   
