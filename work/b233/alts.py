# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1722305-q01":"Convex quadrilateral ABCD with diagonals AC and BD meeting at X. The four triangles around X are labelled with areas 8 (AXB), 15 (BXC), 5 (CXD) and x (DXA).",
 "1709564-q01":"Right isosceles triangle ABC with base AB, the 45 degree angle at A marked, and the altitude CH to the midpoint H of AB with a right-angle mark. Tick marks show AH, HB and HC equal.",
 "1721937-q01":"Right trapezoid ABCD with right angles at A and B, AB = 9 vertical on the left, AD = 5 on top and the long base BC at the bottom. A blue circle with centre I is tangent to all four sides.",
 "1719666-q01":"Triangle with longest side 11 at the bottom and the other two sides labelled a and b.",
 "1721378-q01":"Two triangles of nine numbered circles, four on each side. The left one has corners 1, 2, 3 and side sums 17; the right one has corners 7, 8, 9 and side sums 23.",
 "1720835-q01":"Coordinate axes with points A(0,0), B(-3,4) and C(-6,0). Triangle ABC has sides AB = 5, BC = 5 and AC = 6, with a dashed vertical from B to the x-axis.",
 "1720756-q02":"Coordinate axes with the square 0 <= x <= 5, 1 <= y <= 6, the origin O and the point (4,4) joined by a dotted segment, and the dashed blue perpendicular bisector x + y = 4. The shaded triangle with vertices (0,1), (3,1), (0,4) is the part of the square closer to O.",
 "1719574-q01":"Circle of radius 5 centred at the origin with its twelve lattice points marked. A long blue chord joins P(-4,3) to Q(3,-4) and a short red chord joins R(3,4) to S(4,3).",
 "1719242-q01":"A horizontal line l and a green line l' crossing it at P. From the point O above, dashed perpendiculars meet l at F and l' at F' with right-angle marks; the angle FOF' is marked a, and the angle between l' and l to the right of P is also marked a.",
 "1717424-q01":"Right triangle ABC with the right angle at A, B at the top and C to the right. The bisector BK meets AC at K, with the two equal angles at B marked. Double ticks mark BK and KC equal, and a dashed segment KM meets BC at its midpoint M at a right angle.",
 "1716595-q01":"A vertical tree of height 9 and, 6 units to its right, a vertical man of height 1.5. A dashed sun ray passes over the top of the tree and the top of the man to the common shadow tip X, 1.2 beyond the man.",
 "1717412-q01":"Trapezoid ABCD with long base AB = a at the bottom and short base DC = c at the top. The diagonals AC and BD meet at O at a right angle. A dashed blue segment from C parallel to BD meets the extension of AB at K, with BK = c and a right angle at C between CA and CK.",
 "1717404-q01":"Right triangle ABC with the right angle at C at the top and hypotenuse AB at the bottom. From C the altitude CH (black), the bisector CL (red) and the median CM (blue) meet AB at H, L, M in that order; the equal angles HCL and LCM are marked with ticked arcs.",
 "1717359-q05":"Right triangle ABC with the right angle at B, A above B and C to the right. The bisector AE meets BC at E and the segment BD meets AC at D, crossing AE at F. A blue circle with centre O passes through C, D, F and E, and dashed segments join O to A and to B.",
 "1710109-q03":"Triangle ABC with base AB, the median AD to the midpoint D of BC, the bisector CF from C to AB, meeting at P, and the blue line BP extended to E on AC.",
 "1715899-q01":"Triangle ABC with the median AD, its midpoint S, and the line CS meeting AB at E. A dashed blue segment from D parallel to CE meets AB at M between E and B.",
 "1716607-q01":"Coordinate axes with the blue line y = x + 1 through B(-2,-1), A(0,1) and E(5,6); a dotted vertical drops from E to x = 5 on the x-axis.",
 "1716960-q01":"Triangle ABC with the 72 degree angle at B marked, D on BC with BD = 1 and DC = 2, E the midpoint of AC, and AD and BE crossing at F. Triangle BDF is shaded grey and quadrilateral FDCE is shaded blue.",
 "1715535-q01":"Right triangle ABC with the right angle at C at the top, hypotenuse AB = 3 at the bottom and the altitude CD with a right-angle mark at D. Single ticks mark AD and BC as equal.",
}
Q={
 "1721378-q01":"Nine empty circles arranged on the sides of a triangle, four on each side with the corner circles shared.",
 "1707844-q01":"A regular pentagon drawn in grey with its five diagonals forming a star; ten dots mark the five vertices and the five crossing points of the diagonals.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
