# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1765724-q01":"A horizontal segment labelled F_{k+1} = F_j + F_k. A blue segment F_j swung from its left end and a red segment F_k swung from its right end, with dashed arcs showing that their free ends can only meet at a point on the long segment.",
 "1765635-q01":"A horizontal segment of length 13. A blue segment of length 5 hinged at the left end and a red segment of length 8 hinged at the right end, with dashed arcs that meet only on the segment of length 13.",
 "1764009-q01":"Square ABCD with side DC = 4 and G on side BC with CG = 3. Rectangle DEFG has side DG = 5 and its opposite side EF passes through A. Triangle ADG is shaded, with the segment AG dashed.",
 "1764322-q01":"Triangle ABC with AB = 17 and AC = 25 and its three medians in gray meeting at the centroid G. D is the midpoint of BC, and GD is extended to H with DH = GD. Blue segments BG and GH, a blue dashed segment BH and a gray dashed segment CH form parallelogram BGCH.",
 "1765275-q01":"Isosceles trapezoid with top base AO and bottom base SP = 36. M is the midpoint of AO with AM = MO = 13. Dashed blue bisectors from S and P meet at M, red arcs mark the equal half-angles at S and P, the leg SA is labelled 13 and a dotted height of 12 is drawn from A.",
 "1765183-q01":"An equilateral triangle PQR with side s, and next to it a circle with centre M and a dashed radius r.",
 "1765109-q01":"Right isosceles triangle with C at the bottom left, A at the top and B at the right, filled with a unit grid of horizontal and vertical segments ending on the hypotenuse. One blue shaded right isosceles triangle has its right angle at a grid point labelled (i, j) and its hypotenuse on AB.",
 "1763286-q01":"A regular hexagon V0 to V5 with V0 at the bottom. A large gray sector of radius 600 surrounds V0 below the hexagon. Blue sectors of radius 480 at V1 and V5 lie on the two sides, and narrow green regions of radius 360 at V2 and V4 lie above the hexagon, clipped at the dashed line of symmetry through V0 and V3, which meets the outer arc at X. Gray dashed radii are labelled 600 and 480, and the boundary of the region at V2 is labelled 360.",
 "1764207-q01":"Unit square ABCD with E the midpoint of DC and F above E on the perpendicular from E, joined to A and B. EF and AF are labelled y, DE is labelled one half, a right-angle mark is at E, and quadrilateral ADEF is shaded.",
 "1763215-q01":["Isosceles trapezoid ABCD with legs 2, DE = 1 and the dashed altitude AE with a right-angle mark; the shorter base AB is 2 and the blue segment BE is drawn.","The same construction with a longer top base AB = 4: legs 2, DE = 1, dashed altitude AE and the blue segment BE."],
 "1763615-q01":"Coordinate axes with a blue square region (a diamond) whose vertices are (110, 5), (10, 105), (-90, 5) and (10, -95), and its centre (10, 5) marked.",
 "1763561-q01":"A horizontal line l. Above it a black circle of radius 2 with centre O1, a blue unit circle with centre O2 inside it tangent at T1, and a red unit circle with centre O3 outside it tangent at T2 directly above O1. The dashed line from T1 through O1 meets l at a 30 degree angle, a dashed segment joins O1 and T2, and the green segment O2O3 is labelled square root of 7.",
 "1762366-q148":"Coordinate axes with square WXYZ: W(2, 1), X(6, 3), Y(4, 7) and Z(0, 5). Its dashed diagonals meet at the centre (3, 4).",
 "1762187-q01":"Triangle ABC with an interior point P joined to B and C by blue segments. Red arcs mark angle ABP = 20 degrees and angle ACP = 15 degrees.",
 "1762944-q01":"A circle with centre O and an external point B on its left. Tangent segments BA and BC touch the circle at A and C, with right-angle marks at A and C between the tangents and the dashed radii OA and OC. BA is labelled 8, OA is labelled r, the dashed segment BO is drawn, and a caption states angle ABC = 120 degrees.",
 "1757873-q02":"Tall isosceles triangle ABC with apex A. D lies on AC and E on AB, and the blue segments DE and EC are drawn. Tick marks show AD, DE, EC and CB equal.",
 "1757873-q05":"A clock face with twelve tick marks. A thick hour hand of length 3 and a minute hand of length 4 meet at the centre with angle theta between them, and a red dashed segment d joins their tips.",
}
Q={
 "1764009-q01":"Square ABCD with side DC = 4 and G on side BC with CG = 3. Rectangle DEFG is drawn with E to the left of the square and its side EF passing through the vertex A.",
 "1765109-q01":"Right isosceles triangle with C at the bottom left, A at the top and B at the right, legs labelled 10, filled with horizontal and vertical segments one unit apart that end on the hypotenuse AB.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
