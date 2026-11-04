# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1709573-q01":["A large circle with centre O containing two equal circles with centres O1 and O2 that touch each other at O and touch the large circle, and a small circle above them with centre P touching all three. Blue segments form the right triangle O O2 P with the right angle at O; a dashed segment continues from P to the point T where the small circle touches the large one.", "The right triangle O O2 P drawn on its own, with the right angle at O, leg OO2 labelled 1, leg OP labelled 2 - r and hypotenuse O2P labelled 1 + r."],
 "1710185-q01":"Triangle ABC with points K and L on side AB, M the midpoint of AC and N the midpoint of AB. Blue segments MK and ML meet at a right angle at M; a red dashed segment joins N to M, and a dashed gray circle centred at N passes through K, L and M.",
 "1710138-q01":"Quadrilateral ABCD with AB = 6 at the bottom, AD = 4 on the left, BC = 2 on the right, 60 degree angles at A and B and a right angle at D. The diagonals AC and BD are blue. Dashed gray extensions of AD and BC meet at P above, with DP = 2 and CP = 4.",
 "1710125-q01":"Acute triangle ABC with a 80 degree angle marked at A. The blue altitudes from A and B meet BC at D and CA at E, with right-angle marks, and cross at H; the red angle DHE, opening towards C, is marked 126 degrees.",
 "1709775-q01":"Three squares side by side with sides 10, 24 and 26, labelled with their areas 100, 576 and 676; the last square is blue.",
 "1709625-q01":"Square ABCD inscribed in circle k with centre O. A small blue square EFGH sits on side AB with E and F on AB and G and H on the arc above AB. A red dashed radius joins O to G, and a gray dashed segment joins O to the midpoint of AB.",
 "1708983-q01":"Rhombus ABCD with gray diagonals meeting at right angles at O; OC is labelled 22.5 and OD is labelled 12. A red segment OH of length h is drawn from O perpendicular to side AB, with a right-angle mark at H.",
 "1708628-q01":"Rectangle ABCD with AB = 8 at the bottom and BC = 6 on the right. The diagonal BD is blue and dashed, and the red crease EF, with E on AB and F on CD, crosses it at its midpoint O at a right angle. Right-angle marks are at O and at C.",
 "1708456-q01":"A shaded parallelogram representing the plane Pi. A blue line l pierces the plane at a single point P, drawn dashed where it is behind the plane; a red segment of a line m lies entirely in the plane, away from P.",
 "1708321-q01":"Isosceles triangle with the two equal sides labelled a and marked with ticks, and the base labelled 2008 - 2a.",
 "1707676-q01":"Trapezoid ABCD with top base AB = 12 and bottom base CD = 18, and segment EF parallel to them near the bottom with E on AD and F on BC. A blue dashed line from A parallel to BC meets EF at P and DC at Q; EP is labelled 5 and PF is labelled 12.",
 "1707676-q04":"Side view of two frustums joined at their larger bases: small ellipses of radius 6 at the top and bottom (the bottom radius drawn and labelled 6) and a large middle ellipse whose hidden radius is labelled 16, hidden halves dashed. The height 48 of the upper frustum is a red dashed segment; a gray dashed right angle with horizontal leg 10 beside the upper slant edge l shows the slant height.",
 "1707676-q05":"Regular pentagon ABCDE with sides AB and BC labelled 2. The blue diagonals AC and BD cross at P.",
 "1706122-q01":"A right isosceles triangle: the slope is the hypotenuse from the top of a dashed vertical leg d to the end of a dashed horizontal leg d, with a right-angle mark. The blue angle of 45 degrees between the slope and the vertical is marked at the top.",
 "1705202-q01":"Coordinate axes with four hyperbola branches: blue branches of xy = k in the first and third quadrants and red branches of xy = -k in the second and fourth quadrants.",
 "1704105-q01":"Coordinate axes with origin O and a circle with centre C(k, c) and radius a. A blue dashed line from O through C meets the circle at the nearest point P1 and the farthest point P2. A red segment joins O to another point X on the circle, with a red dashed radius CX labelled a.",
}
Q={
 "1709573-q01":"A large circle containing two equal circles that touch each other at its centre and touch it, and a small circle above them, marked with a question mark, touching all three. A radius of the large circle is labelled 2 and a radius of a medium circle is labelled 1.",
 "1704985-q01":"A two-row triangle made of 9 gray unit rods forming three upward unit triangles and one downward one, with 6 black connector dots at the corners.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
