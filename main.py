
import os 
import csv
import numpy as np
import matplotlib.pyplot as plt

# Constants
chunks_delimiter = 16    
directory_name = "results"


def plot_points(chunks, coord):

    # I consider that if x and y were greater than 16, that should correspond to the next chunk id.
    # for example, the coordinate 8,16,16 should be 9,0,0
    if(coord[1] >= 16 or coord[2] >= 16):
        print("Wrong coordinate, please check: {}".format(coord))
        return

    if(coord[0] >= chunks*chunks):
        print("Wrong chunk id, please check: {}".format(coord[0]))
        return
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #ax = fig.gca()
    max_on_grid = chunks*chunks_delimiter
        

    # to draw the final chunk max on grid + chunks delimiter
    major_ticks = np.arange(0, max_on_grid + chunks_delimiter, chunks_delimiter)
    minor_ticks = np.arange(0, max_on_grid + chunks_delimiter, 1)

    row = int((coord[0]) / chunks)
    col = int((coord[0]) % chunks)

    x_coord = col * chunks_delimiter + coord[1]
    y_coord = row * chunks_delimiter + coord[2]
    

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.set_xlim(ax.get_xlim()[::1])
    ax.xaxis.tick_top()
    ax.yaxis.tick_left()

    title = "{}_{}_{}".format(coord[0],coord[1], coord[2])
    plt.title("Grid size (chunks): {}x{}, coordinate: ({},{},{})".format(chunks, chunks, coord[0],coord[1], coord[2]))
    plt.plot(x_coord, y_coord, "ro")
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.8)
    plt.savefig("results/{}.png".format(title))
    print("Saved: {}".format(title))
    #plt.show()

    

def read_from_file():
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for row in reader:
            if row:
                values = list(map(int, row[0].split(",")))                
                plot_points(values[0], values[1:4])

if __name__ == "__main__":
    # Create results directory if not exists
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        print("Directory created!")

    print("Processing...")
    read_from_file()
    print("All the values have been saved on {} directory".format(directory_name) ) 
