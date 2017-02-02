__author__ = 'lucyliu'

#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {


( 1 ,5000 ) : 238 ,
( 5000 ,10000 ) : 262 ,
( 10000 ,15000 ) : 276 ,
( 15000 ,20000 ) : 279 ,
( 20000 ,25000 ) : 282 ,
( 25000 ,30000 ) : 308 ,
( 30000 ,35000 ) : 311 ,
( 35000 ,40000 ) : 324 ,
( 40000 ,45000 ) : 288 ,
( 45000 ,50000 ) : 314 ,
( 50000 ,55000 ) : 340 ,
( 55000 ,60000 ) : 322 ,
( 60000 ,65000 ) : 335 ,
( 65000 ,70000 ) : 312 ,
( 70000 ,75000 ) : 325 ,
( 75000 ,80000 ) : 351 ,
( 80000 ,85000 ) : 320 ,
( 85000 ,90000 ) : 333 ,
( 90000 ,95000 ) : 333 ,
( 95000 ,100000 ) : 328 ,
( 100000 ,105000 ) : 341 ,
( 105000 ,110000 ) : 354 ,
( 110000 ,115000 ) : 323 ,
( 115000 ,120000 ) : 349 ,
( 120000 ,125000 ) : 336 ,
( 125000 ,130000 ) : 344 ,
( 130000 ,135000 ) : 331 ,
( 135000 ,140000 ) : 344 ,
( 140000 ,145000 ) : 375 ,
( 145000 ,150000 ) : 357 ,
( 150000 ,155000 ) : 370 ,
( 155000 ,160000 ) : 383 ,
( 160000 ,165000 ) : 370 ,
( 165000 ,170000 ) : 352 ,
( 170000 ,175000 ) : 347 ,
( 175000 ,180000 ) : 347 ,
( 180000 ,185000 ) : 365 ,
( 185000 ,190000 ) : 360 ,
( 190000 ,195000 ) : 347 ,
( 195000 ,200000 ) : 360 ,
( 200000 ,205000 ) : 342 ,
( 205000 ,210000 ) : 373 ,
( 210000 ,215000 ) : 373 ,
( 215000 ,220000 ) : 386 ,
( 220000 ,225000 ) : 355 ,
( 225000 ,230000 ) : 368 ,
( 230000 ,235000 ) : 443 ,
( 235000 ,240000 ) : 350 ,
( 240000 ,245000 ) : 368 ,
( 245000 ,250000 ) : 350 ,
( 250000 ,255000 ) : 363 ,
( 255000 ,260000 ) : 345 ,
( 260000 ,265000 ) : 407 ,
( 265000 ,270000 ) : 345 ,
( 270000 ,275000 ) : 407 ,
( 275000 ,280000 ) : 389 ,
( 280000 ,285000 ) : 358 ,
( 285000 ,290000 ) : 389 ,
( 290000 ,295000 ) : 358 ,
( 295000 ,300000 ) : 371 ,
( 300000 ,305000 ) : 371 ,
( 305000 ,310000 ) : 371 ,
( 310000 ,315000 ) : 384 ,
( 315000 ,320000 ) : 353 ,
( 320000 ,325000 ) : 384 ,
( 325000 ,330000 ) : 353 ,
( 330000 ,335000 ) : 353 ,
( 335000 ,340000 ) : 366 ,
( 340000 ,345000 ) : 353 ,
( 345000 ,350000 ) : 441 ,
( 350000 ,355000 ) : 379 ,
( 355000 ,360000 ) : 379 ,
( 360000 ,365000 ) : 410 ,
( 365000 ,370000 ) : 361 ,
( 370000 ,375000 ) : 392 ,
( 375000 ,380000 ) : 423 ,
( 380000 ,385000 ) : 379 ,
( 385000 ,390000 ) : 436 ,
( 390000 ,395000 ) : 405 ,
( 395000 ,400000 ) : 374 ,
( 400000 ,405000 ) : 387 ,
( 405000 ,410000 ) : 405 ,
( 410000 ,415000 ) : 449 ,
( 415000 ,420000 ) : 387 ,
( 420000 ,425000 ) : 418 ,
( 425000 ,430000 ) : 374 ,
( 430000 ,435000 ) : 387 ,
( 435000 ,440000 ) : 400 ,
( 440000 ,445000 ) : 356 ,
( 445000 ,450000 ) : 369 ,
( 450000 ,455000 ) : 387 ,
( 455000 ,460000 ) : 356 ,
( 460000 ,465000 ) : 444 ,
( 465000 ,470000 ) : 413 ,
( 470000 ,475000 ) : 382 ,
( 475000 ,480000 ) : 382 ,
( 480000 ,485000 ) : 413 ,
( 485000 ,490000 ) : 382 ,
( 490000 ,495000 ) : 426 ,
( 495000 ,500000 ) : 395 ,
( 500000 ,505000 ) : 426 ,
( 505000 ,510000 ) : 382 ,
( 510000 ,515000 ) : 470 ,
( 515000 ,520000 ) : 439 ,
( 520000 ,525000 ) : 364 ,
( 525000 ,530000 ) : 408 ,
( 530000 ,535000 ) : 377 ,
( 535000 ,540000 ) : 377 ,
( 540000 ,545000 ) : 408 ,
( 545000 ,550000 ) : 452 ,
( 550000 ,555000 ) : 421 ,
( 555000 ,560000 ) : 390 ,
( 560000 ,565000 ) : 421 ,
( 565000 ,570000 ) : 359 ,
( 570000 ,575000 ) : 377 ,
( 575000 ,580000 ) : 390 ,
( 580000 ,585000 ) : 434 ,
( 585000 ,590000 ) : 359 ,
( 590000 ,595000 ) : 403 ,
( 595000 ,600000 ) : 372 ,
( 600000 ,605000 ) : 403 ,
( 605000 ,610000 ) : 403 ,
( 610000 ,615000 ) : 354 ,
( 615000 ,620000 ) : 447 ,
( 620000 ,625000 ) : 385 ,
( 625000 ,630000 ) : 509 ,
( 630000 ,635000 ) : 385 ,
( 635000 ,640000 ) : 416 ,
( 640000 ,645000 ) : 416 ,
( 645000 ,650000 ) : 385 ,
( 650000 ,655000 ) : 385 ,
( 655000 ,660000 ) : 429 ,
( 660000 ,665000 ) : 367 ,
( 665000 ,670000 ) : 442 ,
( 670000 ,675000 ) : 367 ,
( 675000 ,680000 ) : 385 ,
( 680000 ,685000 ) : 380 ,
( 685000 ,690000 ) : 398 ,
( 690000 ,695000 ) : 442 ,
( 695000 ,700000 ) : 367 ,
( 700000 ,705000 ) : 504 ,
( 705000 ,710000 ) : 380 ,
( 710000 ,715000 ) : 411 ,
( 715000 ,720000 ) : 380 ,
( 720000 ,725000 ) : 411 ,
( 725000 ,730000 ) : 362 ,
( 730000 ,735000 ) : 380 ,
( 735000 ,740000 ) : 424 ,
( 740000 ,745000 ) : 393 ,
( 745000 ,750000 ) : 393 ,
( 750000 ,755000 ) : 424 ,
( 755000 ,760000 ) : 362 ,
( 760000 ,765000 ) : 380 ,
( 765000 ,770000 ) : 468 ,
( 770000 ,775000 ) : 393 ,
( 775000 ,780000 ) : 437 ,
( 780000 ,785000 ) : 362 ,
( 785000 ,790000 ) : 406 ,
( 790000 ,795000 ) : 437 ,
( 795000 ,800000 ) : 468 ,
( 800000 ,805000 ) : 406 ,
( 805000 ,810000 ) : 406 ,
( 810000 ,815000 ) : 406 ,
( 815000 ,820000 ) : 450 ,
( 820000 ,825000 ) : 450 ,
( 825000 ,830000 ) : 419 ,
( 830000 ,835000 ) : 419 ,
( 835000 ,840000 ) : 525 ,
( 840000 ,845000 ) : 388 ,
( 845000 ,850000 ) : 419 ,
( 850000 ,855000 ) : 419 ,
( 855000 ,860000 ) : 388 ,
( 860000 ,865000 ) : 357 ,
( 865000 ,870000 ) : 388 ,
( 870000 ,875000 ) : 432 ,
( 875000 ,880000 ) : 432 ,
( 880000 ,885000 ) : 370 ,
( 885000 ,890000 ) : 445 ,
( 890000 ,895000 ) : 370 ,
( 895000 ,900000 ) : 370 ,
( 900000 ,905000 ) : 401 ,
( 905000 ,910000 ) : 445 ,
( 910000 ,915000 ) : 476 ,
( 915000 ,920000 ) : 432 ,
( 920000 ,925000 ) : 445 ,
( 925000 ,930000 ) : 476 ,
( 930000 ,935000 ) : 414 ,
( 935000 ,940000 ) : 507 ,
( 940000 ,945000 ) : 383 ,
( 945000 ,950000 ) : 383 ,
( 950000 ,955000 ) : 414 ,
( 955000 ,960000 ) : 352 ,
( 960000 ,965000 ) : 414 ,
( 965000 ,970000 ) : 365 ,
( 970000 ,975000 ) : 458 ,
( 975000 ,980000 ) : 383 ,
( 980000 ,985000 ) : 427 ,
( 985000 ,990000 ) : 427 ,
( 990000 ,995000 ) : 365 ,
( 995000 ,1000000 ) : 440 ,


}


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # assert (i >= 0 and j >= 0), "You cannot have negative values!"
    # assert (i != None  and j!= None), "You must enter 2 values!"
    # tested assertions but removed for final code

    if i > j:
        i,j = j, i
    max_length = 0

    # checks if i, j exists in the cache
    if (i , j ) in cache:
            max_length = cache[(i, j)]
            return max_length

    for x in range(i, j+1):
        current_length = 1

        while x > 1:
         if x in cache:
             current_length += cache[x]
             break
         else:
            if (x % 2) == 0:
                x = (x // 2)
            else:
                x = (3 * x) + 1
         current_length += 1
        if x not in cache:
                cache[x] = current_length
        if current_length > max_length:
            max_length = current_length
    return max_length

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""

