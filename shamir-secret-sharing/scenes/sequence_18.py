from manim import *

class Sequence18(Scene):
    
    def construct(self):
        """
        TODO: Add animation for 
        
Next, let’s briefly talk about finite fields and fields in general. The new form of arithmetic that we just invented using modular arithmetic is one of the examples of a finite field. What it means in simple words is that our new form of arithmetic has a “finite” number of numbers, which we can also call “elements”, and these “elements” satisfy all the requirements of a field. We’ll not go too much into the details of these arithmetic properties, we just need to know 2 things. First is that, the reason, we use a “finite” field is because computers can only operate on a finite set of numbers, hence it is practical to work with a finite set of numbers or elements. Second is that any form of arithmetic that you can use any set of elements to create a new form of arithmetic, and as long as they follow the rules of a “finite” field, you can use it to create a practical implementation of Shamir secret sharing.

We covered a lot in this video, so let’s do a quick recap and close with a few other applications that use the same concepts that we covered in this video.

We started with a naive way to share a secret between you and your friend where we solved 2 main problems:

1. We added randomness to our secret using modular arithmetic to achieve perfect secrecy where we don’t leak any information about the secret from just a single secret share.
2. We used graphs to represent our secret and randomness as points to create a secret sharing scheme which could handle scenarios where we can recover our secret with a fraction of the total distributed shares, which maintaining perfect secrecy.

Next, we looked into Lagrange interpolation what showed us a method to recover a secret curve given we have threshold number of points, or shares available.

Once our secret sharing scheme worked in theory, we tried to create a practical implementation for our scheme where we encountered some limitations regarding precision of fractional values due to the way computers store and operate on numbers.

Next, when we tried to update our secret sharing scheme such that it does not involve any fractional values. This time we lost the power of perfect secrecy, again due to fractional values.

Finally, we devised a secret sharing scheme using modular arithmetic where we can made sure that all operations such as addition, subtraction, multiplication, and division always lead to an integer, hence solving the precision and perfect secrecy issues altogether.

This video mostly covered how we can use concepts like Lagrange interpolation to share secrets, but there are a lot of other applications.

For example, we use it to encode and read data from CDs, QR codes, such that even if the CD gets scratched or QR codes are not fully visible, we can still recover the original data in perfect shape!
        """