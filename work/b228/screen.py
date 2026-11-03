NONMATH='Non-mathematical discussion, advice, poll, or resource request without a concrete mathematical exercise.'
_NM=['1746578','1750456','1750534','1402853','1741267','1748960','1593497','1731437','1747564','1747526','1747312','1596315','1703193','1741349']
EXCL={t:NONMATH for t in _NM}
EXCL.update({
 '1751755':'Asks for help with Introduction to Algebra problem 6.20, but the problem itself is not stated.',
 '1751576':'"A square is randomly divided into 5 triangular sections": no distribution for the random division is given, so the probability is undefined (hopelessly ill-posed).',
 '1751354':'Says that the methods for Introduction to Algebra problems 6.7 and 6.2.6 seem the same, but neither problem is stated.',
 '1748405':'Card-pack probability question is ill-posed: the probabilities of grey and yellow cards are not given, "must get at least one grey and one yellow" and "a maximum of 13 rainbow cards" conflict with independent draws, so no consistent model exists.',
 '1749961':'Open-ended invitation to find patterns in Pascal\'s triangle; no specific problem.',
 '587127':'2013 MATHCOUNTS National Target #8 is not stated ("How do you solve this?").',
 '1746850':'Asks where a diagram-only problem comes from; the diagram is a missing image.',
 '1746868':'Pattern puzzle 2*6=20, 3*9=51, 7*5=27 with no stated rule; many rules fit, so 2*5 is not determined.',
 '1744964':'The posted degree-12 polynomial (a sextic in x^2 with pi in the coefficients) does not factor over Q(pi); its real zeros (x^2 = 1.8065...) have no hand-derivable closed form, so the "challenge" as typed is not solvable by hand (probably a typo).',
})
PARTIAL={
 '1749896':'Problem 2 (the nested radical sqrt(1+sqrt(2+sqrt(3+...)))) has no known closed form and is dropped; problem 1 (the continued fraction) is a repeat of an earlier record (aliased).',
}
