​2​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​3​


​Copyright © 2019 Justin Skycak.​
​First edition.​


​All rights reserved. No part of this publication may be reproduced,​
​distributed, or transmitted in any form or by any means, including​
​photocopying, recording, or other electronic or mechanical​
​methods, without the prior written permission of the author, except​
​in the case of brief quotations embodied in critical reviews and​
​certain other noncommercial uses permitted by copyright law. For​
​permission requests, contact the author through the website below.​


[​www.justinmath.com​](http://www.justinmath.com/)


​4​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​5​

# ​Acknowledgements​


​A sincere thank you to Sanjana Kulkarni for her thoughtful​

​suggestions and diligent proofreading of this book.​


​6​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​7​

# ​Table of Contents​


**​Part 1​**
**​Vectors​...............................................................​13​**

​1.1​​N-Dimensional​​Space **​** ........................................ **​** 15​

_​Functions​​with​​Multiple​​Inputs​​and​​Outputs_ _**​**_ _.....................​​15​_
_​Vectors_ _**​**_ _..............................................................................._ _**​**_ _16​_
_​Scalars_ _**​**_ _...............................................................................​​18​_
_​Norm​​of​​a​​Vector...............................................................​​19​_ _**​**_

_​Algebra​​with​​Vectors_ _**​**_ _.........................................................​​20​_
_​Exercises............................................................................​​21​_ _**​**_
​1.2​​Dot​​Product​​and​​Cross​​Product **​** ......................... **​** 25​

_​Dot​​Product.......................................................................​​25​_ _**​**_
_​Cross​​Product....................................................................._ _**​**_ _**​**_ _28​_
_​Geometric​​Interpretation​​of​​Cross​​Product........................_ _**​**_ _**​**_ _29​_
_​Exercises............................................................................​​31​_ _**​**_
​1.3​​Lines​​and​​Planes **​** ...............................................​​35​

_​Finding​​the​​Equation​​of​​a​​Line_ _**​**_ _...........................................​​36​_
_​Checking​​Whether​​a​​Point​​is​​on​​a​​Line_ _**​**_ _..............................​​36​_
_​The​​Equation​​of​​a​​Plane....................................................._ _**​**_ _**​**_ _37​_
_​Finding​​a​​Plane​​Given​​a​​Point​​and​​Perpendicular​​Vector..._ _**​**_ _**​**_ _39​_
_​Finding​​a​​Plane​​Given​​Three​​Points_ _**​**_ _...................................​​40​_
_​Exercises............................................................................​​43​_ _**​**_
​1.4​​Span,​​Subspaces,​​and​​Reduction **​** ......................​​45​

_​Subspaces​​of​​Two-Dimensional​​Space...............................​​46​_ _**​**_
_​Subspaces​​of​​N-Dimensional​​Space...................................​​46​_ _**​**_
_​Independence....................................................................​​48​_ _**​**_
_​Maximum​​Number​​of​​Independent​​Vectors_ _**​**_ _......................​​49​_
_​Reduction_ _**​**_ _..........................................................................._ _**​**_ _51​_


​8​ ​Justin Skycak |​ **​Linear Algebra​**


_​Exercises............................................................................​​55​_ _**​**_
​1.5​​Elimination​​as​​Vector​​Reduction **​** ....................... **​** 57​

_​Interpreting​​Elimination​​as​​Vector​​Reduction_ _**​**_ _....................​​58​_
_​Exercises............................................................................​​61​_ _**​**_
**​Part 2​**
**​Volume​..............................................................​​63​**

​2.1​​N-Dimensional​​Volume​​Formula **​** ....................... **​** 65​

_​Volume​​Enclosed​​by​​N-Dimensional​​Vectors_ _**​**_ _......................_ _**​**_ _65​_
_​Volume​​of​​a​​Parallelogram_ _**​**_ _................................................​​68​_
_​Volume​​of​​a​​Parallelepiped_ _**​**_ _................................................_ _**​**_ _69​_
_​N-Dimensional​​Volume​​Formula_ _**​**_ _........................................_ _**​**_ _71​_
_​Sanity​​Checks_ _**​**_ _.....................................................................​​73​_

_​Final​​Remarks_ _**​**_ _....................................................................​​77​_
_​Exercises............................................................................​​77​_ _**​**_
​2.2 Volume as the Determinant of a​
​Square​​Linear​​System **​** .............................................​​79​

_​Linear​​Systems​​as​​Vector​​Equations_ _**​**_ _..................................._ _**​**_ _79​_
_​The​​Determinant................................................................_ _**​**_ _**​**_ _81​_
_​Exercises............................................................................​​84​_ _**​**_
​2.3 Shearing, Cramer’s Rule, and​
​Volume​​by​​Reduction **​** .............................................. **​** 87​

_​Shearing_ _**​**_ _............................................................................​​87​_
_​Cramer’s​​Rule​​in​​Two​​Dimensions_ _**​**_ _......................................_ _**​**_ _88​_
_​Cramer’s​​Rule​​in​​N​​Dimensions_ _**​**_ _.........................................._ _**​**_ _91​_
_​Volume​​by​​Reduction_ _**​**_ _.........................................................​​92​_
_​Exercises............................................................................​​95​_ _**​**_
​2.4​​Higher-Order​​Variation​​of​​Parameters **​** ..............​​97​

_​Second-Order​​Variation​​of​​Parameters.............................._ _**​**_ _**​**_ _97​_
_​Higher-Order​​Variation​​of​​Parameters..............................​​99​_ _**​**_
_​Demonstration_ _**​**_ _................................................................._ _**​**_ _101​_
_​Exercises..........................................................................​​106​_ _**​**_
**​Part 3​**


​Justin Skycak |​ **​Linear Algebra​** ​9​


**​Matrices​...........................................................​107​**

​3.1 Linear Systems as Transformations​
​of​​Vectors​​by​​Matrices **​** ..........................................​​109​

_​Matrices​​of​​Column​​Vectors_ _**​**_ _............................................._ _**​**_ _109​_
_​Matrices​​of​​Row​​Vectors_ _**​**_ _..................................................​​111​_
_​Matrix​​Multiplication_ _**​**_ _......................................................._ _**​**_ _113​_
_​Geometric​​Intuition_ _**​**_ _.........................................................​​116​_
_​Exercises..........................................................................​​118​_ _**​**_
​3.2​​Matrix​​Multiplication **​** ......................................​​121​

_​General​​Procedure..........................................................._ _**​**_ _**​**_ _121​_
_​Case​​of​​Rectangular​​Matrices.........................................._ _**​**_ _**​**_ _123​_
_​Criterion​​for​​Multiplication_ _**​**_ _..............................................​​124​_
_​Non-Commutativity_ _**​**_ _.........................................................​​125​_

_​Diagonal​​Matrices...........................................................​​127​_ _**​**_
_​Exercises..........................................................................​​129​_ _**​**_
​3.3​​Rescaling,​​Shearing,​​and​​the​​Determinant.....​​131​ **​**

_​Rescaling​​Matrices..........................................................._ _**​**_ _**​**_ _131​_
_​Shearing​​Matrices...........................................................​​133​_ _**​**_
_​Decomposing​​into​​Rescalings​​and​​Shears........................_ _**​**_ _**​**_ _135​_
_​Determinant​​of​​a​​Product................................................​​138​_ _**​**_
_​Meaning​​of​​Negative​​Determinant.................................._ _**​**_ _**​**_ _139​_
_​Exercises..........................................................................​​141​_ _**​**_
​3.4​​Inverse​​Matrices **​** .............................................​​143​

_​Verifying​​an​​Inverse​​Matrix_ _**​**_ _.............................................​​143​_
_​Procedure​​for​​Finding​​the​​Inverse...................................._ _**​**_ _**​**_ _144​_
_​Left​​and​​Right​​Inverses....................................................​​145​_ _**​**_
_​Non-Invertible​​Matrices..................................................._ _**​**_ _**​**_ _146​_
_​Criterion​​for​​Invertibility_ _**​**_ _..................................................​​147​_
_​Faster​​Method​​for​​Computing​​Inverses...........................​​148​_ _**​**_
_​Formula​​for​​the​​Inverse​​of​​a​​2-by-2​​Matrix_ _**​**_ _......................_ _**​**_ _150​_
_​Exercises..........................................................................​​150​_ _**​**_
**​Part 4​**
**​Eigenspace​.......................................................​​153​**


​10​ ​Justin Skycak |​ **​Linear Algebra​**


​4.1 Eigenvalues, Eigenvectors, and​
​Diagonalization **​** .....................................................​​155​

_​Inverse​​Shearings​​and​​Rescalings_ _**​**_ _....................................​​156​_
_​Diagonalized​​Form..........................................................._ _**​**_ _**​**_ _157​_
_​Eigenvectors​​and​​Eigenvalues_ _**​**_ _.........................................​​159​_
_​Demonstration​​of​​Diagonalization_ _**​**_ _..................................​​160​_
_​More​​Complicated​​Case_ _**​**_ _..................................................._ _**​**_ _165​_
_​Eigenvalues​​with​​Multiple​​Eigenvectors_ _**​**_ _..........................​​170​_
_​Non-Diagonalizable​​Matrices..........................................​​172​_ _**​**_
_​Exercises..........................................................................​​174​_ _**​**_
​4.2 Recursive Sequence Formulas via​
​Diagonalization **​** .....................................................​​177​

_​Recursive​​Sequences........................................................_ _**​**_ _**​**_ _177​_

_​Finding​​a​​Closed-Form​​Expression_ _**​**_ _...................................​​178​_
_​Case​​when​​Approximation​​is​​Required............................​​183​_ _**​**_
_​Exercises..........................................................................​​186​_ _**​**_
​4.3​​Generalized​​Eigenvectors​​and​​Jordan​​Form.... **​** **​** 187​

_​Patterns​​in​​Powers...........................................................​​187​_ _**​**_
_​Jordan​​Form....................................................................._ _**​**_ _**​**_ _189​_
_​Procedure​​for​​Finding​​a​​Jordan​​Form..............................​​190​_ _**​**_
_​Demonstration_ _**​**_ _................................................................._ _**​**_ _192​_
_​Exercises..........................................................................​​203​_ _**​**_
​4.4 Matrix Exponential and​
​Systems​​of​​Linear​​Differential​​Equations **​** ..............​​205​

_​Converting​​to​​Matrix​​Form..............................................​​205​_ _**​**_
_​Matrix​​Exponential_ _**​**_ _..........................................................​​206​_
_​Demonstration_ _**​**_ _................................................................._ _**​**_ _212​_
_​Exercises..........................................................................​​215​_ _**​**_
**​Solutions​**
**​to​​Exercises​......................................................​​217​**

​Part​​1 **​** ....................................................................​​219​

​Part​​2 **​** ....................................................................​​223​


​Justin Skycak |​ **​Linear Algebra​** ​11​


​Part​​3 **​** ....................................................................​​227​

​Part​​4 **​** ....................................................................​​235​


​12​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​13​

# ​Part 1​ **​Vectors​**


​14​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​15​

## **​1.1 N-Dimensional Space​**


**​N-dimensional space​** ​consists of points that have N​​components.​

​For example,​ ​is the origin in 2-dimensional space,​ ​is​

​the origin in 3-dimensional space, and​ ​is the origin​​in​
​4-dimensional space.​


​Similarly, the points​ ​,​ ​,​ ​are the corners of a​​triangle​

​in 2-dimensional space, the points​ ​,​ ​,​ ​,​

​are the corners of a tetrahedron in 3-dimensional​​space,​

​and the points​ ​,​ ​,​ ​,​ ​,​

​are the corners of a “hypertetrahedron” in 4-dimensional​
​space.​

## **​Functions with Multiple Inputs and Outputs​**


​We’re used to seeing single variables as inputs and outputs to​
​functions, but functions can really take any number of variables as​
​input and produce any number of variables as output.​


​For example, the function​ ​takes two input​
​variables, and adds them to produce a single output variable. Thus,​
​it maps points in 2-dimensional space onto points in 1-dimensional​
​space.​


​16​ ​Justin Skycak |​ **​Linear Algebra​**


​Similarly, the function​ ​takes two​
​input variables and produces four output variables: the sum,​
​difference, product, and quotient of the inputs. Thus, it maps points​
​in 2-dimensional space onto points in 4-dimensional space.​


​Lastly, the function​
​takes​ ​input variables and produces​ ​output variables,​​which​
​are just the first​ ​input variables multiplied by​​their indices. Thus,​
​it maps points in N-dimensional space onto points in M-dimensional​
​space.​

## **​Vectors​**


​Points in N-dimensional space consist of numbers, but can also be​
​thought of as manipulable entities in their own right, called​ **​vectors​** .​
​When we think of points as vectors, we cease to think of them as​
​fixed points in space. Instead, we think of them as displacements​
​through space.​


​For example, the vector​ ​can represent the displacement​​from​

​the point​ ​to the point​ ​-- but it can also represent​​the​

​displacement from​ ​to​ ​, or​ ​to​ ​, or any​

​other point​ ​to​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​17​


​Vectors can be added component-wise, and adding a sequence of​
​vectors together yields a net displacement through all the vectors​
​combined, starting each vector where the previous one ends.​


​18​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Scalars​**


​Vectors can also be multiplied by regular numbers called​ **​scalars​** .​
​Multiplying a vector by a scalar has the effect of rescaling a vector to​
​become shorter or longer, depending on the magnitude of the​
​scalar.​


​If the scalar is negative, then the vector also flips direction, in​
​addition to being rescaled by the magnitude of the scalar.​


​Justin Skycak |​ **​Linear Algebra​** ​19​

## **​Norm of a Vector​**


​In two dimensions, a vector’s length, called its​ **​norm​**,​​can be​
​obtained using the Pythagorean theorem:​


​In general, the norm of a vector can be computed by extending the​
​Pythagorean theorem to higher dimensions.​


​20​ ​Justin Skycak |​ **​Linear Algebra​**


​To see that this definition of the norm is compatible with the idea​
​that scalar multiplication rescales a vector, observe that the norm of​
​a scaled vector is equal to the product of the scalar and the norm of​
​the unscaled vector.​

## **​Algebra with Vectors​**


​Lastly, expressions involving multiple vector operations follow the​
​standard rules of arithmetic, and equations involving vector​
​variables follow the standard rules of algebra.​


​Justin Skycak |​ **​Linear Algebra​** ​21​


​We can also use algebra to solve for unknown components of​
​vectors.​


|​Exercises​|Col2|
|---|---|
|​For each functon, list the dimensionalites of the input space and​<br>​the output space.​|​For each functon, list the dimensionalites of the input space and​<br>​the output space.​|
|||
|||


​22​ ​Justin Skycak |​ **​Linear Algebra​**

|​Perform the indicated vector operations.​|Col2|
|---|---|
|||
|||
|||
|||
|||



​Solve for the unknown variable.​


​Justin Skycak |​ **​Linear Algebra​** ​23​


​24​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​25​

## **​1.2 Dot Product and Cross Product​**


​We know how to multiply a vector by a scalar, but what does it​
​mean to multiply a vector by another vector?​


​The two most common interpretations of vector multiplication are​
​the​ **​dot product​**, and for vectors in 3 dimensions,​​the​ **​cross product​** .​

## **​Dot Product​**


​The​ **​dot product​** ​is computed as the sum of products​​of​
​components.​


​First of all, notice that the dot product of a vector with itself is just​
​the vector’s norm, squared.​


​Also notice that the dot product can distribute over sums of vectors,​
​just like multiplication.​


​26​ ​Justin Skycak |​ **​Linear Algebra​**


​One can also verify that the dot product behaves like multiplication​

​in other ways -- for example for two vectors​

​and​ ​and any scalar​ ​we have​

​and​ ​.​

## **​Geometric Interpretation of Dot Product​**


​Using the law of cosines on a triangle whose sides are formed by the​
​vectors​ ​,​ ​, and​ ​, we can find a geometric interpretation​​of​
​the dot product:​


​,​


​where​ ​is the angle between the two vectors​ ​and​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​27​


​One interesting consequence of this formula is that perpendicular​
​vectors have a dot product of zero: the angle between​

​perpendicular vectors is​ ​, and​ ​.​


​28​ ​Justin Skycak |​ **​Linear Algebra​**


​Even if the dot product is not zero, we can still use it to compute the​
​angle between the two vectors.​

## **​Cross Product​**


​For 3-dimensional vectors, we also have another interpretation of​
​vector multiplication called the​ **​cross product​** . The​​cross product is​
​given by​


​.​


​Using the above definition, one can verify that the cross product​

​distributes over sums and satisfies​
​for any scalar​ ​.​


​However, when the two vectors in a cross product are interchanged,​
​the result changes sign:​ ​. This is a key difference​
​between the cross product and the dot product.​


​Justin Skycak |​ **​Linear Algebra​** ​29​

## **​Geometric Interpretation of Cross Product​**


​Like the dot product, the cross product also has a geometric​
​interpretation:​


​This is similar to the geometric interpretation of the dot product,​
​except we have​ ​instead of​ ​, and we are talking​​about the​
​norm of the vector resulting from the cross product.​


​As a result, the cross product​ ​represents a vector​​whose norm​
​is equal to the area enclosed by the parallelogram that has​ ​and​
​as sides. Moreover, the cross product produces a vector that is​
​perpendicular to the vectors​ ​and​ ​.​


​30​ ​Justin Skycak |​ **​Linear Algebra​**


​To understand why​ ​, we can begin by squaring​
​both sides of the equation and expressing the right-hand side using​
​the dot product.​


​Now, we expand out the right hand side using​ ​and​

​. We find that some terms cancel, and the remaining​
​terms can be rearranged into the square of the norm of the cross​
​product.​


​Justin Skycak |​ **​Linear Algebra​** ​31​


|​Exercises​|Col2|
|---|---|
|​Evaluate the following vector expressions.​|​Evaluate the following vector expressions.​|
|||
|||
|||
|||
|||
|||
|||


​32​ ​Justin Skycak |​ **​Linear Algebra​**


​Solve for​ ​.​


|​Use the dot product to find the angle​ ​between the​​two vectors.​|Col2|
|---|---|
|||
|||


​Justin Skycak |​ **​Linear Algebra​** ​33​


|​Use the cross product to find the area contained by each​<br>​parallelogram whose sides are given as vectors.​|Col2|
|---|---|
|||
|||


​34​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​35​

## **​1.3 Lines and Planes​**


​A line starts at an initial point and proceeds straight in a constant​
​direction. Thus, we can write the equation of a line as​


​where​

​●​ ​is the initial point,​

​●​ ​is the constant direction in which​
​the line travels, and​

​●​ ​is the point reached by​
​traveling​ ​units away from​ ​in the direction of​ ​.​


​(Though​ ​is actually a vector, we can also refer​​to it as the point​
​where the vector lands when the vector is placed at the origin.)​


​36​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Finding the Equation of a Line​**


​For example, to compute the line between the points​

​and​ ​in 4-dimensional space, we can start by computing​
​the direction​ ​as the difference between the two​​points:​


​Taking​ ​as our initial point, then, we can express​​the​
​line as​


​.​


​If we wanted to find another point on the line, we could substitute​
​another value for​ ​, say,​ ​.​

## **​Checking Whether a Point is on a Line​**


​If we wanted to check whether the point​ ​is on the​

​line, we could substitute this point for​ ​and try​​to solve for​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​37​


​Setting first components equal, we find​ ​, which implies​​that​

​. But equating second components yields​ ​, which​
​implies that​ ​. So, there is no solution that matches​​all pairs of​

​components, and consequently the point​ ​is not​
​on the line.​


​However, we can verify that the point​ ​is on the​​line​
​using the same method.​


​Equating first components yields​ ​which is valid​​for​ ​;​
​equating second components yields​ ​which is also​​valid​
​for​ ​; equating third components yields​ ​which is​​valid for​
​all choices of​ ​; and equating fourth components yields​

​which is also valid for​ ​. Thus the point​ ​is on​​the​

​line because it is simply​ ​evaluated at​ ​.​

## **​The Equation of a Plane​**


​Now, let’s talk about how to write the equation of a plane in​
​N-dimensional space. A plane can be visualized as a flat sheet that​


​38​ ​Justin Skycak |​ **​Linear Algebra​**


​makes a right angle with some particular vector. Thus, a plane just​
​consists of all vectors through some point in the plane, that are​
​perpendicular to a single vector.​


​their dot product must be zero:​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​39​


​a constant, so we can simply call it​ ​. Thus, we have the general​
​equation for a plane:​


​Here,​ ​is a vector that is perpendicular to the plane,​ ​are points​

​on the plane, and​ ​is some constant. Writing​

​and​ ​, we can expand out the general equation​
​for a plane into an equation consisting only of scalars:​

## **​Finding a Plane Given a Point and​** **​Perpendicular Vector​**


​For example, to compute the plane that passes through the point​

​and has a perpendicular vector of​ ​, we can start​
​by setting up the equation with the perpendicular vector​
​substituted.​


​To solve for​ ​, we can simply substitute the point​ ​for​ ​and​
​take the dot product.​


​40​ ​Justin Skycak |​ **​Linear Algebra​**


​Then, we can substitute for​ ​and expand out the dot product in the​
​initial equation.​


​Now, suppose we have an equation for a plane, and we want to find​
​the perpendicular vector.​


​To do this, we can simply organize the equation and convert it to the​
​vector equation of the plane, using the dot product.​


​The perpendicular vector is just the first vector in the dot product,​

​.​

## **​Finding a Plane Given Three Points​**


​Lastly, suppose that we want to find the equation of the plane that​

​contains the three points​ ​,​ ​, and​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​41​


​To start off, we can find two vectors within the plane by starting at​

​one of the points, say​ ​, and computing the displacement​
​vectors to the other two points:​


​These displacement vectors are within the plane, so if we can find a​
​vector that is perpendicular to these displacement vectors, then we​
​will have a vector that is normal to the plane.​


​Since these displacement vectors are 3-dimensional, we can​
​compute their cross product, which yields a perpendicular vector.​


​42​ ​Justin Skycak |​ **​Linear Algebra​**


​for some constant​ ​. To find the value of​ ​, we can simply​

​substitute one of the points in the plane, say,​ ​.​


​Thus, the equation of the plane is​


​which can be simplified to​


​.​


​Looking back, we could have saved some work by using the vector​

​instead of the displacement vector​ ​, since​

​follows the same direction (it’s just half as long).​


​The normal vector resulting from the cross product would then have​

​been​ ​, which is the normal vector in the fully simplified​
​equation of the plane.​


​(The vector​ ​points in the same direction as the​​original​

​normal vector​ ​; it’s just half as long.)​


​Justin Skycak |​ **​Linear Algebra​** ​43​

## **​Exercises​**


​Compute the equation of the line that passes through the given​
​points.​


​Check whether the given point​ ​is on the given line.​​If so,​

​determine the value of​ ​for which​ ​.​


​44​ ​Justin Skycak |​ **​Linear Algebra​**


​Write the equation of the plane that contains the given point​ ​and​
​is perpendicular to the given normal vector​ ​.​


​Write the equation of the plane that contains the three given points.​


​Justin Skycak |​ **​Linear Algebra​** ​45​

## **​1.4 Span, Subspaces, and Reduction​**


​The​ **​span​** ​of a set of vectors consists of all vectors​​that can be made​
​by adding multiples of vectors in the set.​


​For example, the span of the set​ ​is just the entirety​

​of the 2-dimensional plane: any vector​ ​in this plane​​can be​

​made by adding​ ​. For instance,​ ​can be​

​written as​ ​.​


​Similarly, the span of the set​ ​is also the entirety​​of​

​the 2-dimensional plane: any vector​ ​in this plane​​can be made​


​by adding​ ​. This is a little less obvious,​

​but it’s true: for example,​ ​can be written as​

​.​


​The span of the set​ ​, however, is just a 1-dimensional​
​line within the 2-dimensional plane: it contains only vectors of the​

​form​ ​, where​ ​is a constant. To see why this is,​​observe​
​what happens when we try to add multiples of the vectors:​


​46​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Subspaces of Two-Dimensional Space​**


​The span of​ ​is a 1-dimensional line within the​
​2-dimensional plane. So, we say that the span forms a 1-dimensional​
**​subspace​** ​of the 2-dimensional plane.​


​In 2 dimensions, it turns out that any set of two vectors that are​
​multiples of one another will span a line, and any set of two vectors​
​that are NOT multiples of one another will span the entire space.​


​For example, the set​ ​spans a line because​

​. On the other hand, the set​
​spans the entire space because the vectors cannot be written as​
​multiples of each other.​


​But just because two vectors are multiples, doesn’t mean they can’t​
​be included in a set that spans the space. For example, the set​

​spans only a line, but if we add include a third​

​vector​ ​that is not a multiple of the original two​​vectors, then​

​the set​ ​spans the entire plane.​

## **​Subspaces of N-Dimensional Space​**


​Now, let’s generalize these ideas to N dimensions. It might be​
​tempting to think that in general, a set of vectors will span the entire​
​space provided there are some three vectors that aren’t multiples of​
​one another. But this isn’t always true.​


​Justin Skycak |​ **​Linear Algebra​** ​47​


​For example, consider the set​ ​. None​
​of these vectors are multiples of each other, but there is no way to​
​combine the vectors to reach a point whose third component is not​
​zero.​


​The issue here is that the third vector is the sum of the first two​
​vectors. As a result, the third vector is redundant -- we can already​
​reach any point using the first two vectors, that we can reach using​
​the third vector. The set, then, has the same span as the set of just​
​the first two vectors. It covers just a plane, a 2-dimensional​
​subspace of 3-dimensional space.​


​any points above or below the plane, by adding multiples of vectors​
​in the set.​


​48​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Independence​**


​In general, the dimension of the span of a set of vectors is equal to​
​the number of​ **​independent​** ​vectors that remain after​​we remove​
​the​ **​dependent​** ​vectors. A vector is said to be​ _​dependent​_ ​if it can be​
​written as a sum of multiples of other vectors in the set.​


​The labeling of vectors as independent or dependent depends on​
​the order in which the vectors are considered, but regardless of​
​order, removing all dependent vectors will leave the same number​
​of independent vectors, even if the independent vectors themselves​
​are different for different orders.​


​For example, in the set​ ​we can start​

​by looking at the first vector,​ ​. This vector is​​dependent since​
​it can be produced by subtracting the other two vectors:​

​. Removing this vector from the set​

​yields the reduced set​ ​, which contains two​
​independent vectors and thus cannot be reduced any further.​


​Since the fully reduced set has two independent vectors, it spans a​
​2-dimensional plane, and since the original set has the same span as​
​the reduced set, the original set also spans the same 2-dimensional​
​plane.​


​Alternatively, beginning with the original set​

​we can start by looking at the second​

​vector,​ ​. This vector is dependent since it can be​​produced​

​by subtracting the other two vectors:​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​49​


​Removing this vector from the set yields the reduced set​

​, which contains two independent vectors and​
​thus cannot be reduced any further.​


​Again, since the fully reduced set has two independent vectors, it​
​spans a 2-dimensional plane, and since the original set has the same​
​span as the reduced set, the original set also spans the same​
​2-dimensional plane.​


​The last alternative, beginning with the original set​

​, is to start by looking at the third​

​vector,​ ​. This vector is dependent since it can be​​produced​

​by adding the other two vectors:​ ​.​
​Removing this vector from the set yields the reduced set​

​, which contains two independent vectors and​
​thus cannot be reduced any further.​


​Again, since the fully reduced set has two independent vectors, it​
​spans a 2-dimensional plane, and since the original set has the same​
​span as the reduced set, the original set also spans the same​
​2-dimensional plane.​

## **​Maximum Number of Independent Vectors​**


​Since the number of independent vectors in a set tells us the​
​dimension of the span of that set, we can make the general​
​conclusion that​ **​a set of N-dimensional vectors can​​have at most N​**
**​independent vectors.​**


​50​ ​Justin Skycak |​ **​Linear Algebra​**


​The N-dimensional vectors reside in N-dimensional space, so the​
​largest space they can possibly span is their full N-dimensional​
​space. Consequently, it’s not possible for the set of vectors to​
​contain more than N independent vectors -- otherwise, they would​
​need to span a space of more than N dimensions.​


​For example, consider the following set of vectors:​


​Looking at the first two vectors​ ​and​ ​, we see that​​these​
​two vectors are independent since they are not multiples of each​
​other. As a result, the span of the vectors must have a dimension of​
​at least 2.​


​But the vectors reside in 2-dimensional space, so their span is​
​limited to at most 2 dimensions. Thus, we can conclude that the set​
​of vectors spans exactly 2 dimensions, and that the third and fourth​
​vectors in the set must be dependent, without even needing to​
​check whether they can be written as sums of multiples of the first​
​two vectors.​


​Now, consider the following set of vectors:​


​Justin Skycak |​ **​Linear Algebra​** ​51​


​We can tell the first two vectors​ ​and​ ​are​
​independent since they aren’t multiples of each other, but it’s​

​harder to see whether the remaining two vectors​ ​and​

​are independent because we also have to make sure​
​they can’t be written as sums of multiples of other vectors in the​
​set.​

## **​Reduction​**


​To make it easier for us to tell whether these vectors are​
​independent, we can​ **​reduce​** ​the set of vectors to a​​simpler set with​
​the same span, by adding multiples of vectors from each other.​


​To begin the process of reduction, we can add multiples of the first​
​vector to the other vectors so that we eliminate the first component​
​from each of the other vectors.​

​●​ ​The second vector has a first component of​ ​, so we​​can​
​eliminate it by adding​ ​times the first vector.​

​●​ ​The third vector has a first component of​ ​, so we​​can​
​eliminate it by adding​ ​times the first vector.​

​●​ ​The fourth vector has a first component of​ ​, so we​​can​
​eliminate it by adding​ ​times the first vector.​


​52​ ​Justin Skycak |​ **​Linear Algebra​**


​The resulting set of vectors is shown below.​


​Since we only added multiples of vectors, we haven’t changed the​
​span at all. But now all of the first components are zero EXCEPT for​
​the first component in the first vector, so we can see that the first​
​vector cannot be written as a sum of other vectors in the set. All the​
​other vectors have zero in their first component, so every time we​
​add multiples of them, the result will still have zero in the first​
​component.​


​To check whether the second vector is independent, we can add​
​multiples of the second vector to the remaining vectors to eliminate​
​their second components.​


​But to make this easier, we can start by rescaling (i.e. multiplying)​
​the second vector to have a second component of​ ​.​​Its second​
​component is currently​ ​, so to convert​ ​to​ ​, we​​need to multiply​

​by​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​53​


​Now, we can add multiples of the second vector to the third and​
​fourth vectors so that we eliminate their second components.​

​●​ ​The third vector has a second component of​ ​, so we​​can​
​eliminate it by adding​ ​times the second vector.​

​●​ ​The fourth vector has a second component of​ ​, so​​we can​
​eliminate it by adding​ ​times the second vector.​


​Clearly, the second vector cannot be written as a sum of multiples​
​including the first vector, since including the first vector would cause​
​the first component to become nonzero. And the second vector​
​cannot be written as a sum of multiples of the third and fourth​
​vectors, either, because no combination of them can produce a​
​nonzero second component. So the second vector must be​
​independent.​


​54​ ​Justin Skycak |​ **​Linear Algebra​**


​To determine whether the third and fourth vectors are independent,​
​we can repeat the usual process once more. First, we’ll rescale the​

​third vector by​ ​so that its first component is​ ​.​


​The result is shown below.​


​The fourth vector has a third component of​ ​, so we​​can eliminate​
​it by adding​ ​times the third vector.​


​Our final result is shown below.​


​Justin Skycak |​ **​Linear Algebra​** ​55​


​We see that the first three vectors are independent, whereas the​
​fourth vector is dependent since it is a multiple of every vector in​
​the set (you can multiply any other vector by​ ​to​​obtain the fourth​
​vector). As a result, our set spans a 3-dimensional subspace of​
​4-dimensional space.​

## **​Exercises​**


​Tell the dimension of the span of the set of vectors.​


​56​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​57​

## **​1.5 Elimination as Vector Reduction​**


​Recall that systems of linear equations can be solved through​
**​elimination​**, multiplying equations by constants and​​adding​
​equations to each other to cancel variables.​


​For example, to solve the following linear system​


​we can start by adding the first equation to the second equation and​
​subtracting two times the first equation from the third equation.​


​58​ ​Justin Skycak |​ **​Linear Algebra​**


​Then, starting with​ ​, we can back-substitute to solve for each​
​of the variables:​


​We reach the final solution​ ​,​ ​, and​ ​.​

## **​Interpreting Elimination as Vector Reduction​**


​In light of the previous chapter, elimination can also be interpreted​
​as vector reduction.​


​First, we can interpret the linear system itself as a set of vectors,​
​consisting of the coefficients and constants.​


​Then, to reduce the set of vectors, we can add the first equation to​
​the second equation, and subtract two of the first equation from the​
​third equation.​


​Justin Skycak |​ **​Linear Algebra​** ​59​


​Then, we can convert the set of vectors back into equations that can​
​be solved in the same way via back-substitution.​


​The big geometric insight here is that​ **​the space of​​linear equations​**
**​is actually a vector space​** .​


​This occurs because we’re allowed to add/subtract multiples of the​
​equations. The particular linear equations in our system span a​
​subspace of this vector space, and reducing the vectors allows us to​
​simplify the system while maintaining the original span.​


​60​ ​Justin Skycak |​ **​Linear Algebra​**


​Thinking of linear equations in terms of vectors can sometimes yield​
​additional insight. For example, notice that for a system of linear​
​equations to have a single solution, the vectors must be reducible to​
​the following form:​


​In other words, the vectors must span all components except the​
​last. For a system of linear equations in​ ​variables,​​the vectors​
​consist of​ ​components: the first​ ​components correspond​​to​
​variable coefficients, and the last component corresponds to the​
​constant.​


​Justin Skycak |​ **​Linear Algebra​** ​61​


​As a result,​ **​for a system of linear equations in​** **​variables to have a​**
**​single solution, at least​** **​equations are required.​**

## **​Exercises​**


​Solve the following systems.​


​62​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​63​

# ​Part 2​ **​Volume​**


​64​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​65​

## **​2.1 N-Dimensional Volume Formula​**


​N-dimensional volume generalizes the idea of the space occupied by​
​an object:​


​●​ ​1-dimensional volume refers to the space occupied by a​
​1-dimensional object, such as the length of a line segment.​


​●​ ​2-dimensional volume refers to the space occupied by a​
​2-dimensional object, such as the area of a square.​


​●​ ​3-dimensional volume is what we normally mean by the word​
​“volume” -- the amount of space occupied by a 3-dimensional​
​object, such as the volume of a cube.​


​Continuing this pattern, we can infer that 4-dimensional volume​
​refers to the space occupied by a 4-dimensional object. It’s harder to​
​come up with an example, though, since it’s difficult to visualize​
​shapes in 4 and higher dimensions.​

## **​Volume Enclosed by N-Dimensional Vectors​**


​However, it becomes easier if we think about N-dimensional volume​
​as being enclosed by N-dimensional vectors.​


​66​ ​Justin Skycak |​ **​Linear Algebra​**


​The length of a unit line segment can be interpreted as the space​

​enclosed by the 1-dimensional unit vector​ ​.​


​The volume of a unit cube can be interpreted as the space enclosed​

​by the three 3-dimensional unit vectors:​ ​,​ ​, and​

​.​


​Justin Skycak |​ **​Linear Algebra​** ​67​


​unit vectors:​ ​,​ ​,​ ​, and​ ​.​


​This is harder to draw, but it gives us a general way to think about​
​volume in N dimensions. The volume of a unit N-dimensional cube​
​can be interpreted as the space enclosed by the N N-dimensional​
​unit vectors:​


​68​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Volume of a Parallelogram​**


​Given an object whose sides are perpendicular unit vectors, it’s easy​
​to see that the volume of the object is 1, since the distance of the​
​object in each perpendicular dimension is 1.​


​But it’s difficult when the vectors are not perpendicular. For​
​example, how would we compute the area of the parallelogram​

​enclosed by the vectors​ ​and​ ​?​


​Remember, the area of a parallelogram enclosed by two​
​3-dimensional vectors is just the magnitude of their cross product.​


​Although the vectors​ ​and​ ​are 2-dimensional, we​​can​

​interpret them as the 3-dimensional vectors​ ​and​ ​in​
​the​ ​plane.​


​Justin Skycak |​ **​Linear Algebra​** ​69​

## **​Volume of a Parallelepiped​**


​We can also use the cross product as a starting point to find the​
​volume of a parallelepiped enclosed by three 3-dimensional vectors​

​,​ ​, and​ ​.​


​The cross product of two of the vectors, say​ ​, gives​​a vector​
​whose magnitude is the area of a face of the parallelepiped, and​
​which points in the direction perpendicular to the face.​


​The height of the parallelepiped, then, is the length of the remaining​
​vector​ ​in the direction of​ ​.​


​70​ ​Justin Skycak |​ **​Linear Algebra​**


​Thus, the volume can be obtained using the dot product:​


​This result is known as the​ **​triple product​** .​


​Justin Skycak |​ **​Linear Algebra​** ​71​

## **​N-Dimensional Volume Formula​**


​Now that we know general methods to compute volume enclosed​
​by 2-dimensional and 3-dimensional vectors, how do we extend this​
​to 4-dimensional vectors?​


​If we rewrite the 3-dimensional volume formula in terms of the​
​2-dimensional volume formula, a pattern jumps out at us.​


​To start, let’s write down the 2-dimensional volume formula for two​

​vectors​ ​and​ ​.​


​However, in order to make the pattern clear, we will leave off the​
​absolute value sign, thereby permitting “signed” volume.​


​In 2 dimensions, the volume is traced out from the first vector​

​to the second vector​ ​, and the sign​
​of the volume just tells us whether the tracing occurs​
​counterclockwise (positive) or clockwise (negative). Intuitively, this​
​convention matches that which is used for tracing out positive or​
​negative angles in the unit circle.​


​72​ ​Justin Skycak |​ **​Linear Algebra​**


​Now, let’s write down the 3-dimensional volume formula for 3​

​vectors​ ​,​ ​, and​

​, again leaving off the absolute value sign and​
​thereby permitting “signed” volume. (The meaning of “signed”​
​volume in 3 dimensions will be addressed later.)​


​To ease notation, we define another volume function​ ​that also​
​computes volumes of vectors, but first re-indexes the vectors by​
​removing the k​ [​th​] ​component and moving entries after​​the k​ [​th​]

​component to the beginning of the vector. This way, the​
​3-dimensional volume formula can be simplified to​


​.​


​Using this form, we can guess at an N-dimensional volume formula:​


​Justin Skycak |​ **​Linear Algebra​** ​73​

## **​Sanity Checks​**


​Let’s test out this formula on a simple case: the 4-dimensional unit​

​cube, which is enclosed by the vectors​ ​,​

​,​ ​, and​ ​.​


​74​ ​Justin Skycak |​ **​Linear Algebra​**


​Now we’re reaching the point where it’s hard to actually “see”​
​what’s happening. But the math shows us a pattern, the pattern​
​matches our intuition on a simple case, and given that​
​3-dimensional volume is the sum of multiples of 2-dimensional​
​volumes, it seems plausible that N-dimensional volume could be the​
​sum of multiples of (N-1)-dimensional volumes.​


​Moreover, the volume formula matches our intuition when we​
​rescale a vector. Intuitively, rescaling a vector should have the effect​
​of rescaling the volume: for example, if we double the length of one​
​of the sides of a parallelogram, the area should double.​


​Justin Skycak |​ **​Linear Algebra​** ​75​


​Likewise, if we double the length of one of the sides of a​
​parallelepiped, then the volume should double.​


​76​ ​Justin Skycak |​ **​Linear Algebra​**


​Of course, we have only shown that rescaling the first vector​
​rescales the volume. However, we can use this fact to show that​
​rescaling the second vector also rescales the volume.​


​Justin Skycak |​ **​Linear Algebra​** ​77​


​We could keep on going, using similar arguments to show that​
​rescaling the 3rd, 4th, so on, and Nth vector have the same effect of​
​rescaling the volume.​

## **​Final Remarks​**


​Unfortunately, this volume formula is unintuitive and unwieldy for​
​volume computations in high-dimensional space.​


​Soon, though, we will introduce a more intuitive concept called​
**​shearing​**, which will lead us to an easier, more intuitive​​process of​
​computing high-dimensional volumes.​


​The volume formula presented in this chapter is still noteworthy,​
​though, because although shearing will provide us with a​ _​process​_ ​for​
​computing volume, it won’t give us a​ _​formula​_ ​for computing​​volume.​

## **​Exercises​**


​Compute the N-dimensional unsigned volume​
​enclosed by the vectors​ ​.​


​78​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​79​

## **​2.2 Volume as the Determinant of a​** **​Square Linear System​**


​We have seen that the space of linear equations is actually a vector​
​space, and that the linear equations in any particular system span a​
​subspace of this vector space.​

## **​Linear Systems as Vector Equations​**


​However, there is also another way to interpret linear systems in​
​terms of vectors:​ **​a linear system can be interpreted​​as a single​**
**​vector equation stating that some multiples of particular vectors​**
**​add up to another particular vector.​**


​For example, we can write the system below as a vector equation by​
​interpreting each side of the equation as a vector:​


​80​ ​Justin Skycak |​ **​Linear Algebra​**


​This equation states that some multiples​ ​,​ ​, and​ ​of the​

​coefficient vectors​ ​,​ ​, and​ ​sum to the​

​constant vector​ ​.​


​You might recall that we solved this system earlier using reduction,​
​and we found that the solution was​ ​,​ ​, and​ ​.​
​Now, we see that these are simply the multiples of the coefficient​
​vectors that sum to the constant vector.​


​For the linear system to have a solution, there must be some​
​multiples of the coefficient vectors that add to the constant vector.​
​In other words, for the linear system to have a solution, the constant​
​vector must be in the span of the coefficient vectors.​


​Thinking about linear systems in terms of coefficient vectors can​
​provide useful intuition. For example, we can tell that the linear​
​system below has a solution because its coefficient vectors span the​
​full 2-dimensional plane.​


​Justin Skycak |​ **​Linear Algebra​** ​81​


​Moreover, since there are 3 coefficient vectors spanning a​
​2-dimensional plane, there must be a dependent vector, so there​
​must be infinitely many solutions.​


​For example,​ ​is a multiple of​ ​, so in any solution​​we can​
​increase​ ​by some amount and decrease​ ​by twice​​that amount​
​to yield another solution. Thus since​ ​is a​
​solution, so is​ ​, and​ ​,​
​and so on.​

## **​The Determinant​**


​When there are exactly N coefficient vectors that form an​
​N-dimensional parallelepiped, we can also extend this intuition to​
​relate to the volume of the coefficient vectors. Such linear systems​
​are called​ **​square​** ​linear systems because they consist​​of N rows of​
​equations and N columns of variables. In a square system, the​
​volume of the coefficient vectors is called the​ **​determinant​**,​​because​
​it​ _​determines​_ ​much about the solutions of the system.​


**​When the determinant is nonzero, there is exactly one solution.​**
​When the determinant is nonzero, the N coefficient vectors form a​
​parallelepiped that extends some nonzero amount in all N​
​dimensions, and consequently the coefficient vectors span the full​
​N-dimensional space, guaranteeing a solution.​


​82​ ​Justin Skycak |​ **​Linear Algebra​**


​Moreover, the solution must be unique. For N vectors to span N​
​dimensions, the vectors must be independent -- meaning that no​
​vector can be written in terms of the others, and thus guaranteeing​
​that there is only one solution.​


​For example, the following linear system has a nonzero determinant,​
​and a single solution​ ​.​


​On the other hand,​ **​when the determinant is zero, there​​are either​**
**​no solutions or infinitely many solutions.​** ​When the​​determinant is​
​zero, the coefficient vectors form a parallelepiped that is flat in at​
​least one dimension, and consequently the coefficient vectors span​
​only a smaller subspace of N-dimensional space, which may or may​
​not contain the constant vector.​


​If the subspace​ _​does not​_ ​contain the constant vector,​​then there is​
​no solution.​


​If the subspace​ _​does​_ ​contain the constant vector,​​then there is a​
​solution, and moreover, since a set of N vectors spanning fewer than​
​N dimensions must contain at least one dependent vector, there​
​must be infinitely many solutions.​


​Justin Skycak |​ **​Linear Algebra​** ​83​


​For example, the following linear system has a zero determinant and​
​no solutions.​


​On the other hand, the following linear system has a zero​
​determinant, and infinitely many solutions.​


​One solution, for example, is​ ​. But since​

​is the sum of​ ​and​ ​, we can obtain another​
​solution by increasing​ ​and​ ​by some amount, and​​decreasing​
​by that same amount. For example, another solution is​

​, and yet another solution is​

​.​


​Later, we will see that the determinant plays a fundamental role in​
​understanding transformations of vectors, which are called​


​84​ ​Justin Skycak |​ **​Linear Algebra​**


**​matrices​** . For now, though, we will just get in the habit of writing​
​volume using the determinant operator​ ​in place of​ ​.​

## **​Exercises​**


​Determine whether the system has A) exactly one solution, or B) no​
​solutions or infinitely many solutions.​


