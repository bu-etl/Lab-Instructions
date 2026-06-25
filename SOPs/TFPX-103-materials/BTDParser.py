import base64
import matplotlib.pyplot as plt
import numpy as np
import zlib 

module_so = input("Module Serial Number (e.g. RH0142): ").strip()
chip_no = input("Chip number (12 or 13): ").strip()
with open(str("BTD_Files/" + module_so + "_Chip" + chip_no + "_Deformation" ".btd"), "r", encoding="utf-8") as file:
    lines = file.readlines()

b1_def_data = []
b1_def_xsteps = []
b2_def_data = []
b2_def_xsteps = []
b1_cur_data = []
b1_cur_xsteps = []
b2_cur_data = []
b2_cur_xsteps = []
b1 = True

# Extract deformation curves
for i in range(len(lines)):
    if '<deformation xstep=' in lines[i]:
        encoded = lines[i+1].strip()
        decoded = base64.b64decode(encoded)
        decompressed = zlib.decompress(decoded[4:])
        data = np.frombuffer(decompressed, dtype=np.float64)
        if b1:
            b1_def_data.append(data)
            b1_def_xsteps.append(float(lines[i].split('"')[1]))
        else:
            b2_def_data.append(data)
            b2_def_xsteps.append(float(lines[i].split('"')[1]))

    elif '<current1 xstep=' in lines[i]:
        encoded = lines[i+1].strip()
        decoded = base64.b64decode(encoded)
        decompressed = zlib.decompress(decoded[4:])
        data = np.frombuffer(decompressed, dtype=np.float64)
        if b1:
            b1_cur_data.append(data)
            b1_cur_xsteps.append(float(lines[i].split('"')[1]))
        else:
            b2_cur_data.append(data)
            b2_cur_xsteps.append(float(lines[i].split('"')[1]))
        b1 = not b1

    

# Create time arrays
time_def_data_b1 = [
    [0 + b1_def_xsteps[j]* 1000 * i for i in range(len(b1_def_data[j]))] 
    for j in range(len(b1_def_data))
]
time_def_data_b2 = [
    [0 + b2_def_xsteps[j]* 1000 * i for i in range(len(b2_def_data[j]))] 
    for j in range(len(b2_def_data))
]
time_cur_data_b1 = [
    [0 + b1_cur_xsteps[j]* 1000 * i for i in range(len(b1_cur_data[j]))]
    for j in range(len(b1_cur_data))
]
time_cur_data_b2 = [
    [0 + b2_cur_xsteps[j]* 1000 * i for i in range(len(b2_cur_data[j]))]
    for j in range(len(b2_cur_data))
]



def make_hover_plot(time_data, def_data, title, deformation):
    fig, ax = plt.subplots()
    lines = []
    for i in range(len(def_data)):
        line, = ax.plot(time_data[i], def_data[i], label=f"Wire {i+1}")
        lines.append(line)

    # Axis labels, title, grid
    plt.xlabel("Time (ms)")
    if deformation:
        plt.ylabel("Deformation ($\mu$m)")
        plt.gca().invert_yaxis()
    else:
        plt.ylabel("Current (mA)")
    plt.title(title)
    plt.grid()

    # Annotation for hover
    annot = ax.annotate(
        "", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->")
    )
    annot.set_visible(False)

    def update_annot(line, ind):
        x_data, y_data = line.get_data()
        idx = ind["ind"][0]
        annot.xy = (x_data[idx], y_data[idx])
        annot.set_text(line.get_label())
        annot.get_bbox_patch().set_alpha(0.8)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            for line in lines:
                cont, ind = line.contains(event)
                if cont:
                    update_annot(line, ind)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    # Connect hover event
    fig.canvas.mpl_connect("motion_notify_event", hover)
    return fig

# One window for each
fig1 = make_hover_plot(time_def_data_b1, b1_def_data, "Bond 1 Deformation Curves", True)
fig2 = make_hover_plot(time_def_data_b2, b2_def_data, "Bond 2 Deformation Curves", True)
fig3 = make_hover_plot(time_cur_data_b1, b1_cur_data, "Bond 1 Current Curves", False)
fig4 = make_hover_plot(time_cur_data_b2, b2_cur_data, "Bond 2 Current Curves", False)


plt.show()