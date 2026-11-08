# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1762570-q01":"Square ABCD with A at bottom left and P on the top side CD. Segments PA and PB are drawn, and the blue bisector of angle APB, with the two equal half-angles marked by ticked arcs, meets AB at Q. The red segment Q0Q1 on AB is the set of possible positions of Q.",
 "1762490-q01":["A circular pizza cut into eight 45-degree sectors by four diameters, with a red pepperoni circle inscribed in each sector, touching both straight edges and the crust.",
  "One 45-degree sector with centre O and its inscribed red circle with centre K. Dashed segment OK, labelled R - r, lies along the bisector and continues to the arc; the blue radius KT, labelled r, meets the lower edge at T at a right angle; the half-angle at O is marked 22.5 degrees."],
 "1762318-q01":"Triangle ABC with A at the top, the angle at A marked 120 degrees, and sides labelled c (AB), b (AC) and a (BC).",
 "1762096-q01":"Triangle with base BC = 16, AB = 13 and AC = sqrt 41. The dashed blue altitude h from A meets BC at H with a right-angle mark.",
 "1761304-q01":"Coordinate axes with triangle A(0,8), B(2,0), C(8,0). The red line y = mx through the origin O crosses AB at P and AC at Q, and the cut-off triangle APQ is shaded.",
 "1762011-q01":"Unit square ABCD with four quarter circles of radius 1 centred at the corners and the shaded central region inside all four. Its four corner points P1 (bottom), P2 (right), P3 (top) and P4 (left) are joined by a dashed square, and dotted segments join D to P1 and to P2.",
 "1761985-q01":"Circle with centre O and a radius labelled 9.",
 "1761719-q01":"Grid of lattice points with the segment from A(3,-2) to B(15,7); the four lattice points on it, A, (7,1), (11,4) and B, are marked in red.",
 "1761140-q01":"Square board with corners (1,1), (-1,1), (-1,-1), (1,-1) and centre O. A dashed square joins the midpoints of the sides, and four arcs of radius 1 centred at the corners bulge towards O; the four shaded regions lie between each arc and the dashed side.",
 "1761197-q01":"Oblique view of a cylinder with a red dashed vertical axis. The shaded blue rectangle from the axis to the side has bottom edge 10 (the radius) and side 9 (the height).",
 "1760504-q01":"Graph of y = x^2 + 2x + 4 with coordinate axes. Two inscribed equilateral triangles are drawn: a blue one with its bottom vertex at the parabola's vertex (-1,3) and a horizontal top side, and a red one with a vertex at (0,4).",
 "1760885-q01":"Right triangle with hypotenuse 3, vertical leg 2 opposite the angle theta at the bottom left, and horizontal leg sqrt 5; the right angle is at the bottom right.",
 "1759713-q05":"Circle with centre P and horizontal diameter AC labelled 26. Point B on the circle above A is joined to A and C, with AB = 10 and a right-angle mark at B.",
 "1759128-q01":"Circular cross-section of the clarinet with centre O and the blue water level line 2 below O; the region of the circle below the line is shaded. Dashed radii of length 4 go from O to the ends of the chord, and a dashed segment of length 2 from O down to the chord. A double arrow at the left shows that the water level is 2 above the bottom of the circle.",
 "1759128-q02":"Right triangle with the right angle at A at the bottom left, AB = 3 vertical, hypotenuse BC = x, and the angle at C marked.",
 "1759676-q136":"Regular hexagon ABCDEF with A on the right. K is the midpoint of side CD; the red segment AK is drawn, and the dashed perpendicular from K meets the dashed diagonal AD at H with a right-angle mark.",
 "1759331-q01":"Coordinate axes with the line y = 2x + 12 through A(-6,0), the point B(0,4), and the gray dashed segment AB with its blue dashed perpendicular bisector. The bisector meets the line at P, and red segments join P to A and to B.",
 "1759220-q01":"Coordinate axes with the line y = x + 1 through A(1,2) and B(3,4). A' (1,-2) is the reflection of A in the x-axis (dotted segment AA'). Red segments AP and PB meet the x-axis at P, and the red dashed segment from P to A' continues the line BP.",
}
Q={
 "1762011-q01":"Square ABCD with four quarter circles of radius equal to the side, centred at the four corners, and the central region inside all four shaded.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