​Justin Skycak |​ **​Linear Algebra​** ​85​


​86​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​87​

## **​2.3 Shearing, Cramer’s Rule, and​** **​Volume by Reduction​**


​Not only can a nonzero determinant tell us that a linear system has​
​exactly one solution -- the nonzero determinant can also help us​
​quickly find that solution through a process known as​ **​Cramer’s rule.​**

## **​Shearing​**


​The key bit of intuition surrounding Cramer’s rule is the idea that​
​moving one of the sides of a parallelepiped in a parallel direction​
​does not change the volume of the parallelepiped. This kind of​
​transformation is known as​ **​shearing​**, and the intuition​​can be most​
​easily illustrated in 2 dimensions.​


​Suppose we have the following 2-dimensional linear system:​


​The three vectors in this system -- two coefficient vectors and one​
​constant vector -- can be represented visually as the vertices of a​
​parallelogram.​


​88​ ​Justin Skycak |​ **​Linear Algebra​**


​parallelogram, we have​


​.​


​Using the fact that scaling a vector results in the volume being​
​scaled by the same amount, we can simplify and solve for​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​89​


​This is the solution for​ ​in the original system!​​We can use the​
​same method to solve for​ ​, too.​


​90​ ​Justin Skycak |​ **​Linear Algebra​**


