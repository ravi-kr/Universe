# Credits: inventwithpython.com
"""Bitmap message, by Ravi Kumar ravikumar483@gmail.com
Displays a text message according to the provided bitmap image."""
import sys
# There are 68 periods along the top and bottom of this string:

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print('Bitmap message, by Ravi Kumar, ravikumar483@gmail.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()
    
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            print(message[i % len(message)], end = '')
    print()
