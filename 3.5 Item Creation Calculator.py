#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rpayne
#
# Created:     05/11/2021
# Copyright:   (c) rpayne 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# To use, input price(in gp), dc, and roll then hit run.
price =
DC =
roll =
item_value = price*10
raw_cost = price*1/3
challenge = DC*roll
time = challenge/item_value
fail = raw_cost*1/2
if DC-3<roll<DC:
    print("No progress made.");
    print("Cost: " , raw_cost, " gold pieces.");
    print("Time Taken: 1 Week.")
if roll<DC-4:
    print("Lose " , fail , " silver.");
    print("No progress made.");
    print("Cost: " , raw_cost, " gold pieces.");
    print("Time Taken: 1 Week.")
if 2>time>.9999999999:
    print("Item Creation Successful.");
    print("Time Taken: 1 Week.");
    print("Cost: " , raw_cost, " gold pieces.")
if 3>time>1.9999999999:
    print("Item Creation Successful.");
    print("Time Taken: 3.5 Days.");
    print("Cost: " , raw_cost, " gold pieces.")
if 4>time>2.9999999999:
    print("Item Creation SUccessful.");
    print("Time Taken: 2.33 Days.");
    print("Cost: " , raw_cost, " gold pieces.")