​This method is known as​ **​Cramer’s rule​** . We illustrate​​it below on a​
​concrete example, which would otherwise be annoying to solve by​
​reduction because its solutions are fractional.​


​Using Cramer’s rule, however, the solutions are much easier to​
​compute.​


​Justin Skycak |​ **​Linear Algebra​** ​91​

## **​Cramer’s Rule in N Dimensions​**


​To generalize Cramer’s rule to N dimensions, we first come up with a​
​compact notation for writing systems of linear equations.​


​In this notation, we reduce the linear system to a single equation in​

​terms of the vectors​ ​,​ ​, and​

​. The solutions from Cramer’s rule can then be written​
​as follows:​


​The pattern is clear:​ ​is given by a fraction whose​​denominator is​
​the determinant of the coefficient vectors, and whose numerator is​
​the same except that the​ ​th coefficient vector​ ​is replaced with​
​the constant vector​ ​.​


​92​ ​Justin Skycak |​ **​Linear Algebra​**


​For an N-dimensional square linear system, then, the solutions to​


​are given by​


​.​

## **​Volume by Reduction​**


​Now, let’s take a step back and talk more about the elegance of​
​shearing. We have seen that through Cramer’s rule, shearing can be​
​used to express the solution of a linear system using ratios of​
​volumes. Now, we will see that​ **​shearing can also be​​used to​**
**​compute volumes themselves, without having to use the volume​**
**​formula.​**


