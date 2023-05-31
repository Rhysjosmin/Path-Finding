
import numpy as np


def merge_close_lines(coordinates, threshold):
    merged_lines = []
    merged_indices = set()

    for i in range(len(coordinates)):
        if i in merged_indices:
            continue

        line = coordinates[i].reshape(1, 4)
        merged_line = line

        for j in range(i + 1, len(coordinates)):
            if j in merged_indices:
                continue

            other_line = coordinates[j].reshape(1, 4)
            dist = np.sqrt((line[0, 0] - other_line[0, 0]) ** 2 + (line[0, 1] - other_line[0, 1]) ** 2)

            if dist <= threshold:
                merged_line = np.vstack((merged_line, other_line))
                merged_indices.add(j)
                print('Merged')
        merged_lines.append(merged_line)

    return merged_lines


# coordinates = Lines
# threshold = 50
# merged_lines = merge_close_lines(coordinates, threshold)

# # print("Merged lines:")

# for line in merged_lines:
#     cv2.line(image,(line[0][0],line[0][1]),(line[0][2],line[0][3]),(0,255,0),2)

#     print(line)
    
# cv2.imwrite('f.jpg',image)