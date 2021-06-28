
import os 
import numpy as np
import matplotlib.pyplot as plt

# Constants
chunks_delimiter = 16    
directory_name = "results"


def plot_points(chunks, coord):

    
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
    plt.title("({},{},{})".format(coord[0],coord[1], coord[2]))
    plt.plot(x_coord, y_coord, "ro")
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.8)
    plt.savefig("results/{}.png".format(title))
    #plt.show()

    print("All the values have been saved on {} directory".format(directory_name) )

if __name__ == "__main__":
    # Create results directory if not exists
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        print("Directory created!")

    chunks = input("chunks: ")
    input_coordinate = input("Enter coordinate (n, x, y): ")
    
    coordinates = map(int, input_coordinate.split(","))
    plot_points(int(chunks), list(coordinates))
