# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1728070-q01":"Isosceles triangle ABC with apex A and base BC, angle B marked 70 degrees. Segment CE runs from C to E on side AB, and the blue segment ED is parallel to BC with D on side AC. Angles ECB, DCE and DEC are each marked 35 degrees, and CD and DE carry equal tick marks.",
 "1726274-q01":"Coordinate axes with the parabolas y^2 = 4x (a = 1) and y^2 = 12x (a = 3) opening to the right, their foci marked on the x-axis. From each focus a blue segment of length k goes to a red point on its parabola, and a red dashed ellipse through the origin passes through both red points.",
 "1726675-q01":"Oblique drawing of a tetrahedron with vertices A, B, C at the base and D at the top; the hidden edge AC is dashed and the other five edges are solid.",
 "1725794-q01":"Rectangle ABCD with AB = 1 vertical on the left and BC = 2 along the bottom. A red dashed line y = x/4 runs from B to the midpoint height 1/2 on side CD, and the triangle below it, next to side BC, is shaded.",
 "1726281-q01":"Quadrilateral LMNO drawn around a circle with centre P, touching it at four blue points. The two tangent pieces at each vertex are labelled with the same letter: l at L, m at M, n at N and o at O.",
 "1726281-q02":"Oblique drawing of a long rectangular box with dimensions l, w and h, hidden edges dashed, and a red space diagonal of length 8 from the front bottom left corner to the back top right corner.",
 "1726281-q03":"Square ZENG with Z bottom left, E bottom right, N top right and G top left. A blue circle with centre O passes through Z and G and touches side EN at its midpoint M. Dashed segments: OM of length r, OH of length s - r to the midpoint H of ZG, and red OZ of length r; HZ is labelled s/2 and right angles are marked at H and M.",
 "1726281-q04":"Isosceles trapezoid ABCD with bottom base AB = 8, top base DC = 4 and slanted side BC = 6, with a blue inscribed circle touching all four sides. A dashed height of length 4 sqrt 2 drops from C to AB with a right-angle mark, cutting off a piece of length 2 next to B.",
 "1725452-q01":"Equilateral triangle ABC with a shaded blue square PQRT standing on base AB, its top corners T and R on sides AC and BC. The square's sides are labelled s, the base pieces AP and QB are labelled x, and the 60 degree angle at B is marked.",
 "1723237-q01":"Coordinate axes with points D(-5,-3), F(5,4) and D'(12,-6). Dashed segments FD (blue) and FD' (red) meet at F at a right angle, and a curved arrow shows the counterclockwise turn from FD to FD'.",
 "1723237-q02":"Coordinate axes with the line y = x - 2. Point R(-5,3) and its mirror image R'(5,-7) are joined by a dashed segment crossing the line at right angles. Dotted segments join the origin O to R' and to R''(-7,-5), and a red segment RR'' is labelled 2 sqrt 17.",
 "1725821-q01":"Square with corners (0,0) and (10,10). Red dashed lines y - x = 5 and x - y = 5 and a blue dashed line x + y = 5 cut it, and the hexagonal region between them, away from the three corners they cut off, is shaded.",
 "1725534-q01":"Right triangles ABC and DAE with A, C, D on a horizontal line, B above it and E below it. Line m (red) passes through the midpoint M of AB, the midpoint P of AD and the midpoint K of segment CE (dashed gray). The part of triangle ABC between A and line m, triangle APM, is shaded.",
 "1724620-q01":"Square ZENG with its corner triangle ZYI cut off along segment YI (the removed triangle is shaded and its sides are dashed). A blue circle with centre O touches sides EN and NG and segment YI at T; three dashed radii of length r are drawn, the one to T in red.",
 "1724972-q01":"Segment AB labelled c = 15 inside a gray dashed ellipse labelled a + b = 33 with foci A and B. Triangle ABC has C on the ellipse with sides a and b; blue dashed segments join A and B to the top point C0 of the ellipse.",
 "1724982-q01":"Triangle ABC with a blue incircle centred at I. Red radii of length r meet sides CA and CB at right angles; the pieces from C to these points of tangency are both labelled s - c, and the dashed segment CI bisects angle C, with half the angle marked C/2.",
 "1724486-q03":"Very flat isosceles triangle ABC drawn to scale, with apex A just above base BC. Points E and D on BC are joined to A; BE = 5, ED = 1 and DC = 5.",
 "1723400-q01":"Triangle ABC with area T, its three sides extended beyond each vertex by length x to points A1, A2, B1, B2, C1, C2. The hexagon A1A2B2B1C2C1 is split into the triangle, three green corner triangles at the vertices and three blue strips along the sides; the extensions inside the hexagon are dashed.",
 "1724416-q01":"Rhombus ABCD with 60 degree angles at A and C. Side DA is extended beyond A and side BC beyond C as dashed lines, and the exterior angles at A and C are marked 120 degrees in blue.",
 "1722309-q01":"Parallelogram ABCD with midpoints K of CD, L of DA, M of AB and N of BC. Blue segments AK, BL, CM and DN cross to form a smaller shaded quadrilateral in the middle.",
 "1723548-q01":"Two green regular pentagons and a blue regular decagon meeting at one point, with the angles there marked 108, 108 and 144 degrees.",
}
Q={
 "1725534-q01":"Right triangles ABC and DAE with A, C, D on a horizontal line, B above and E below. Triangle ABC has AB = 5, AC = 4, BC = 3 with the right angle at C; triangle DAE has DA = 5, AE = 3, DE = 4 with the right angle at E.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
