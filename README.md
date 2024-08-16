**Axis-Aligned Bounding Box**
One of the simpler forms of collision detection is between two rectangles that are axis aligned — meaning no rotation.
The algorithm works by ensuring there is no gap between any of the 4 sides of the rectangles. Any gap means a collision does not exist.
*Conditions*                                        (x,y)    _________________ (x+dim,y)
condition_1 = body1.x < body2.x+body2.dimention             |                 |
condition_2 = body1.x+body1.dimention > body2.x             |                 |
condition_3 = body1.y < body2.y+body2.dimention             |                 |
condition_4 = body1.dimention+body1.y > body2.y             |                 |
                                                  (x,y+dim) |_________________| (x+dim,y+dim)
IF THE FOUR CONDITION SATISFIES THEN THEY ARE COLLIDING

**Circle-Circle Collison**
Simplest of them all.
Just Checks if the distance between the centres is lesser then the sum of the radius.
If true then they are colliding.


