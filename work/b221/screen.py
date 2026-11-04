NONMATH='Non-mathematical discussion, advice, poll, or resource request without a concrete mathematical exercise.'
_NM=['1782607','1789023','1788347','1780197','1787885','1786918','1787678','1785915','1222101','1776792','1785968','1786201','1786863','1785810','1785522','1785514']
EXCL={t:NONMATH for t in _NM}
EXCL.update({
 '1788782':'Asks about AoPS book problem 1.3.4 (dogs that can sit and roll) without stating the problem or its numbers.',
 '314315':'"The eight points in the array shown below": the array is only in a missing image and is not described in the text.',
 '1787206':'No problem text (empty post titled "Geometry").',
 '1787207':'No problem text (empty post titled "Geometry").',
 '1588499':'"Nice or bad cards": no problem is stated.',
 '1599867':'Only asks whether the notation 7 = 1 (mod 2) is written correctly; no exercise.',
 '1786911':'Inconsistent post: the statement minimises (x+y)^2+(3x+2y)^2 but the working uses (3x+3y)^2. As stated the minimum on the circle is a root of a quartic (about 1.1313) with no elementary closed form; the other reading is trivial (minimum 0). Not repairable into the intended problem.',
 '1783140':'Garbled expression sqrt(-sqrt(3+sqrt(3+8sqrt7+4sqrt3))) with no question; the outer square root is of a negative number.',
 '1786337':'Asks for the maximum number of circles of radius 2 sqrt 6 that fit in a 65 by 120 rectangle: an optimal circle-packing problem with no elementary verifiable answer.',
 '1785508':'"Solve for x" with the equation only in a missing image (answer x = 81 given, equation unknown).',
 '1783102':'Ill-posed: two of the roots of x^3-4x^2+9x-8 are non-real, so the square roots sqrt(p-1) are ambiguous, and with principal roots the product is about 6.1418, not a rational m/n.',
 '1785210':'Vietnamese request for help ("please help my brother with this problem") with no problem text.',
 '1782881':'Impossible conditions: in every triangle with angle ABD = angle AEB (E the foot of the bisector from A, D the midpoint of AC), BP < CE, so BP = CE cannot hold (checked numerically over all triangle shapes).',
})
PARTIAL={
 '1780989':'Problem 3 (triangle with AC = AB and angle ACB = 96 degrees, D inside with angle DAB = 30 degrees, find angle ACD) is impossible (a base angle of an isosceles triangle cannot be 96 degrees) and underdetermined; only problems 1 and 2 are used.',
 '1785634':'Problem 6 is not given ("I do have a problem 6, but it is quite bad"); problems 1-5 are used.',
}