​In a set of vectors, shearing simply amounts to adding one vector to​
​another vector. Consequently, reducing a set of vectors preserves​
​the volume of the parallelepiped formed by those vectors, provided​
​that we don’t rescale any of the vectors themselves (otherwise, the​
​volume would be rescaled as well).​


​The volume of a reduced set of vectors is much easier to compute:​
​we can simply multiply the diagonal, because the diagonal entries​
​are the parallelepiped’s lengths in each dimension.​


​Justin Skycak |​ **​Linear Algebra​** ​93​


​As a simple example, we can use shearing to compute the volume​

​enclosed by the vectors​ ​and​ ​.​


​94​ ​Justin Skycak |​ **​Linear Algebra​**


​When computing the volume of 4 or more vectors, it is much faster​
​to use shearing instead of the volume formula. Below is an example​
​of a 4-dimensional volume calculation using shearing.​


​Justin Skycak |​ **​Linear Algebra​** ​95​

## **​Exercises​**


​State whether the linear system has A) exactly one solution, or B) no​
​solutions or infinitely many solutions. If there is A) exactly one​
​solution, then use Cramer’s rule to find it.​


​In your calculations of determinants in higher than 3 dimensions, be​
​sure to use the technique of shearing -- it will save lots of time!​


​96​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​97​

