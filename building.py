import car_base
import batmobile_base, batsub_base

build_batmobile = batmobile_base.BatmobileBase('Bruce', 4, 'DC', 2, True)
print(build_batmobile.ejected_seats)
build_batmobile.ownerStatement()

build_batsub = batsub_base.BatsubBase('Mr Bruce', 0, 'DC', 2, 6)
print(build_batsub.oxygentank_hours)
