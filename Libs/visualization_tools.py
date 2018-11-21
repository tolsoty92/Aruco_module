from cv2 import line, circle

def draw_dst_pt(img, pt):
    size = 15
    pt1 = (pt[0] - size, pt[1])
    pt2 = (pt[0] + size, pt[1])
    pt3 = (pt[0], pt[1] - size)
    pt4 = (pt[0], pt[1] + size)
    line(img, pt1, pt2, (0, 50, 255), 2)
    line(img, pt3, pt4, (0, 50, 255), 2)

def draw_direction(img, marker_cntr, matker_direction_pt):
    line(img, marker_cntr, matker_direction_pt, (30, 255, 15), 1)
    circle(img, matker_direction_pt, 1, (200, 55, 255), 15)

def draw_trajectory(img, marker_cntr, destination_pt):
    line(img, marker_cntr, destination_pt, (250, 180, 140), 2)