## **​2.4 Higher-Order Variation of Parameters​**


​Until this point, we have been working exclusively with linear​
​systems. However, solving linear systems can sometimes be a​
​necessary component of solving nonlinear systems.​

## **​Second-Order Variation of Parameters​**


​For example, recall the​ **​variation of parameters​** ​method​​for solving a​
​second-order differential equation of the form​


​.​


​Variation of parameters proceeds by first guessing a solution of the​
​form​


​,​


​where​ ​and​ ​are the two zero solutions of the differential​
​equation​


​,​


​and​ ​and​ ​are some unknown multiplier functions​​that​
​we solve for by setting up a system of equations.​


​98​ ​Justin Skycak |​ **​Linear Algebra​**


​To set up the first equation in our system, we force​


​and equate it to the true derivative of​ ​:​


​The second equation comes from substituting our guess for​ ​into​
​the differential equation and simplifying, using the fact that​ ​and​
​are the zero solutions.​


​This results in a square system of 2 equations.​


​Justin Skycak |​ **​Linear Algebra​** ​99​


​In 2 dimensions, we can easily solve for​ ​and​ ​using​
​elimination, obtaining the result below.​


​Then, we can simply integrate and substitute these back into our​
​particular solution.​

## **​Higher-Order Variation of Parameters​**


​When we wish to use variation of parameters to find the particular​
​solution of an Nth order differential equation​


​we guess a solution of the form​


​and force​


​100​ ​Justin Skycak |​ **​Linear Algebra​**


​.​


​By equating each derivative with the true derivative of​ ​up to​
​order N, we can set up a system of equations.​


​This system is difficult to solve by elimination. But now we can use​
​Cramer’s rule! First, let’s write our system more compactly, using the​
​notation​


​.​


​The system becomes​


​.​


​According to Cramer’s rule, each​ ​is given by​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​101​


​The denominator of this fraction is also known as the​ **​Wronskian​**,​
​denoted​


​.​


​If we define​ ​as​


​then we have​


​.​


​Finally, we can write the particular solution to the differential​
​equation by integrating and substituting into our initial guess.​

## **​Demonstration​**


​Let’s illustrate this method on a simple example. To make it easier to​
​find the zero solutions, we’ll choose an example with constant​
​coefficients, but remember that this method works even when the​
​coefficients are functions themselves.​


​102​ ​Justin Skycak |​ **​Linear Algebra​**


​We start off by finding the zero solutions, i.e. those that satisfy the​
​equation whose right-hand side is zero.​


​We do this by finding the roots of the characteristic polynomial​

​. We can find the roots via factoring by​
​grouping.​


​These roots correspond to the following zero solutions:​


​It remains to find the particular solution. To use variation of​
​parameters, we need three independent zero solutions, so we’ll​

​choose the simplest ones from above:​ ​.​


​Substituting these into the variation of parameters formula, we have​
​a particular solution of the form​


​Justin Skycak |​ **​Linear Algebra​** ​103​


​with​ ​. Now, it remains to do the computations. First,​​we​
​compute the standard Wronskian in the denominator.​


​104​ ​Justin Skycak |​ **​Linear Algebra​**


​Next, we compute the modified Wronskians in the numerators.​


​Justin Skycak |​ **​Linear Algebra​** ​105​


​Lastly, we substitute back into the formula for the particular​
​solution, and simplify.​


​106​ ​Justin Skycak |​ **​Linear Algebra​**


​The full solution to the differential equation, then, is​


​.​

## **​Exercises​**


​Solve the following differential equations using variation of​
​parameters.​


​Justin Skycak |​ **​Linear Algebra​** ​107​

# ​Part 3​ **​Matrices​**


​108​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​109​

## **​3.1 Linear Systems as Transformations​** **​of Vectors by Matrices​**


​Let’s create a compact notation for expressing systems of linear​
​equations like the one shown below.​

## **​Matrices of Column Vectors​**


​We’re familiar with a slightly condensed version using coefficient​
​vectors.​


​However, we can condense this even further by putting the​
​coefficient vectors in a vector themselves and taking the dot product​
​with the vector of variables.​


​110​ ​Justin Skycak |​ **​Linear Algebra​**


​To save space, the vector of variables can be written as a column​
​vector as well.​


​Finally, to simplify the notation, we can remove the vector braces​
​around the individual coefficient vectors and remove the dot​
​product symbol.​


​The array containing the coefficients is called a​ **​matrix​** . It’s really just​
​a vector of sub-vectors, written without braces on the individual​
​sub-vectors.​


​Justin Skycak |​ **​Linear Algebra​** ​111​


​Looking back, it makes sense to define a matrix multiplying a vector​
​as follows:​

## **​Matrices of Row Vectors​**


​Keeping this form of matrix notation and multiplication in mind, let’s​
​start from scratch and proceed to condense a system of linear​
​equations in a different way. We’ll get an interesting result.​


​Again, we will start with the system below.​


​This time, however, we will begin by writing each equation as a dot​
​product.​


​112​ ​Justin Skycak |​ **​Linear Algebra​**


​Then, we will write the system as a single vector equation by​
​interpreting each side of the equation as a vector.​


​Each component of the left-hand-side vector includes a dot product​
​with the vector of variables, so we can factor out the vector of​
​variables.​


​Again, to save space, the vector of variables can be written as a​
​column vector.​


​Justin Skycak |​ **​Linear Algebra​** ​113​


​Finally, to simplify the notation, we can again remove the vector​
​braces around the individual coefficient vectors.​


​Again, there is a matrix! And again, the matrix just represents a​
​vector of sub-vectors, written without braces on the individual​
​sub-vectors.​


​But this time, looking back, it makes sense to define a matrix​
​multiplying a vector by a different rule.​

## **​Matrix Multiplication​**


​Which rule is correct? It turns out, they both are. Before we do an​
​example, though, let’s recap.​


​114​ ​Justin Skycak |​ **​Linear Algebra​**


​We’re stumbling upon the following structure:​


​The array on the left-hand side is called a matrix, and we have two​
​ways to compute the product of a matrix and a vector -- one which​
​involves interpreting the columns of the matrix as individual vectors,​
​and another which involves interpreting the rows of the matrix as​
​individual vectors.​


​Justin Skycak |​ **​Linear Algebra​** ​115​


​To verify that both methods of computation indeed yield the same​
​result, we can try out a simple example using the two different​
​methods to compute the product of a 2-by-2 matrix and a​
​2-dimensional vector.​


​116​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Geometric Intuition​**


​Lastly, let’s build some geometric intuition. Geometrically, a matrix​
​represents a transformation of a vector space, and we can visualize​
​this transformation by thinking about what the matrix does to the​
​N-dimensional unit cube.​


​For example, to see what the matrix from the example does to the​

​unit square, we can multiply the vertices​ ​and​ ​of the unit​
​square by the matrix.​


​We see that the matrix moves the vertices of the unit square from​

​and​ ​, to​ ​and​ ​. Notice that these are just the​
​columns of the matrix!​


​Justin Skycak |​ **​Linear Algebra​** ​117​


​118​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Exercises​**


​Convert the following linear systems to matrix form.​


​Justin Skycak |​ **​Linear Algebra​** ​119​


​Compute the product of the given vector and matrix by A)​
​interpreting the columns of the matrix as individual vectors, and B)​
​interpreting the rows of the matrix as individual vectors. Verify that​
​the results are the same.​


​120​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​121​

## **​3.2 Matrix Multiplication​**


​We have seen how to multiply a vector by a matrix. Now, we will see​
​how to multiply a matrix by another matrix.​


​Whereas multiplying a vector by a matrix corresponds to a linear​
​transformation of that vector, multiplying a matrix by another matrix​
​corresponds to a composition of linear transformations.​

## **​General Procedure​**


​The procedure for matrix multiplication is quite familiar: we simply​
​multiply each column vector in the right matrix by the left matrix.​


​Really, we’re just trying to figure out where the points​ ​and​

​map to after being transformed once by the right​​matrix and​
​then again by the left matrix. We already know that the right matrix​
​maps those points to its columns, so all we have to do is map those​
​columns according to the left matrix.​


​122​ ​Justin Skycak |​ **​Linear Algebra​**


​An example is shown below.​


​We can verify that multiplying a vector by this new matrix gives the​
​same result as multiplying the vector first by the original right​
​matrix, and then by the original left matrix.​


​Justin Skycak |​ **​Linear Algebra​** ​123​

## **​Case of Rectangular Matrices​**


​Matrix multiplication isn’t limited to just square matrices. The​
​matrices can be rectangular, too.​


​But notice that if we switch the above example around, it no longer​
​makes sense to multiply the matrices, because we are unable to​
​multiply each column vector in the right matrix by the left matrix.​
​There are fewer columns in the left matrix than there are entries in​
​each column of the right matrix.​


​124​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Criterion for Multiplication​**


[​The trick to telling whether matrix multiplication is defined in a​](http://www.texrendr.com/?eqn=%5Cbegin%7Balign*%7D%20%5Cbegin%7Bpmatrix%7D%203%20%26%204%20%5C%5C%205%20%26%206%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%201%20%26%202%20%5Cend%7Bpmatrix%7D%20%5Cend%7Balign*%7D%0)
[​particular case is to check whether the width of the left matrix​](http://www.texrendr.com/?eqn=%5Cbegin%7Balign*%7D%20%5Cbegin%7Bpmatrix%7D%203%20%26%204%20%5C%5C%205%20%26%206%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%201%20%26%202%20%5Cend%7Bpmatrix%7D%20%5Cend%7Balign*%7D%0)
[​matches the height of the right matrix.​](http://www.texrendr.com/?eqn=%5Cbegin%7Balign*%7D%20%5Cbegin%7Bpmatrix%7D%203%20%26%204%20%5C%5C%205%20%26%206%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%201%20%26%202%20%5Cend%7Bpmatrix%7D%20%5Cend%7Balign*%7D%0)


​Matrix dimensions are usually written as​ ​, so matrix​
​multiplication is defined whenever the inner dimensions match up.​


​For example, in the multiplication​


​the left matrix has dimensions​ ​and the right matrix​​has​
​dimensions​ ​.​


​Writing these dimensions in the order of multiplication, we see that​
​the inner dimensions do indeed match up: they’re​ ​and​ ​.​


​Moreover, the outer dimensions give the dimensions of the resulting​
​product:​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​125​


​On the other hand, the matrices in the multiplication​


​have dimensions​ ​. The inner dimensions don’t​
​match up: they’re​ ​and​ ​. Therefore, the matrix multiplication​​is​
​not defined.​


​Notice the implications for square matrices: multiplication is defined​
​for square matrices only when they both have the same dimensions,​
​say​ ​, and multiplication remains defined even if​​we switch​
​the order of the square matrices, because the dimensions of the​
​product stay the same:​


​Moreover, the output is itself a square matrix of the same​
​dimension,​ ​.​

## **​Non-Commutativity​**


​Even for square matrices, though,​ **​matrix multiplication​​is generally​**
**​not commutative​** ​-- if we switch the order of two matrices​​in a​
​product, we tend to get a different result.​


​126​ ​Justin Skycak |​ **​Linear Algebra​**


​For example, switching the two matrices in the most recent example​
​yields a different result:​


​Even simple matrices generally do not commute:​


​The reason matrices tend not to commute is that left-multiplication​
​and right-multiplication have different interpretations:​
​left-multiplication sums combinations of row vectors, whereas​
​right-multiplication sums combinations of column vectors.​


​Justin Skycak |​ **​Linear Algebra​** ​127​


​Applying some operation to the rows of a matrix is generally not the​
​same as applying that operation to the columns of a matrix.​


**​Left-multiplication of​** **​by​**


**​Right-multiplication of​** **​by​**

## **​Diagonal Matrices​**


​That being said, there are some instances in which matrices do​
​commute.​


​128​ ​Justin Skycak |​ **​Linear Algebra​**


​For example,​ **​diagonal​** ​matrices commute with each other. (A​
​diagonal matrix consists of zero everywhere except the diagonal​
​running from the top-left entry to the bottom-right entry.)​


​Diagonal matrices commute with each other because the diagonal​
​components end up being multiplied independently as scalars rather​
​than vectors, and scalar multiplication does in fact commute.​


​Be aware, though, that​ **​antidiagonal​** ​matrices generally​​do not​
​commute with each other. (An antidiagonal matrix is like a diagonal​
​matrix, but with the diagonal running from top-right to bottom-left.)​


​Justin Skycak |​ **​Linear Algebra​** ​129​

## **​Exercises​**


​Compute the product of the given matrices, if possible, using A) the​
​left-multiplication interpretation, and B) the right-multiplication​
​interpretation.​


​Otherwise, if it is not possible to compute the product, then state​
​the dimensions that A) the left matrix would need to have for the​
​multiplication to be defined, or B) that the right matrix would need​
​to have for the multiplication to be defined.​


