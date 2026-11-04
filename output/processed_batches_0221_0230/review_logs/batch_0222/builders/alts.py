# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1784575-q01":"Isosceles triangle PQR with apex P at the top and base QR; PQ and PR carry single tick marks. Point X lies on side PR, and the blue segment QX carries double ticks, as does the base QR.",
 "1784545-q01":"Triangle ABC with P on AB and Q on AC joined by a segment parallel to BC. AP is labelled 1.5, PB is labelled 3, AQ is labelled 1.3 and QC is labelled x.",
 "1784532-q01":"Left: a square of side s divided by four vertical dashed lines into five equal strips. Right: the folded result, a shaded rectangle of height s and width s/5.",
 "1784164-q01":"Two parallelograms ABCD with AC = 82 and BD = 30 drawn in blue. (i) AB = 28 and (ii) AB = 52; in each a dashed perpendicular of length 18 rises from A to the dashed extension of side DC, with a right-angle mark.",
 "1783346-q01":"Trapezoid ABCD with AB = 3 on top, DC at the bottom, AD = 3 and BC = 4. A dashed segment BT parallel to AD, of length 3, meets DC at T with DT = 3 and TC = 5; the angle TBC is marked right. A dashed altitude h from B meets DC at H with a right-angle mark.",
 "1783613-q01":"Isosceles trapezoid ABCD with AB = 3 on top and DC at the bottom. Segment FE is parallel to the bases, with F on AD and E on BC. A dashed line from A parallel to BC meets FE at G and DC at K, with DK = 1 and KC = 3.",
 "1783549-q01":"Oblique drawing of a 3 by 3 by 3 cube built from small cubes. On the three visible faces the corner cells are pink, the edge cells are blue and the face-centre cells are green; a legend says pink shows 3 faces, blue 2 faces and green 1 face.",
 "1772864-q02":"Triangle ABC with side a opposite A on BC, side b on CA and side c on AB.",
 "1780436-q01":"Equilateral triangle with side 50 divided by lines parallel to its sides into 100 small equilateral triangles of side 5; the small triangle in the bottom left corner is shaded red and labelled 5.",
 "1726380-q01":"Rectangle ABCD with AB = 6 and AD = 2 sqrt 3. From corner A the diagonal AC and the segment AP to the point P on DC with DP = 2 and PC = 4 split the right angle at A into three 30 degree angles. The pieces are shaded: ADP labelled K, APC labelled R and ABC labelled M.",
 "1782694-q01":["(i) Triangle ABC with base BC = 6 and a dimension arrow showing height 2 at the level of A; a blue square DEFG inside it has D on AB, E on AC and side GF on BC.","(ii) The same triangle with AB and AC extended beyond A as dashed lines; a blue square of side 3 has its top side ED on these extensions and its bottom side FG on BC, and A lies inside the square."],
 "1782611-q26":"Coordinate axes with the triangle with vertices (-4,0), (6,0) and (0,5). A blue line parallel to the left side meets the x-axis at -2/3 and the right side at Q; the small triangle between this line and the vertex (6,0) is shaded.",
 "1782697-q01":"Acute triangle ABC with three circles: a blue circle centred at O1 on BC touching AB and AC, with dashed radii to the two points of tangency and a dashed segment AO1; a green circle centred at O2 on CA touching AB and BC; and a red circle centred at O3 on AB touching BC and CA.",
 "1782537-q01":"Right triangle with the right angle at C, legs CA = 11 and CB = 60, and hypotenuse AB = 61, drawn to scale.",
 "1746417-q01":"Cross-section of a regular tetrahedron through apex D, vertex A and the midpoint M of the opposite edge: triangle AMD with the dashed height DG to the foot G on AM, marked with a right angle. A blue circle with centre I on DG touches AM at G and DM, with a dashed radius r to DM.",
 "1782031-q01":"A horizontal yellow ribbon of width 4 crossed by a slanted cyan ribbon of width 12; their overlap is a grey parallelogram whose horizontal sides are 15 long and whose slanted sides are 5 long.",
 "1780203-q04":"Right circular cone with apex V, base radius 3 and slant height 5. A blue ellipse marks a plane cut parallel to the base, and a dimension arrow on the right marks the distance d between the cut and the base.",
}
Q={}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
