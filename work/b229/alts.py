# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1745995-q01":"Rectangle PQRS with P at the left and R at the right on a horizontal dashed diagonal, Q at the top and S at the bottom joined by the other dashed diagonal. Sides PQ and QR are labelled 20 and 15. A horizontal dimension arrow below marks 25 between P and R, and a vertical dimension arrow at the left marks 24 between the heights of S and Q.",
 "1745992-q02":"Right triangle ABC with the right angle at C, legs CA = 6 and CB = 8 and hypotenuse 10, with its blue incircle centred at I and a dashed radius r from I down to side CB.",
 "1746150-q01":"Segment AB at the bottom with parallel slanted segments AC = a at A and BD = b at B on the same side. Lines CB and DA cross at E, and the blue segment EF = c, parallel to AC, goes from E down to F on AB.",
 "1745919-q01":"Circle with centre O and an exterior point A to its right; tangent segments AB and AC touch the circle at B and C, with dashed radii OB and OC and dotted segment OA. The blue line through the midpoints D of AB and E of AC is vertical and lies entirely outside the circle.",
 "1743708-q01":"Coordinate axes with the black line 2x + y = 3 sloping down steeply and the blue line y = (1/2)x + 3 through the marked points (0,3) and (-6,0).",
 "1745435-q01":"Coordinate axes with a circle of centre O(3,3) and the blue line y = x + 2 cutting it at P(9,11) and Q(-5,-3). A dashed segment from O meets the line at right angles at H, and a dashed radius OP is labelled 10.",
 "1745417-q01":"Oblique drawing of a cube of outer edge s with a blue dashed inner cube of edge s - 2 inside it; a small arrow marks the wall thickness 1.",
 "1744022-q01":"Oblique drawing of a 5 by 5 by 5 cube divided into unit squares on its front, top and right faces, with the central square of each visible face black to show the square holes.",
 "1744022-q02":"Oblique drawing of a cube with edge 30 and a marked top corner T. A blue circle of radius 30 centred at T, with a dashed horizontal ellipse through T and a vertical radius labelled 30, outlines the sphere of points within reach of the rope.",
 "1744764-q01":"Triangle ABC with D on AB, E on BC and F on CA; the cevians AE, CD and BF meet at G. Blue mass labels 40, 24 and 9 are written next to A, B and C.",
 "1744133-q01":"Circle with centre O and perpendicular diameters AB (horizontal) and CD (vertical). From P on the circle, perpendiculars meet AB at Y and CD at Z with right-angle marks; the blue segment YZ and the dashed radius OP are the diagonals of rectangle OYPZ.",
 "1743778-q01":"Coordinate axes with triangle ABC in black, A(-4,2), B(1,2), C(-1,5), and its blue reflection A'B'C' in the y-axis. The overlapping region, triangle B'BX with X on the y-axis, is shaded gray.",
 "1743083-q01":"Regular octagon with every second vertex joined to form a blue square; the other four vertices are joined by a gray dashed square.",
 "1743083-q03":"Oblique drawing of cube ABCDEFGH with bottom face ABCD and top face EFGH. J is the midpoint of edge FB and I the midpoint of edge HD; the cross-section EJCI is shaded, with EJ and JC drawn solid blue and CI and IE dashed blue.",
 "1743083-q04":"Square ABCD with A at the bottom left, the diagonal AC and the segment from B to the midpoint E of CD meeting at F. Quadrilateral AFED is shaded gray and triangle BFC is shaded light blue.",
 "1742862-q01":"A triangle with sides labelled a, b and c, the longest side c along the bottom.",
 "1743013-q01":"Coordinate axes with triangle A(0,8), B(2,0), C(8,0) and the blue horizontal line y = t meeting AB at T and AC at U; the small triangle ATU at the top is shaded gray.",
 "1742450-q01":"Regular hexagon inscribed in a circle with centre O; dashed radii from O to two adjacent vertices and the side between them are each labelled 4.",
 "1742456-q01":"Two vertical towers on level ground 100 apart: the left tower AP of height 90 and the right tower BQ of height 150. A brown horizontal bridge joins them at height 70, and the blue rope from P to the foot B crosses the bridge at X. The left tower is marked 20 above the bridge and 70 below it.",
 "1741984-q01":"Coordinate axes with square A(1,3), B(4,4), C(5,1), D(2,0) and its dashed diagonals AC and BD crossing at the centre M.",
 "1741490-q01":"Rectangle with two small circles of radius r stacked along the left side and a large circle of radius 2r touching the top, bottom and right sides. The blue segment joining the lower small centre to the large centre is labelled 3r, with dashed horizontal leg d and vertical leg r; dotted radii r and 2r are also shown.",
 "1741603-q01":["Circle with centre O and inscribed triangle ABC with A at the top, AB = 5 and AC = 6, B and C on opposite sides of A, so that BC is long and the angle at B is acute.","Circle with centre O and inscribed triangle ABC with A at the top, AB = 5 and AC = 6, B and C both to the left of A, so that BC is short and the angle at B is obtuse."],
}
Q={
 "1741490-q01":"Rectangle of width w and height h with two congruent circles stacked along the left side, each tangent to the left side and to one of the top and bottom, and a larger circle tangent to the top, bottom and right sides and to both small circles.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
