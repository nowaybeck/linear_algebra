import matplotlib.pyplot as plt

def draw_vector(v, title="Vector"):
    fig, ax = plt.subplots()

    ax.quiver(
        0,0,v[0],v[1],
        angles='xy',
        scale_units='xy',
        scale=1
    )

    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_xticks(range(-10,11))
    ax.set_yticks(range(-10,11))
    ax.grid()
    ax.set_title(title)

    return fig


def draw_two_vectors(v1, v2, title="Vectors"):
    fig, ax = plt.subplots()

    ax.quiver(0,0,v1[0],v1[1],color='blue',
              angles='xy',scale_units='xy',scale=1)

    ax.quiver(0,0,v2[0],v2[1],color='red',
              angles='xy',scale_units='xy',scale=1)

    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_xticks(range(-10,11))
    ax.set_yticks(range(-10,11))
    ax.grid()
    ax.set_title(title)

    return fig

# quiver() : converts displacement into an arrow.
# angles='xy' : use the actual x-y coordinate.
# scale_units='xy' : measure arrow size inn graph units.
# scale=1 : arrow length stays same, no shrinking/stretching.
#     - intuition: 'scale' is a divisor for the arrow length.
#     think of it like "drawn length = actual length/scale"
# xlim()/ylim : x-axis range and y-axis range 
# grid() : shows grid lines 