​130​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​131​

## **​3.3 Rescaling, Shearing, and the Determinant​**


​The key insight in this chapter is that​ **​every square​​matrix can be​**
**​decomposed into a product of rescalings and shears​** .​​Before we​
​elaborate on that, though, let’s discuss what rescalings and shears​
​are, in terms of matrices.​

## **​Rescaling Matrices​**


**​Rescaling matrices​** ​are matrices that rescale the dimensions​​of​
​space, with each dimension potentially being rescaled by a different​
​amount. That is to say, the dimensions of space maintain their​
​original direction, but their lengths are multiplied by some factors.​


​For example, in 2-dimensional space, the rescaling of​ ​into​


​and​ ​into​ ​is given by left- or right-multiplication​​by​
​the following rescaling matrix:​


​132​ ​Justin Skycak |​ **​Linear Algebra​**


​We could also have negative rescalings, or even zero rescalings that​
​collapse a vector’s length down to​ ​. For example,​​the rescaling​

​matrix that rescales​ ​into​ ​and​ ​into​ ​is given​
​by​


​.​


​We can extend to higher dimensions as well. In 3-dimensional space,​

​the rescaling matrix that rescales​ ​to​ ​, and​


​to​ ​, and​ ​to​ ​is given by​


​.​


​Do you notice a pattern?​ **​Rescaling matrices are just​​diagonal​**
**​matrices!​**


​There is a fast trick for multiplying rescaling matrices: just multiply​
​the diagonal entries independently. Consequently, the product of​
​two rescaling matrices is itself always a rescaling matrix as well.​


​Likewise, there is also a fast trick to compute the determinant of a​
​rescaling matrix. Since the vectors in a rescaling matrix form a​
​rectangular prism, and the volume of that prism is obtained by​


​Justin Skycak |​ **​Linear Algebra​** ​133​


​multiplying the side lengths, the determinant of a rescaling matrix is​
​simply the product of the rescalings, i.e. the product of the diagonal.​

## **​Shearing Matrices​**


​Now let’s talk about​ **​shearing matrices​** . Recall that​​shearing involves​
​moving one of the sides of a parallelepiped in a parallel direction,​
​and does not change the volume of the parallelepiped. We have also​
​seen that in a set of vectors, shearing simply amounts to adding a​
​multiple of some vector to a different vector.​


​Since a matrix is defined by its transformation of the unit cube, we​
​can consider just the shears of the unit cube. In 2 dimensions, for​
​example, a shear of the unit cube would either consist of vectors​

​and​ ​, or​ ​and​ ​, where​ ​is the multiple of​
​the vector that is added.​


​134​ ​Justin Skycak |​ **​Linear Algebra​**

|​Lef-t multiply​:​|Col2|Col3|Col4|
|---|---|---|---|
|​OR​||||
|​Right-multply**​**:​||||



​Do you notice a pattern?​ **​Shear matrices consist of​​a diagonal of 1s,​**
**​with all other entries zero except for possibly a single row or​**
**​column.​**


​Justin Skycak |​ **​Linear Algebra​** ​135​


​Unfortunately, there is no easy trick for multiplying shear matrices,​
​other than just adding multiples of one row/column to another​
​row/column. The result of multiplying two shear matrices might not​
​even maintain a diagonal of 1s, for example:​


​However, there is one property that is conserved in the result of​
​multiplying shear matrices: the determinant of a product of shear​
​matrices has to remain 1. This is because shear matrices don’t​
​change the volume of any parallelepiped within a vector space.​

## **​Decomposing into Rescalings and Shears​**


​Now let’s move onto the main idea of this chapter:​ **​every square​**
**​matrix can be decomposed into a product of rescalings and shears​** .​
​We’ll illustrate the process through a couple of examples.​


​The process of decomposing a matrix into a product of rescalings​
​and shears is very familiar -- it mainly consists of reducing the row or​
​column vectors while keeping track of our multipliers in rescaling​
​and shear vectors.​


​The only catch is that we need to keep track of the process​ _​in​_
_​reverse​_, which means we have to flip the sign of the​​multipliers that​
​we put in shear matrices, and take the reciprocal of the multipliers​
​that we put in rescaling matrices.​


​136​ ​Justin Skycak |​ **​Linear Algebra​**


​For example, to decompose the matrix below into a product of​
​rescalings and shears, we start by adding​ ​times​​the first row to​
​the second row, which means we put​ ​in our left shear​​matrix to​
​represent the reverse operation. Then, we multiply the bottom row​

​by​ ​, which means we put​ ​in our left rescaling matrix​​to​
​represent the reverse operation.​


​Here is another example, which might initially seem tricky because​
​the first row has a​ ​as its first entry. However,​​we can create a​ ​as​


​the first entry by adding​ ​of the second row. Then,​​all that​
​remains is to rescale the second row.​


​Justin Skycak |​ **​Linear Algebra​** ​137​


​Note that sometimes we may need to rescale by​ ​to introduce a​
​into a row of​ ​s, such as in the top row of the matrix​​below.​


​Likewise, to introduce a​ ​into a​ _​column​_ ​of​ ​s, we​​can​ _​right​_ -multiply​
​by a rescaling matrix having a​ ​entry on the diagonal.​


​Below is a final example of decomposing a​ ​matrix​​into​
​rescalings and shears.​


​138​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Determinant of a Product​**


​One important consequence of decomposing square matrices into​
​rescalings and shears is that,​ **​for two square matrices​** **​and​** **​, we​**
**​have​**


​.​


​To understand why this is, imagine writing​ ​and​ ​each as a​
​product of rescalings and shears.​


​Since the shears have no effect on volume, they can be removed​

​from the product​ ​without changing​ ​.​


​Then, we are left with the rescaling matrices for​ ​and​ ​, which​
​give the determinants for​ ​and​ ​, respectively.​


​Justin Skycak |​ **​Linear Algebra​** ​139​

## **​Meaning of Negative Determinant​**


​Another consequence of decomposing square matrices into​
​rescalings and shears is that it makes clear the meaning of negative​
​determinant.​


​Since shears don’t change the determinant, a negative in a​
​determinant must come from the rescalings -- meaning that the​
​total number of negative entries in the diagonals of all the rescaling​
​matrices must be odd.​


​There is geometric intuition for negative determinants as well,​
​having to do with the orientation of space.​


​The orientation of space can be thought of as a “curl” proceeding​
​from​ ​to​ ​, and then to​ ​, and so on, until​ ​, and​​then back​
​to​ ​. For example, for the unit cube in 3 dimensions,​​the curl is​
​counterclockwise (when viewed opposite the origin).​


​However, applying a matrix with a single negative rescaling and thus​
​a determinant of​ ​, one of the sides of the unit cube​​is flipped in​
​the opposite direction. This causes the curl to reverse its orientation​
​from counterclockwise to clockwise.​


​140​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​141​

## **​Exercises​**


​Decompose the following matrices into products of rescalings and​
​shears.​


​142​ ​Justin Skycak |​ **​Linear Algebra​**


​Compute​ ​for the matrix​ ​in the equations below,​​given​

​that​ ​,​ ​, and​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​143​

## **​3.4 Inverse Matrices​**


​In this chapter, we introduce the idea of the​ **​inverse​** ​of a matrix,​
​which undoes the transformation of that matrix.​

## **​Verifying an Inverse Matrix​**


​For example, it’s straightforward that the inverse of the rescaling​
​matrix​


​is obtained as the rescaling matrix that rescales each dimension by​
​the inverse amount.​


​We can verify that by multiplying the matrix by its inverse, and​
​observing that the inverse takes the matrix back to the unit square.​


​144​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Procedure for Finding the Inverse​**


​But when we consider a more general matrix like the one below, it’s​
​less straightforward how to find the inverse.​


​We could try inverting each of the components separately, like we​
​did with the diagonal of the rescaling matrix, but the resulting​
​matrix doesn’t take the original matrix back to the unit square -- so​
​it can’t be the inverse.​


​Here is another idea: since we want to end up with the unit square,​
​let’s left-multiply our matrix by other matrices representing row​
​operations until we get to the unit square.​


​Justin Skycak |​ **​Linear Algebra​** ​145​


​Then, let’s take all the matrices we multiplied by, and find their​
​product. That will be our inverse matrix.​


​We can verify that indeed, this is the correct inverse matrix.​

## **​Left and Right Inverses​**


​Based on the fact that we computed the inverse by left-multiplying,​
​we should only expect the inverse to work for left-multiplication.​


​Interestingly, it works for right-multiplication as well!​


​This result is general to any inverse matrix -- regardless of whether​
​we multiply a matrix by its inverse on the left or right, the result will​
​be the unit cube.​


​146​ ​Justin Skycak |​ **​Linear Algebra​**


​To see why, we’ll need to do a bit of simple algebra. To ease​
​notation, we’ll denote the unit cube matrix by​ ​, which stands for​
​the​ **​identity matrix​** ​and comes from the fact that​
​for any matrix​ ​.​


​Since​ ​for an inverse matrix obtained by​
​left-multiplication, and since matrix multiplication is associative, we​
​have​


​.​


​But if we left-multiply​ ​by a matrix and maintain​​a result of​ ​,​

​that matrix must be the identity! That is, if​ ​, then​​we​
​must have​ ​. Hence, left and right inverses are one​​and​
​the same.​

## **​Non-Invertible Matrices​**


​Now, let’s try to find the inverse of the matrix below. Something​
​weird will happen.​


​This is simply a rescaling matrix with the rescaling quantities​ ​and​
​on the diagonal. With rescaling matrices, we’re used to finding the​

​inverse by inverting the diagonal entries. We can invert​ ​and get​ ​,​


​but we can’t invert​ ​-- the fraction​ ​is undefined.​


​Justin Skycak |​ **​Linear Algebra​** ​147​


​It turns out, this matrix has no inverse. In general, any matrix having​
​a​ ​rescaling has no inverse, because once a vector​​is rescaled by a​
​factor of​ ​, it’s impossible to recover the original​​length of the​
​vector -- as far as we know, it could be any length, because​ ​times​
​any number results in​ ​.​

## **​Criterion for Invertibility​**


​By the same token, any matrix whose rescalings are all nonzero has​
​an inverse. Once a vector is rescaled by a factor of​ ​, we can​
​recover the original length of the vector by simply rescaling again​

​by​ ​.​


​Since the determinant of a matrix is the product of its rescalings, we​
​can put all this together into an elegant statement:​ **​a matrix is​**
**​invertible if and only if its determinant is nonzero.​**


​This statement gives another perspective on why a linear system​
​with nonzero determinant has exactly 1 solution, whereas a linear​
​system with zero determinant has none or infinitely many solutions.​


​Any linear system can be written as a matrix equation​ ​, and​

​if​ ​, then​ ​exists, resulting in a single solution​​given​
​by​ ​.​


​On the other hand, if​ ​, then​ ​contains some zero​
​rescaling, and thus if there is any solution at all, then there must be​
​infinitely many solutions because multiplication by zero gives the​
​same result for infinitely many numbers.​


​148​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Faster Method for Computing Inverses​**


​Lastly, let’s end by discussing a faster method to compute inverse​
​matrices, based on the technique of reduction.​


​We already know how to use reduction to keep track of coefficients​
​when solving linear systems by elimination -- but we’ll introduce a​
​more compact​ **​augmented matrix​** ​notation that will allow​​us to​
​compute inverse matrices.​


