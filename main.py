import csv
import matplotlib.pyplot as plt
import scipy.integrate as it

with open("Magnetometer.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header_row = next(reader)
    rows = []
    t = []
    time = []
    mx = []
    my = []
    mz = []
    [rows.append(row[0]) for row in reader]
    for i in rows:
        t = i.split(',')
        time.append(float(t[1]))
        mx.append(float(t[1]))
        my.append(float(t[2]))
        mz.append(float(t[3]))

    csvfile.close()

with open("Accelerometer.csv", 'r') as file:
    reader = csv.reader(file, delimiter=' ', quotechar='|')
    header_row = next(reader)
    rows = []
    t1 = []
    time1 = []
    ax = []
    ay = []
    az = []
    [rows.append(row[0]) for row in reader]
    for i in rows:
        t1 = i.split(',')
        time1.append(float(t1[0]))
        ax.append(float(t1[1]))
        ay.append(float(t1[2]))
        az.append(float(t1[3]))

    file.close()


def graph1(ax, time1):
    plt.plot(time1, ax)
    plt.grid(True)
    plt.xlabel("Time, s")
    plt.ylabel("Acceleration X, m/s^2")
    plt.title("Graph of the acceleration-time function")
    plt.show()
    return ax, time1


def graph2(ay, time1):
    plt.plot(time1, ay)
    plt.grid(True)
    plt.xlabel("Time, s")
    plt.ylabel("Acceleration Y, m/s^2")
    plt.title("Graph of the acceleration-time function")
    plt.show()
    return ay, time1


def graph3(az, time1):
    plt.plot(time1, az)
    plt.grid(True)
    plt.xlabel("Time, s")
    plt.ylabel("Acceleration X, m/s^2")
    plt.title("Graph of the acceleration-time function")
    plt.show()
    return az, time1


def integral(ax, ay, az, time1):
    velocity = it.cumtrapz(ax, time1, initial=time1[0])
    displacement = it.cumtrapz(velocity, time1, initial=time1[0])
    velocity1 = it.cumtrapz(ay, time1, initial=time1[0])
    displacement1 = it.cumtrapz(velocity1, time1, initial=time1[0])
    velocity2 = it.cumtrapz(az, time1, initial=time1[0])
    displacement2 = it.cumtrapz(velocity2, time1, initial=time1[0])
    print(displacement)
    return displacement, displacement1, displacement2


def graph4(time1, displacement):
    plt.plot(time1, displacement)
    plt.xlabel("Time, s")
    plt.ylabel("Displacement x, m")
    plt.title("Displacement vs. time")
    plt.show()
    return time1, displacement


def graph5(time1, displacement1):
    plt.plot(time1, displacement1)
    plt.xlabel("Time, s")
    plt.ylabel("Displacement y, m")
    plt.title("Graph of displacement vs. time")
    plt.show()
    return time1, displacement1


def graph6(time1, displacement2):
    plt.plot(time1, displacement2)
    plt.xlabel("Time, s")
    plt.ylabel("Displacement z, m")
    plt.title("Graph of displacement vs. time")
    plt.show()
    return time1, displacement2

def graph7(mx, displacement):
    plt.plot(displacement, mx)
    plt.xlabel("Displacement, m")
    plt.ylabel("Magnetic field, mT")
    plt.title("Graph of magnetic field vs. displacement")
    plt.show()
    return mx, displacement
def graph8(my, displacement1):
    plt.plot(displacement1, my)
    plt.xlabel("Displacement, m")
    plt.ylabel("Magnetic field, mT")
    plt.title("Graph of magnetic field vs. displacement")
    plt.show()
    return my, displacement1
def graph9(mz, displacement2):
    plt.plot(displacement2, mz)
    plt.xlabel("Displacement, m")
    plt.ylabel("Magnetic field, mT")
    plt.title("Graph of magnetic field vs. displacement")
    plt.show()
    return mz, displacement2




graph1(ax, time1)
graph2(ay, time1)
graph3(az, time1)
displacement, displacement1, displacement2 = integral(ax, ay, az, time1)
graph4(time1, displacement)
graph5(time1, displacement1)
graph6(time1, displacement2)
graph7(mx, displacement)
graph8(my, displacement1)
graph9(mz, displacement2)
