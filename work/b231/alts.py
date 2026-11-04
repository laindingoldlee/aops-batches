# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1734624-q01":"Bus route from home: 8 west, then 8 north, then 7 west to school, with a right-angle mark at the first turn. Dotted lines show the total westward distance 15, and the dashed blue straight path from home to school is labelled 17.",
 "1734624-q02":"A regular 17-sided polygon with vertex V at the top; the 14 diagonals from V to all vertices except V and its two neighbours are drawn in blue.",
 "1734398-q01":"Points A, C and B on one line with C between A and B; arrows above mark AC = b and CB = a, and an arrow below marks AB = a + b.",
 "1733869-q01":"Oblique drawing of a cube with hidden edges dashed. The two diagonals of the right face are drawn in red and cross at its centre, and the two space diagonals from the front left vertices to the back right vertices are drawn in blue and cross at the centre of the cube.",
 "1732087-q01":["Two intersecting circles with centres O1 and O2 on opposite sides of the vertical common chord PQ (red, length a). The dashed segment O1O2 of length b crosses PQ at a right angle; radius O1P is c (blue) and radius O2P is r (green).","A small circle with centre O1 inside part of a large circle with centre O2, both centres on the same side of the common chord PQ (red, length a). The dashed line from O2 through O1 meets PQ; O1O2 = b, radius O1P is c (blue) and radius O2P is r (green)."],
 "1732087-q02":"Equiangular hexagon ABCDEF with sides AB = 4, BC = 2, CD = 7, DE = 1, EF = 5, FA = 4. Sides AB, CD and EF are extended (dashed gray) to meet at X, Y and Z, forming a large equilateral triangle with small equilateral triangles at the corners.",
 "1657695-q06":"Coordinate axes with the triangle with vertices (1,2), (18,3) and (6,5).",
 "1657695-q10":"A rectangle of sides x and y with a shaded 2 by 2 square at each corner. Dashed fold lines bound the inner rectangle of sides x - 4 and y - 4.",
 "1657695-q12":"A triangle with sides 5 (base), 2 (left) and 4 (right).",
 "1730101-q01":"Coordinate axes with the dashed blue directrix x + y = 0 and the red parabola opening up and to the right along the line y = x, with focus F(1,1) marked.",
 "1728894-q01":"Large semicircle on a diameter with the two smaller semicircles with centres P and Q inside. Radii PL and QM (blue, perpendicular to segment LM) are drawn; H on PL with PH = 4 and HL = 2, and the dashed red segment HQ is parallel to LM. PQ is labelled 10 and QM is labelled 4; right-angle marks at L and M.",
 "1727878-q01":"Triangle ABC with E on AB near B, D on BC near C, segment ED, and the blue line from B through F on ED to G on AC near C.",
}
Q={
 "1734077-q01":"A plus-shaped figure of five unit squares (a centre square with one square on each side); each square has both of its diagonals drawn.",
 "1728894-q01":"Large semicircle on a diameter containing two smaller semicircles with centres P and Q on the diameter, tangent to each other and to the large semicircle. A line touches the left small semicircle at L and the right one at M.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