​To solve the linear system below, we first convert it to an augmented​
​matrix.​


​Then, we perform row operations on the augmented matrix until we​
​have reduced the left-hand side to the identity matrix.​


​Finally, the solutions are displayed on the right-hand side:​
​and​ ​.​


​This process is familiar -- we’re just left-multiplying by matrices​
​corresponding to row operations until we get to the identity matrix,​
​at which point we have effectively multiplied the original left-hand​
​side matrix by its inverse.​


​Justin Skycak |​ **​Linear Algebra​** ​149​


​Since we perform those same operations on the right-hand side​
​vector, we are effectively multiplying the vector by the inverse​
​matrix as well, which yields the solution.​


​If we want to find the actual inverse matrix, rather than just using it​
​to solve the system, we can modify this process slightly by replacing​
​the original right-hand side vector with the identity matrix.​


​Then, once the left-hand side matrix is taken to the identity matrix,​
​the right-hand side identity matrix will be taken to the inverse​
​matrix.​


​To find the actual inverse matrix in the previous example, we replace​
​the right-hand side with the identity matrix and perform the same​
​row operations to reduce the left-hand side.​


​Thus, we have the inverse matrix:​


​150​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Formula for the Inverse of a 2-by-2 Matrix​**


​There is a nice general formula for the inverse of a​ ​matrix,​
​which is given below.​


​It is recommended to memorize this formula to ease manipulations​
​with​ ​matrices, since the whole point of doing examples​​with​
​matrices is to ensure that they are relatively simple​​and fast.​

## **​Exercises​**


​For each given matrix​ ​, compute​ ​to tell whether​ ​is​
​invertible. If it is, then compute​ ​, and verify that​
​and​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​151​


​For each equation​ ​, tell whether​ ​exists. If it​​does, then​
​compute the solution​ ​.​


​152​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​153​

# ​Part 4​ **​Eigenspace​**


​154​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​155​

## **​4.1 Eigenvalues, Eigenvectors, and​** **​Diagonalization​**


​Suppose we want to compute a matrix raised to a large power, i.e.​
​multiplied by itself many times.​


​Of course, we could perform this computation using sheer brute​
​force, multiplying out each of the 999 matrices -- but this would take​
​a while.​


​On the other hand, we could go about the multiplications in a more​
​clever way -- for example, if the matrix is​ ​, then​​we could compute​
​,​ ​, and so on until we get to​
​, and then compute​


​.​


​However, this would still require us to compute 14 multiplications,​
​which -- although it is much better than the original 999 -- is still an​
​annoyingly large amount of work, especially once the numbers​
​inside the matrices become large.​


​156​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Inverse Shearings and Rescalings​**


​Fortunately, there is an even better way. First, notice that there is a​
​way to express this matrix as a particular product of shearings and​
​rescalings shown below.​


​The two shearings surrounding the rescaling are special in that they​
​are inverses of each other:​


​As a result, if we multiply 999 copies of the​ _​decomposed​_ ​matrix, we​
​see that all of the shears cancel except the very first and the very​
​last, leaving us with a product of 999 rescaling matrices in between.​


​Justin Skycak |​ **​Linear Algebra​** ​157​


​But rescaling matrices are easy to multiply -- we can just multiply​
​the diagonal entries separately! This leaves us with only 3 remaining​
​matrix multiplications, which isn’t too much work to do by hand.​

## **​Diagonalized Form​**


​In order to reproduce this trick on other matrices, we need to come​
​up with a general method for expressing a matrix​ ​in the​
**​diagonalized​** ​form​


​158​ ​Justin Skycak |​ **​Linear Algebra​**


​where​ ​is a diagonal rescaling matrix and the surrounding​
​matrices​ ​and​ ​are inverses of each other.​


​In order to solve for​ ​and​ ​, it helps to right-multiply​​both sides​
​of the equation by​ ​so that​


​.​


​Then, we can express​ ​in terms of its column vectors​ ​and​ ​in​
​terms of its diagonal entries​ ​, and multiply.​


​We see that the problem amounts to finding pairs of vectors​ ​and​
​scalars​ ​such that​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​159​

## **​Eigenvectors and Eigenvalues​**


​Such vectors​ ​are called​ **​eigenvectors​** ​of the matrix​ ​, and the​
​scalars​ ​that the eigenvectors are paired with are​​called​
**​eigenvalues​** .​


​Essentially, the eigenvectors of a matrix are those vectors that the​
​matrix simply rescales, and the factor by which an eigenvector is​
​rescaled is called its eigenvalue.​


​There is one important constraint:​ **​the eigenvectors​​must be​**
**​nonzero and independent​**, since we need to be able​​to compute the​
​inverse of the matrix that has them as columns.​


​In order to solve for the eigenvector and eigenvalue pairs, we​
​rearrange the equation once more, introducing the identity matrix​

​so that we may factor out the eigenvector​ ​.​


​Since we’re assuming​ ​is not the zero vector, the​​last equation tells​
​us that some combination of not-all-zero multiples of columns of​

​makes the zero vector. Consequently, the columns​​of​
​must be dependent, and thus​


​.​


​160​ ​Justin Skycak |​ **​Linear Algebra​**


​Finally, we have an equation that we can use to solve for​ ​. Then,​
​for each solution that we find for the eigenvalue​ ​, we can simply​

​substitute back into​ ​to solve for the corresponding​
​eigenvector​ ​.​

## **​Demonstration of Diagonalization​**


​Let’s work an example. Say we want to diagonalize the matrix below.​


​We start by solving the equation​ ​for the​
​eigenvalues​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​161​


​Now that we have the eigenvalues​ ​and​ ​, we solve​

​the equation​ ​for corresponding eigenvectors​ ​and​
​.​


​At this point, one option is to write​ ​in terms of​​its components,​

​say​ ​, and simplify the matrix equation into a linear​​system​
​in​ ​and​ ​.​


​We can simplify the system by dividing the top equation by​ ​and​
​the bottom equation by​ ​. This reveals that the two​​equations are​
​really just the same equation.​


​162​ ​Justin Skycak |​ **​Linear Algebra​**


​As a result, they can be reduced down to a single equation, and we​
​can easily solve for​ ​in terms of​ ​.​


​Substituting back into​ ​, we have​


​.​


​In other words, the eigenvector​ ​can be chosen as​​any multiple of​


​the vector​ ​. Intuitively, this makes sense: if​ ​,​​then​
​any multiple​ ​of​ ​will have the same property:​


​We only need to choose a single vector for​ ​. For​​the sake of​


​simplicity, we will choose​ ​to be the least multiple​​of​ ​that​
​has whole number coefficients, and a positive first component. We​
​multiply the vector by​ ​to reach​


​Justin Skycak |​ **​Linear Algebra​** ​163​


​.​


​Thus, we have our first eigenvalue-eigenvector pair!​


​Solving for an eigenvector might seem like a bit of work, but once​
​you go through the process several times, you’ll notice a faster​
​method: we can simply multiply by a diagonal matrix.​


​The diagonal matrix represents the operations we did the long way​
​on the system of equations: dividing the top equation by​ ​and​
​the bottom equation by​ ​.​


​164​ ​Justin Skycak |​ **​Linear Algebra​**


​Then, we just have to choose​ ​as a vector whose dot product with​

​is equal to​ ​. The simplest choice is​ ​, and to​​keep the​
​solution general, we introduce a parameter​ ​to mean​​that​ ​is any​

​nonzero multiple of​ ​.​


​For the purposes of diagonalization, we just need one particular​
​such vector, so we will choose the simplest case,​ ​(and we will​
​implicitly assume such choice when solving for other eigenvectors).​


​Using this method, we reach the same eigenvalue-eigenvector pair.​


​Next we repeat the same process to find the second​
​eigenvalue-eigenvector pair, this time starting with our second​
​eigenvalue​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​165​


​Now that we have our eigenvalues and eigenvectors, we can​
​substitute them into our diagonalization.​

## **​More Complicated Case​**


​In this example, the eigenvalues came out to nice integer values. As​
​we’ll see in the next example, eigenvalues and eigenvectors might​
​be messy, involving roots or even complex numbers.​


​The next example will also be on a​ ​matrix, to illustrate​​that​
​the method of diagonalization is the same even for​
​higher-dimensional matrices.​


​166​ ​Justin Skycak |​ **​Linear Algebra​**


​To diagonalize the matrix​


​we begin by computing the eigenvalues:​


​Justin Skycak |​ **​Linear Algebra​** ​167​


​Then, we solve for the eigenvectors corresponding to the​
​eigenvectors​ ​,​ ​, and​ ​.​


​168​ ​Justin Skycak |​ **​Linear Algebra​**


​Collecting our eigenvalues and eigenvectors, we have​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​169​


​We substitute the eigenvalues and eigenvectors into our​
​diagonalization.​


​Then we compute​ ​.​


​Finally, we’re done!​


​170​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Eigenvalues with Multiple Eigenvectors​**


​When diagonalizing some matrices such as the one below, we may​
​end up with a single repeated eigenvalue, which corresponds to​
​multiple independent eigenvectors.​


​This matrix consists of two distinct eigenvalues, one of which is​
​repeated.​


​Justin Skycak |​ **​Linear Algebra​** ​171​


​When we solve for the eigenvector corresponding to the eigenvalue​

​, we find that the solution consists of combinations​​of​ _​two​_
​independent vectors.​


​We shall use the simplest cases,​ ​and​ ​, to​
​choose two eigenvectors corresponding to the eigenvalue​ ​.​
​Thus, we have two eigenvalue-eigenvector pairs!​


​172​ ​Justin Skycak |​ **​Linear Algebra​**


​We solve for the third eigenvector, corresponding to the eigenvalue​

​, as usual.​


​Then, we can invert the eigenvector matrix and diagonalize.​

## **​Non-Diagonalizable Matrices​**


​Other times, though, we may not find enough independent​
​eigenvectors to create the matrix​ ​.​


​In such cases,​ ​simply cannot be diagonalized (though​​we will later​


​Justin Skycak |​ **​Linear Algebra​** ​173​


​learn a different method to exponentiate such matrices without too​
​much more work).​


​For an example of a non-diagonalizable matrix, consider the matrix​
​below:​


​We are able to solve for the eigenvalues of this matrix:​


​However, when we attempt to solve for the eigenvectors, we reach a​
​problem: there is only one independent vector that satisfies​

​.​


​174​ ​Justin Skycak |​ **​Linear Algebra​**


​We need two pairs of eigenvalues and eigenvectors to diagonalize​
​the matrix, but we have a repeated eigenvalue and only one​
​independent eigenvector corresponding to that eigenvalue.​


​Thus, we simply do not have enough independent eigenvectors to​
​diagonalize the matrix.​

## **​Exercises​**


​Diagonalize the given matrices​ ​, if possible. If​​diagonalization is​
​possible, then use the diagonalization to compute a formula for​ ​.​
​Check your formula on the case​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​175​


​176​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​177​

## **​4.2 Recursive Sequence Formulas via​** **​Diagonalization​**


​In this chapter, we introduce an interesting application of matrix​
​diagonalization: constructing closed-form expressions for recursive​
​sequences.​

## **​Recursive Sequences​**


​A recursive sequence is defined according to one or more initial​
​terms and an update rule for obtaining the next term after some​
​number of previous terms.​


​For example, the sequences​ ​and​ ​given below are​
​arithmetic and geometric sequences given in recursive form.​


​For both of these sequences, it is straightforward to write a​
​closed-form expression for the Nth term:​


​178​ ​Justin Skycak |​ **​Linear Algebra​**


​For other sequences, however, this is not so straightforward. For​
​example, consider the​ **​Fibonacci sequence​**, whose first​​term is​ ​,​
​whose second term is​ ​, and whose successive terms​​are obtained​
​by adding the previous two terms together.​


​The recursive rule for the Fibonacci sequence is as follows:​

## **​Finding a Closed-Form Expression​**


​Notice that we can express the recursive update rule using matrices.​


​Repeatedly multiplying by this matrix, we can write a closed-form​
​expression for the Nth and (N+1)st terms.​


​Justin Skycak |​ **​Linear Algebra​** ​179​


​We can simplify this expression even further by diagonalizing the​
​matrix. First, we solve for the eigenvalues.​


​Now, we find the eigenvectors​ ​and​ ​that correspond​​to the​


