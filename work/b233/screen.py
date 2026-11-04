NONMATH='Non-mathematical discussion, advice, poll, advert, spam or request without a concrete mathematical exercise.'
_NM=['1721633','1721035','1720200','1720520','1720251','1720039','1706509','1719723','1719598','1703862','1718176','1718605','1717445','1638793','1235662']
EXCL={t:NONMATH for t in _NM}
EXCL.update({
 '1721631':'No content ("THX for the replies"); the question was removed.',
 '1721514':'"Cool equation" (x^2+x^3)/8*(6^3)^2 = 9x^5+6 is a quintic 9x^5-5832x^3-5832x^2+6=0 with no rational roots and no closed-form solution; hopelessly ill-posed as an exercise.',
 '1720678':'2018 MATHCOUNTS School Team #9 is only in a linked PDF; the problem is not stated.',
 '1720445':'No problem text ("Please some help!").',
 '1720332':'Economics question whose text is missing (only "Any ideas?").',
 '1717997':'Asks for a diagram for 1993 AHSME #13 given only as a link; the problem is not stated and the poster solved it.',
 '1717989':'"Expected value of (2+3x)/(4-7x) for 0<=x<=10" is ill-posed: the function has a pole at x=4/7 inside the interval, so the average does not exist (and no distribution is given).',
 '1718128':'2016 AMC 10A #11 ("find the area of the shaded region"): the figure is only in a missing image and the text does not determine it.',
 '1717642':'"Next number in the sequence" puzzles with no rule given (parts b and c are identical); no unique answer.',
 '1718146':'The problems are only in screenshots that are not included.',
 '1363136':'MATHCOUNTS State surface-area problem is only in a missing image (answer 52 quoted without the problem).',
 '1717277':'Dartboard problem: the point values of the regions are only in a missing image.',
 '1716396':'Asks for the average rate of change of a piecewise function without giving an interval; ill-posed.',
 '1716792':'Largest square inside a 5x5 square with 1x1 corners removed: the optimum (side sqrt 15, tilted, edges through the reflex corners) was found numerically, but a proof of optimality needs a long case analysis on the orientation that we cannot present as a sound self-contained solution.',
})
PARTIAL={
 '1720756':'Problem 1 (ellipse with foci (0,0), (-8,8) through (3,4), ratio of y-intercepts, answer 8) is dropped: the data give y-intercepts about -3.057 and 8.676 with irrational ratio, so the data or the answer are wrong. Problem 2 is kept (q02).',
 '1717359':'Problem 6 (cards removed if "n (mod 3)", "2n (mod 7)", "3n (mod 11)") is dropped: the conditions are garbled and the question cannot be reconstructed. Problems 1-5 are used (1, 2, 4 aliased to b232 drafts).',
 '1710109':'Problem 4 (circumradius of a regular 5-simplex) is dropped as five-dimensional geometry outside the bank\'s scope with no possible sketch; problem 6 (probability that John eats 5 donuts given an average of 4) is dropped because it only works by assuming an unstated Poisson model. Problems 1, 2, 3, 5 are used.',
}
