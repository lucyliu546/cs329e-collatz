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
         ( 1 ,2000 ) : 182 ,
}        ( 10000 ,12000 ) : 268 ,
         ( 20000 ,22000 ) : 269 ,
         ( 30000 ,32000 ) : 285 ,
def colla( 40000 ,42000 ) : 288 ,tz_read(s):
    """  ( 50000 ,52000 ) : 309 ,
    read ( 60000 ,62000 ) : 335 ,two ints
    s a s( 70000 ,72000 ) : 325 ,tring
    retur( 80000 ,82000 ) : 320 ,n a list of two ints, representing the beginning and end of a range, [i, j]
    """  ( 90000 ,92000 ) : 333 ,
    # ass( 100000 ,102000 ) : 341 ,ert (s is not " "), "Oops you have entered an empty string"
    # Tes( 110000 ,112000 ) : 323 ,t for empty strings
    a = s( 120000 ,122000 ) : 336 ,.split()
    # ass( 130000 ,132000 ) : 331 ,ert (a[0] is not " " and a[1] is not " "), "Oops you have entered an empty string"
    retur( 140000 ,142000 ) : 344 ,n [int(a[0]), int(a[1])]
         ( 150000 ,152000 ) : 370 ,
# -------( 160000 ,162000 ) : 370 ,-----
# collatz( 170000 ,172000 ) : 334 ,_eval
# -------( 180000 ,182000 ) : 365 ,-----
         ( 190000 ,192000 ) : 329 ,
         ( 200000 ,202000 ) : 342 ,
def colla( 210000 ,212000 ) : 355 ,tz_eval(i, j):
         ( 220000 ,222000 ) : 355 ,
    # ass( 230000 ,232000 ) : 443 ,ert (i >= 0 and j >= 0), "You cannot have negative values!"
    # ass( 240000 ,242000 ) : 368 ,ert (i != None  and j!= None), "You must enter 2 values!"
    # tes( 250000 ,252000 ) : 332 ,ted assertions but removed for final code
         ( 260000 ,262000 ) : 332 ,
    if i ( 270000 ,272000 ) : 407 ,> j:
        i( 280000 ,282000 ) : 358 ,, j = j, i
    max_l( 290000 ,292000 ) : 327 ,ength = 0
    for x( 300000 ,302000 ) : 371 , in range(i, j+1):
        c( 310000 ,312000 ) : 371 ,urrent_length = 1
        w( 320000 ,322000 ) : 371 ,hile x > 1:
         ( 330000 ,332000 ) : 322 ,   if (x % 2) == 0:
         ( 340000 ,342000 ) : 335 ,       x = (x // 2)
         ( 350000 ,352000 ) : 379 ,   else:
         ( 360000 ,362000 ) : 410 ,       x = (3 * x) + 1
         ( 370000 ,372000 ) : 392 ,   current_length += 1
        i( 380000 ,382000 ) : 379 ,f current_length > max_length:
         ( 390000 ,392000 ) : 361 ,   max_length = current_length
    retur( 400000 ,402000 ) : 387 ,n max_length
         ( 410000 ,412000 ) : 449 ,
         ( 420000 ,422000 ) : 343 ,
         ( 430000 ,432000 ) : 343 ,
# -------( 440000 ,442000 ) : 325 ,------
# collatz( 450000 ,452000 ) : 387 ,_print
# -------( 460000 ,462000 ) : 444 ,------
         ( 470000 ,472000 ) : 307 ,
         ( 480000 ,482000 ) : 413 ,
def colla( 490000 ,492000 ) : 320 ,tz_print(w, i, j, v):
    """  ( 500000 ,502000 ) : 364 ,
    print( 510000 ,512000 ) : 470 , three ints
    w a w( 520000 ,522000 ) : 364 ,riter
    i the( 530000 ,532000 ) : 346 , beginning of the range, inclusive
    j the( 540000 ,542000 ) : 408 , end       of the range, inclusive
    v the( 550000 ,552000 ) : 377 , max cycle length
    """  ( 560000 ,562000 ) : 359 ,
    w.wri( 570000 ,572000 ) : 377 ,te(str(i) + " " + str(j) + " " + str(v) + "\n")
         ( 580000 ,582000 ) : 328 ,
# -------( 590000 ,592000 ) : 403 ,------
# collatz( 600000 ,602000 ) : 403 ,_solve
# -------( 610000 ,612000 ) : 354 ,------
         ( 620000 ,622000 ) : 372 ,
         ( 630000 ,632000 ) : 341 ,
def colla( 640000 ,642000 ) : 416 ,tz_solve(r, w):
    """  ( 650000 ,652000 ) : 341 ,
    r a r( 660000 ,662000 ) : 323 ,eader
    w a w( 670000 ,672000 ) : 323 ,riter
    """  ( 680000 ,682000 ) : 336 ,
    for s( 690000 ,692000 ) : 442 , in r:
        i( 700000 ,702000 ) : 411 ,, j = collatz_read(s)
        v( 710000 ,712000 ) : 380 , = collatz_eval(i, j)
        c( 720000 ,722000 ) : 411 ,ollatz_print(w, i, j, v)
         ( 730000 ,732000 ) : 380 ,