# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1793187-q01":"Square ABCD with A at bottom left, E on side BC and F on side CD; segments AE, AF and EF are drawn and angle FAE is marked 45 degrees. DF and BE are labelled x and y, and a dashed construction extends CB below B to G with BG = x, joined to A by a dashed segment.",
 "1792786-q01":"Triangle ABC with centroid G on segment AX, where X lies beyond side BC. Blue segments from X parallel to the sides end at L on BC, M on CA and N on line AB extended beyond B (dashed gray extension). A red dashed line passes through N, L and M.",
 "1792730-q01":"Quadrilateral ABCD inscribed in a gray circle, with E and F on side BC. A dashed blue circle passes through A, D, E and F. Segments AE, AF, DE, DF are drawn, and the diagonals AC and DB are red.",
 "1791558-q01":"Right triangle ABC with the right angle at B, A above B and C to the right. M is the midpoint of AB with BM = 6 and N the midpoint of BC with BN = NC = 8. A blue circle passes through M, N and C, with centre O joined to C by a dashed radius.",
 "1791997-q01":"Level ground with sun rays shown as parallel orange arrows slanting down to the right. A post PT leans to the right making angle alpha with the ground; the dashed ray from T meets the ground at Q making angle beta, and the shadow PQ is drawn thick in gray. The post has length L.",
 "1791167-q06":"A large white circle of diameter 4 containing three mutually tangent blue circles, each containing three white circles, each containing three blue circles, and so on for four levels.",
 "1788394-q01":"Right isosceles triangle ABC with the right angle at B and AB = 4, and square ACDE on the other side of AC. Segment BE is red and labelled 4 sqrt 5; a dashed right triangle with legs AF = 4 along line BA extended and FE = 4 is drawn.",
 "1788973-q02":"Regular hexagon with an interior point P. Dashed blue perpendiculars from P to the six sides have lengths 4, 6, 9, 10, 8 and 5 going around, each with a right-angle mark at its foot.",
 "1789696-q01":"The x-axis and the line y = x from the origin O, with the dashed angle bisector. Three blue circles w0, w1, w2 of increasing size, each tangent to both lines and to the next circle, have their centres on the bisector.",
 "1789625-q01":"Oblique drawing of a 3 by 3 by 3 box with a blue 2 by 2 by 2 cube in its front lower left corner. The red point Z at the centre of the box lies inside the blue cube.",
}
Q={
 "1788394-q01":"Right isosceles triangle ABC with the right angle at B and AB = 4, and square ACDE built on the hypotenuse AC on the side away from B.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
