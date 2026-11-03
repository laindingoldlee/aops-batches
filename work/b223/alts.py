# Alt text for every diagram: key <topic>-qNN -> string or list (several diagrams, in order)
A={
 "1779563-q01":"A regular 12-gon with centre O and its dashed gray incircle. A blue segment r runs from O to the midpoint of a side, with a right-angle mark at the side, and a dashed segment R runs from O to a vertex.",
 "1779285-q01":"Circle with centre O and points B, C at the top, D at the lower right and A at the bottom. Chords AB, BC, CD and radii OB, OC are drawn; angle ABO is marked 24 degrees, and the blue arcs mark angles OBC, OCB and OCD, each labelled x.",
 "1778586-q01":"Tall rectangle ABCD with point P near the bottom. Blue segments PA = 2, PB = 3, PC = 10 and a red segment PD. Dashed gray lines through P parallel to the sides split AB into r and s and AD into p and t.",
 "1778586-q02":"Nested figure: a circle of radius 1 (blue radius labelled 1) with an inscribed square, a circle inscribed in that square, another inscribed square, and so on for five stages. The regions between each circle and its inscribed square are shaded gray.",
 "1778486-q01":"Triangle ABC with base BC labelled 36. A red segment DE, with D on AB and E on AC, is parallel to BC and labelled x; the small triangle ADE above it is shaded light blue.",
 "1775616-q01":"Semicircle of radius 4 with centre O on its diameter. Points A and B on the arc form triangle OAB with angle theta at O and side OA labelled 4. A dashed blue height h from B meets OA at a right angle.",
 "1776426-q01":"Coordinate axes with triangle A(0,0), B(0,3), C(5,0). Point P lies inside, just below side BC. Dashed blue segments PA and PB are labelled sqrt 10 and sqrt 13, and a dashed red segment PC is labelled sqrt 5.",
 "1774223-q01":"Triangle ABC with its blue circumcircle. Dashed perpendicular bisectors of AB (through its midpoint M) and of BC (through its midpoint K), with right-angle marks, meet at the centre O. Gray segments join O to A, B and C.",
 "1772259-q03":"Obtuse triangle ABC with sides BC = 4t, CA = 3t, AB = 2t and the obtuse angle at A. Dashed blue altitudes: 3 from A to BC, 4 from B and 6 from C; the last two meet the dotted extensions of CA and BA beyond A, with right-angle marks at the feet.",
 "1772259-q04":"Square ABCD with E on side BC and F on segment DE. Segments DE, BF and a red segment AF are drawn; dashed gray lines show diagonal BD and the part FC of diagonal AC. Single ticks mark DF = BF, double ticks mark FE = BE, angle EDB is marked 15 degrees and angle DFA 75 degrees.",
 "1773745-q01":"Right triangle with the right angle at C, CA = 5 vertical, CB = 12 horizontal and AB = 13. A red segment runs from P on AB to Q on CB; a point X on it is joined by a dashed blue horizontal segment x to side CA.",
}
Q={
 "1779285-q01":"Circle with centre O and points B, C at the top, D at the lower right and A at the bottom. Chords AB, BC, CD and radii OB, OC are drawn, and angle ABO is marked 24 degrees.",
}
ALT={**{(k,'solution'):v for k,v in A.items()},**{(k,'question'):v for k,v in Q.items()}}
