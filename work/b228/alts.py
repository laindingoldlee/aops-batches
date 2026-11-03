# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1751255-q02":"Triangle ABC with E on side AB and F on side AC. AE and EB are marked 1 and 2, AF and FC are marked 1 and 1, and the small triangle AEF at vertex A is shaded.",
 "1751902-q01":"Coordinate axes with the steep blue line f through (-3,-10) and (3,8) and the red line g through (-3,-10) and (12,-15). A right-angle mark at (-3,-10) shows the lines are perpendicular.",
 "1751211-q01":"Triangle ABC with A(2,7), B(-2,0), C(3,-1) drawn solid. Three dashed gray triangles share vertex C: A'BC, A'B'C and A''B'C, obtained by successive reflections. A red segment joins A to A''.",
 "1751489-q01":"Triangle ABC with altitude AN to BC and a right-angle mark at N, which lies between B and C. NC = x, AN = 2x, AB = 3x, and BN and AC are both labelled square root of 5 times x.",
 "1750909-q01":"Two overlapping blue and green unit circles C1 and C2 and a long flat red ellipse through both. Ten black dots mark the intersection points: two where the circles cross and four where the ellipse crosses each circle.",
 "1750969-q03":"Two cross-sections. Left: a circle labelled sphere containing a blue rectangle with sides s and s root 2 whose corners lie on the circle, with a dashed radius x from the centre to a corner. Right: a semicircle labelled hemisphere with a blue rectangle of base s root 2 standing on the diameter and height s, its top corners on the arc, with a dashed radius x from the centre of the base to a top corner.",
 "1751050-q01":"Coordinate axes with a tilted square whose vertices are (5,4), (8,-3), (1,-6) and (-2,1). Its dashed diagonals cross at the centre M.",
 "1750568-q01":"Square ABCD with A at bottom left and side 12. Point P lies on line BA extended 4 units beyond A. The red segment PC crosses side AD at Q, dividing AD into AQ = 3 and QD = 9.",
 "1749495-q01":"Oblique drawing of a box with edges a, b and c, hidden edges dashed. A dashed blue face diagonal e runs across the bottom face from corner P, and a red space diagonal joins P to the opposite top corner Q.",
 "1749331-q01":"Two strips crossing at 30 degrees: a horizontal strip of width 2 and a slanted strip of width 2, each width marked with a double arrow. Their overlap ABCD is a shaded rhombus with sides AB and AD labelled 4 and the 30 degree angle marked at A.",
 "1748689-q01":"Trapezoid ABCD with AB parallel to DC, AB on top. E is on side AD and P is on side BC. Solid blue segments EB and DP are parallel, and dashed red segments EC and AP are also parallel.",
 "1748217-q01":"Circle with centre O and two horizontal parallel chords on opposite sides of O, the upper one with half-length 5 and the lower one with half-length 4. A dashed perpendicular through O meets them at right angles, with distances d above O and 6 - d below, and blue radii r join O to the right ends of both chords.",
 "1748217-q02":"A blue regular 20-gon labelled Kevin, 20 sides of 8 m, and a red regular 24-gon labelled Allen, 24 sides of 6 m, touching at the start point. Kevin's first side points north from the start and Allen's first side points south; Kevin's polygon lies to the west and Allen's to the east.",
 "1747731-q04":"Triangle ABC in its gray circumcircle, with circumcentre O, centroid G and orthocentre H marked on a dashed red line, with G between O and H.",
 "1747684-q01":"A rectangular garden along a shaded house wall. The fence runs along the other three sides: two sides of length y perpendicular to the house and one side of length x parallel to it.",
 "1746837-q01":"Parallelogram ABCD with blue diagonals AC and BD meeting at O. The halves of AC are labelled d1 over 2 and the halves of BD d2 over 2, and the angle theta between the diagonals is marked at O between OC and OD.",
 "1746950-q01":"Equilateral triangle with each side labelled s and a dashed altitude to the base with a right-angle mark, labelled root 3 over 2 times s. The caption reads area 435600 square feet.",
}
Q={}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
