# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1757367-q01":"Two right triangles side by side, drawn to scale with right-angle marks: legs 10 and 15 captioned area 75, and legs 5 and 20 captioned area 50.",
 "1757367-q02":"The square from (0,0) to (10,10) in the xy-plane with the band between the dashed lines y = x - 3 and y = x + 3 shaded blue and labelled |x - y| < 3. The two unshaded corner triangles are each labelled 49/2; the axes are marked 0, 3 and 10.",
 "1754235-q03":"A strip of seven squares in a row with the first, fourth and sixth squares shaded grey, no two shaded squares adjacent.",
 "1756743-q01":"Coordinate axes with the horizontal segment from (-2,4) to (8,4), equal-length tick marks on its two halves, and its midpoint M(3,4). The blue vertical line x = 3 passes through M with a right-angle mark.",
 "1756275-q01":"Coordinate axes with the points (0,2), (0,3) and (1,1). Dashed lines join (1,1) to (0,2) and to (0,3), the triangle between them is shaded blue, and a red line through (1,1) crosses the y-axis between (0,2) and (0,3).",
 "1753558-q01":"Cross-section of the cube through the centre: a square with a blue inscribed circle with centre O and a dashed radius r; below, a double arrow across the square is labelled s = 2r.",
 "1754002-q01":"Oblique drawing of tetrahedron ABCD with the hidden edge AC dashed. The interior point O is joined to A, B and C by blue dashed segments, and a red segment r runs from O down to the face ABC.",
 "1754336-q05":"Rhombus ABCD with dashed diagonals AC and BD meeting at O, half-diagonals labelled 2 (OA) and 1 (OB). A blue inscribed circle with centre O; the region of the rhombus outside the circle is shaded. A red radius r from O meets side CD at a right angle.",
 "1753987-q01":"A cone with apex V, height 10 and base radius 5, the base drawn as an ellipse with a dashed back half and a dashed radius. A blue ellipse marks a parallel cut; a blue double arrow labelled h runs from the level of V down to the cut.",
 "1751624-q01":"Equilateral triangle ABC with C at the top. Point D inside, near side AB, is joined to A and B; angle DAB is marked 10 degrees and angle DBA 20 degrees. The red segment CD and the red angle x = angle ACD are marked at C.",
 "1753684-q01":"Tall isosceles triangle ABC with apex A, the apex angle marked 34 degrees. The blue inscribed circle has centre P, joined to A and to C by dashed segments.",
 "1753584-q01":"A circle with centre O and radii OA = 6 and OB forming a 120-degree angle; chord AB is drawn and the region between the chord and the minor arc AB is shaded blue. A dashed segment from O meets AB at its midpoint M at a right angle.",
 "1753532-q01":"Three regular hexagons side by side, each with one shaded triangle on its vertices: an equilateral triangle on alternate vertices, an isosceles triangle on three consecutive vertices (120-degree angle), and a 30-60-90 triangle using a long diagonal; they are captioned accordingly.",
 "1752547-q01":["Equilateral triangle ABC with D on AB and E on AC, AD = CE = one third of the side; segments BE and CD meet at F, and triangle BCF is shaded. Caption: AD = (1/3)AB.","The same construction with AD = CE = two thirds of the side: D close to B, E close to A, segments BE and CD meeting at F near D, and triangle BCF shaded. Caption: AD = (2/3)AB."],
}
Q={}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
