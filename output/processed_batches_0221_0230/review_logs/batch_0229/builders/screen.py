NONMATH='Non-mathematical discussion, advice, poll, or resource request without a concrete mathematical exercise.'
EXPL='Request for an explanation of a general method or concept, with no specific problem to solve.'
_NM=['1741326','1740033','1745205','1744062','1743092','1741383','1741281','1742737','1742526','1741460','1741979','1741560','1741323','1740880','1741337']
_EX=['1742883','1742661','1744041','1742097','1740620']
EXCL={t:NONMATH for t in _NM}
EXCL.update({t:EXPL for t in _EX})
EXCL.update({
 '1746248':'"I have attached two questions": the geometry questions are only in missing attachments.',
 '1731400':'Ill-posed four-way nerf "truel": the shooting order omits one of the four players and the other players\' strategies are not specified, so the stormtrooper\'s best strategy and winning probability are not determined.',
 '1745317':'"Use the Term" marathon opening post: rules and the term "Pi" only, no problem.',
 '1745055':'The net of two squares and six equilateral triangles (with its fold lines and gluing arrows) is only in a missing figure, so the polyhedron is not determined by the text.',
 '1740579':'2009 Vestavia Hills Geometry questions 3, 8, 16, 18, 22 are only in a linked PDF.',
 '1741036':'2007 Vestavia Hills Geometry questions 17, 21, 24 are only in a linked PDF.',
 '1743564':'The answer needs the number of distinct values of r1+r2+r3+r4 over all factorisations of 69^69 into four signed integer factors (about 10^9 ordered factorisations); no reasonable solution without a computer search, and the "easy" intended answer is not stated.',
 '1741441':'"Odd function" with a non-standard definition: "how many zeroes must it have" and "how many other roots can I find from a+bi" are ill-posed (the domain is unspecified and the second question has no definite meaning).',
})
PARTIAL={
 '1731039':'Problem 2 (lanterns lit at 60 and 200 per hour) has the non-integer answer 7000/13 for a count of lanterns, and Problem 3 ("maximise the probability of being as close as possible" to a random mean) is ill-posed; only Problem 1 is used.',
}
