By
Mark Prigg

Facebook has created an algorithm that can pick a face out of a crowd almost as accurately as a human.

Called DeepFace, it uses technology the firm bought when it acquired Israeli startup face.com last year.

Its creators say it pick a face out of a crowd with 97.25 per cent accuracy.

DeepFace uses a 3-D model to rotate faces, virtually, so that they face the camera. Image (a) shows the original image, and (g) shows the final, corrected version which the software can then attempt to recognise.

Yaniv Taigman and colleagues at Facebook's AI lab found a way to build a 3D model of a face from a photo that can be rotated into the best position for the algorithm to start matching.

They then used a neural network that had been trained on a massive database of faces to try and match the face with one in a test database of more than 4 million images, containing more than 4000 separate identities, each one labelled by humans.

'We revisit both the alignment step and the representation step by employing explicit 3D face modeling in order to apply a piecewise affine transformation, and derive a face representation from a nine-layer deep neural network,' the team wrote.

The system can now identify faces at virtually the same level of accuracy as a human

The team achieved 97.25 per cent accuracy on the test data that contained more than 13,000 images of faces collected from the web.

A test using real people recruited on Amazon's Mechanical Turk crowdsourcing site managed 97.5 per cent.

Details will be presented at the Computer Vision and Pattern Recognition conference in Columbus, Ohio, in June.

Experts say Facebook could use it to identify all of a user's real friends are.

'They could identify every one of your friends in all of your photos,' Christopher Kanan of the California Institute of Technology told New Scientist.

'This would let them know who your real friends are – people you actually hang out with in the real world.'

@highlight

DeepFace was trained by analysing pictures uploaded to Facebook

@highlight

Can 'spin' a head to get a clear look at the face using 3D modelling