import numpy as np
import matplotlib.pyplot as plt

chunks_delimiter = 16    

def plot_points(chunks, coord):

    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #ax = fig.gca()
    max_on_grid = chunks*chunks_delimiter
        

    # to draw the final chunk max on grid + chunks delimiter
    major_ticks = np.arange(0, max_on_grid + chunks_delimiter, chunks_delimiter)
    minor_ticks = np.arange(0, max_on_grid + chunks_delimiter, chunks_delimiter)

    row = int((coord[0]+1) / chunks)
    col = int((coord[0]+1) % chunks)

    #TODO remember to check for 0
    x_coord = (col-1) * chunks_delimiter
    y_coord = row * chunks_delimiter

    

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.xaxis.tick_top()
    ax.yaxis.tick_left()

    #plt.plot(x_coord, y_coord, "ro")
    #plt.grid()
    plt.show()


if __name__ == "__main__":
    chunks = input("chunks: ")
    input_coordinate = input("Enter coordinate (n, x, y): ")
    
    coordinates = map(int, input_coordinate.split(","))
    plot_points(int(chunks), list(coordinates))
