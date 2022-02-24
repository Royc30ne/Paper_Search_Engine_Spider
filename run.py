import sys

import IEEE_Xplore_Spider as ixs
import sys

if __name__ == '__main__':
    while (True):
        print("  ========================================")
        print("  =           Paper Crawler              =")
        print("  =          Author: Royc30ne            =")
        print("  =  A Higher Place: WWW.ROYC30NE.COM    =")
        print("  =              Enjoy It!               =")
        print("  =             Ver. 0.1.0               =")
        print("  ========================================")
        print("Enter number to choose paper search engine:")
        print("1. IEEE Xplore")
        print("2. ACM Digit Library (Under Construction)")
        print("3. PubMed            (Under Construction)")
        print("4. Exit")
        search_engine = input("Pls type pure number: \n")
        if (search_engine == '4'):
            sys.exit()

        elif (search_engine == '1'):
            while (True):
                content = input("Please type your your search content: \n")
                print("You want to search: " + content + ' , Right?')
                ieee_confirm = input('Enter [y] to Confirm or back to Previous Menu: \n')
                if (ieee_confirm == "Y" or ieee_confirm == "y"):
                    ieee = ixs.XploreSpider(content)
                    ieee.operate()
                    ieee_loop = input(
                        "Do you want to continue searching? Enter [y] to continue or back to Previous Menu: \n")
                    if (ieee_loop != 'y'):
                        break
                else:
                    break