​eigenvalues​ ​and​ ​.​


​180​ ​Justin Skycak |​ **​Linear Algebra​**


​Finally, we can diagonalize the matrix.​


​Substituting the diagonalized matrix into the original formula, we​
​are able to simplify so much that we find a closed-form, non-matrix​
​formula for the Nth term of the sequence.​


​Justin Skycak |​ **​Linear Algebra​** ​181​


​This formula might be a little surprising -- the Fibonacci sequence​

​consists only of whole numbers, yet​ ​appears often​​in the​
​formula!​


​However, the formula is indeed correct. We verify the formula for​

​,​ ​, and​ ​-- and it will work on all the other terms​​as well.​


​182​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​183​

## **​Case when Approximation is Required​**


​This same method applies for any recursive sequence, though we​
​may need to diagonalize a higher-dimensional matrix and​
​numerically approximate the eigenvalues.​


​For example, consider the following spin-off of the Fibonacci​
​sequence:​


​First, we express the recursive update rule using matrices, and write​
​a closed-form expression involving an exponentiated matrix​
​multiplying the first few terms.​


​184​ ​Justin Skycak |​ **​Linear Algebra​**


​We omit the steps of diagonalizing the matrix since they should be​
​routine by now -- but it is worthwhile to discuss the method of​
​approximating the eigenvalues.​


​When solving for the eigenvalues, we reach the following equation:​


​This cubic cannot be factored manually -- not even using synthetic​
​division -- since it has no rational roots.​


​Hence, we turn to a graphing utility to approximate a root​

​. Then, we can perform synthetic division with that​​root​
​to factor the polynomial into​


​.​


​We can use the quadratic equation to solve​


​for the other two roots, which we find as​
​and​ ​.​


​Then, with a bit of grunt work, we can use these approximations to​
​solve for the eigenvectors, substitute the diagonalization into the​
​original equation, and multiply to find the formula for the Nth term.​


​Justin Skycak |​ **​Linear Algebra​** ​185​


​The result, with each term rounded to 3 decimal places, is​


​.​


​Lastly, we can verify that the first several terms match up with the​
​actual sequence​ ​.​


​Our estimates are slightly off due to compounded rounding error,​
​but they could be made more accurate by using greater precision in​
​the decimals that occur in the formula for​ ​.​


​186​ ​Justin Skycak |​ **​Linear Algebra​**

## **​Exercises​**


​Use diagonalization to compute a closed-form expression for the​
​recursive sequence​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​187​

## **​4.3 Generalized Eigenvectors and Jordan Form​**


​As we saw previously, not every matrix is diagonalizable, even when​
​allowing complex eigenvalues/eigenvectors. The matrix below was​
​given as an example of a non-diagonalizable matrix.​

## **​Patterns in Powers​**


​However, notice that there’s a pattern in the powers of this matrix.​


​Leveraging this pattern, we can still write a formula for the Nth​
​power of this matrix.​


​188​ ​Justin Skycak |​ **​Linear Algebra​**


​When we conduct this same experiment with a​ ​matrix of​
​similar form, a more general pattern pops up.​


​The pattern is that the numbers are all just binomial coefficients​
​taken from Pascal’s triangle! Writing this pattern more generally for​
​a​ ​square matrix, we have​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​189​


​If we replace the diagonal with another number, say​ ​, then similar​
​experimentation reveals the following formula:​

## **​Jordan Form​**


​These matrices consisting of a diagonal​ ​directly​​below an​
​off-diagonal of​ ​s are called​ **​Jordan blocks​**, and a​​matrix consisting​
​of Jordan blocks is called a​ **​Jordan matrix​** .​


​For example, the matrix below consists of two Jordan blocks. (Note​
​that blank entries correspond to​ ​.)​


​The big question, then, is: which matrices​ ​can be​​expressed as​


​where​ ​is a Jordan matrix?​


​190​ ​Justin Skycak |​ **​Linear Algebra​**


​The answer is quite satisfying: all of them! Thus,​ **​Jordan form​**
**​provides a guaranteed backup plan for exponentiating matrices​**
**​that are non-diagonalizable.​**

## **​Procedure for Finding a Jordan Form​**


​So, how do we construct the matrices​ ​and​ ​? Let’s​​start out like​
​we did with diagonalization, right-multiplying both sides of the​
​equation by​ ​.​


​To keep things simple but interesting enough to generalize our​
​results, let’s assume the following two-block Jordan matrix.​


​Then we have​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​191​


​First of all, since​


​we see that​ ​and​ ​are eigenvectors corresponding​​to the​
​eigenvalues​ ​and​ ​, respectively.​


​This makes intuitive sense because these columns mark the start of​
​the Jordan blocks and thus don’t have a 1 above them -- these​
​columns are perfect diagonals.​


​Before we go on, notice that we can rearrange the above equations​
​as follows:​


​This will be helpful shortly. Now, we move into the more novel​
​cases, beginning by equating the second columns.​


​By rearranging the equation, we come up with an equation similar​
​to those we found for the eigenvectors​ ​and​ ​.​


​192​ ​Justin Skycak |​ **​Linear Algebra​**


​We call​ ​a​ **​generalized eigenvector​** ​of order​ ​for​​the eigenvalue​

​because it solves the equation​ ​, whereas​
​normal eigenvectors (i.e. generalized eigenvectors of order​ ​) for the​

​eigenvalue​ ​solve the equation​ ​.​


​By the same reasoning, we conclude that​ ​is a generalized​
​eigenvector of order​ ​for​ ​, and​ ​is a generalized​​eigenvector​
​of order​ ​for​ ​.​

## **​Demonstration​**


​To conclude this chapter, we walk through an example of​
​exponentiating the non-diagonalizable matrix below by converting it​
​to Jordan form.​


​Justin Skycak |​ **​Linear Algebra​** ​193​


​First, we compute the eigenvalues. In the row manipulations, we use​
​the symbol​ ​to denote matrix entries that change​​but have no​
​consequence when computing the determinant.​


​Now that we have the eigenvalues​ ​repeated twice​​and​
​repeated three times, we solve for the first and​
​second-order generalized eigenvectors for​ ​, and the​​first, second,​
​and third-order generalized eigenvectors for​ ​.​


​194​ ​Justin Skycak |​ **​Linear Algebra​**


​First, we solve for the first-order generalized eigenvector​ ​of​
​.​


​Justin Skycak |​ **​Linear Algebra​** ​195​


​Next, we solve for the second-order generalized eigenvector​ ​of​
​, which is independent of the first-order generalized​
​eigenvector​ ​.​


​196​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​197​


​Before we go on, let’s take inventory of what we have, filling in part​
​of our Jordan form expression.​


​Continuing, we solve for the first-order generalized eigenvector​
​of​ ​.​


​198​ ​Justin Skycak |​ **​Linear Algebra​**


​Then, we solve for the second-order generalized eigenvector​ ​of​
​, which is independent of the first-order generalized​
​eigenvector​ ​.​


​Justin Skycak |​ **​Linear Algebra​** ​199​


​Lastly, we solve for the third-order generalized eigenvector​ ​of​
​, which is independent of the first and second-order​
​generalized eigenvectors​ ​and​ ​.​


​200​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​201​


​Finally, we can fill in the rest of our Jordan form expression.​


​Exponentiating our matrix, we have​


​.​


​To exponentiate the middle matrix, it suffices to exponentiate the​
​two blocks separately. The first block is simple and familiar:​


​202​ ​Justin Skycak |​ **​Linear Algebra​**


​For the second block, we make use of the general formula​


​and find that​


​.​


​Thus, we have​


​.​


​Multiplying out and simplifying, we reach​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​203​


​Lastly, let’s verify this formula on the case​ ​.​


​It checks out!​

## **​Exercises​**


​For each matrix​ ​, express​ ​where​ ​is a Jordan​
​matrix, and use this Jordan expression to compute​ ​. Check your​
​formula on the case​ ​.​


​204​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​205​

## **​4.4 Matrix Exponential and​** **​Systems of Linear Differential Equations​**


​In this chapter, we will learn how to solve systems of linear​
​differential equations. These systems take the form shown below.​

## **​Converting to Matrix Form​**


​We can write the system in matrix form:​


​206​ ​Justin Skycak |​ **​Linear Algebra​**


​Defining​


​the system can be written more compactly as​


​.​


​This bears resemblance to a familiar differential equation​ ​,​
​where​ ​and​ ​are both scalars. We know that the solution​​to such​

​a system is given by​ ​.​


​We infer, then, that the solution to the matrix differential equation is​
​given by​


​.​


​But what does it mean to exponentiate a matrix? How should we​
​compute​ ​?​

## **​Matrix Exponential​**


​Recall that​ ​can be written as the power series​


​Justin Skycak |​ **​Linear Algebra​** ​207​


​.​


​Consequently,​ ​can be written as the power series​


​.​


​Extending this to the matrix exponential​ ​, then,​​we have​


​.​
​Writing​ ​in the form​


​where​ ​is a Jordan matrix, we have​


​.​


​208​ ​Justin Skycak |​ **​Linear Algebra​**


​Thus, computing the exponential of a matrix reduces to the problem​
​of computing the exponential of the corresponding Jordan matrix.​
​As such, we need only investigate how to compute exponentials of​
​Jordan blocks.​


​First, we consider the simplest case: a perfectly diagonal block.​


​In this case, we have​


​Justin Skycak |​ **​Linear Algebra​** ​209​


​.​


​Second, we consider the more involved case: a block with an​
​off-diagonal of​ ​s.​


​210​ ​Justin Skycak |​ **​Linear Algebra​**


​In this case, we have​


​.​


​Taking the convention​ ​when​ ​, we can write​


​.​


​Justin Skycak |​ **​Linear Algebra​** ​211​


​Notice that the entries in the matrix take the form​


​where​ ​is the column index of the matrix. We can​​simplify these​
​expressions as follows:​


​212​ ​Justin Skycak |​ **​Linear Algebra​**


​Thus,​


​.​

## **​Demonstration​**


​Now, we’re ready to run through an example. We shall solve the​
​system below.​


​Justin Skycak |​ **​Linear Algebra​** ​213​


​First, we convert the system to matrix form.​


​Next, we write the matrix in the form​ ​where​ ​is​​a Jordan​
​matrix. We did this with the same matrix in the previous chapter, so​
​we will just assume our previous result.​


​We know that the solution to the system is given by​

​, which we will be able to multiply once we​
​compute​ ​. We break up the computation of​ ​across​​the two​
​blocks within​ ​.​


​214​ ​Justin Skycak |​ **​Linear Algebra​**


​Applying our formula from earlier, we have​


​.​


​Putting this together, we have​


​.​


​Finally, we compute the solution.​


​Justin Skycak |​ **​Linear Algebra​** ​215​

## **​Exercises​**


​Solve each system of linear differential equations by converting it to​


​a matrix equation​ ​and computing the solution​

​.​


​216​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​217​

# **​Solutions​** ​to Exercises​


​218​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​219​

## **​Part 1​**


_​Chapter 1.1​_


_​Chapter 1.2​_


​220​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 1.3​_


​Justin Skycak |​ **​Linear Algebra​** ​221​


_​Chapter 1.4​_


​222​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 1.5​_


​Justin Skycak |​ **​Linear Algebra​** ​223​

## **​Part 2​**


_​Chapter 2.1​_


_​Chapter 2.2​_


​224​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 2.3​_


​Justin Skycak |​ **​Linear Algebra​** ​225​


_​Chapter 2.4​_


​226​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​227​

## **​Part 3​**


_​Chapter 3.1​_


​228​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​229​


_​Chapter 3.2​_


​230​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 3.3​_


​Justin Skycak |​ **​Linear Algebra​** ​231​


​232​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 3.4​_


​Justin Skycak |​ **​Linear Algebra​** ​233​


​234​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​235​

## **​Part 4​**


_​Chapter 4.1​_


​236​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​237​


_​Chapter 4.2​_


​238​ ​Justin Skycak |​ **​Linear Algebra​**


_​Chapter 4.3​_


​Justin Skycak |​ **​Linear Algebra​** ​239​


​240​ ​Justin Skycak |​ **​Linear Algebra​**


​Justin Skycak |​ **​Linear Algebra​** ​241​


_​Chapter 4.4​_


​242​ ​Justin Skycak |​ **​Linear Algebra​**


