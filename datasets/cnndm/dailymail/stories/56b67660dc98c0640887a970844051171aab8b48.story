Parents often ponder what their children will look like when they grow up.

Now, a computer could answer the question in less than a minute.

University of Washington researchers have developed software that automatically generates images of a young child's face as it ages through a lifetime.

Scroll down for video

Using one photo of a 3 year-old, the software automatically renders images of his face at multiple ages while keeping his identity (and the milk moustache)

The technique is the first fully automated approach for aging babies to adults that works with variable lighting, expressions and poses.

‘Aging photos of very young children from a single photo is considered the most difficult of all scenarios, so we wanted to focus specifically on this very challenging case,’ said Ira Kemelmacher-Shlizerman, an assistant professor of computer science and engineering at the University of Washington.

‘We took photos of children in completely unrestrained conditions and found that our method works remarkably well.’

The research team has posted a paper on the new technique and will present its findings at the June IEEE Computer Vision and Pattern Recognition conference in Columbus, Ohio.

The software determines the average pixel arrangement from thousands of random Internet photos of faces in different age and gender brackets.An algorithm then finds correspondences between the averages from each bracket and calculates the average change in facial shape and appearance between ages.These changes are then applied to a new child's photo to predict how she or he will appear for any subsequent age up to 80.The researchers tested their rendered images against those of 82 actual people photographed over a span of years.People could not distinguish between the real and rendered images.

The shape and appearance of a baby's face – and variety of expressions – often change drastically by adulthood, making it hard to model and predict that change.

This technique leverages the average of thousands of faces of the same age and gender, then calculates the visual changes between groups as they age to apply those changes to a new person's face.

In an experiment asking random users to identify the correct aged photo for each example, they found that users picked the automatically rendered photos about as often as the real-life ones.

‘Our extensive user studies demonstrated age progression results that are so convincing that people can't distinguish them from reality,’ said co-author Steven Seitz, Professor of Computer Science and Engineering.

‘When shown images of an age-progressed child photo and a photo of the same person as an adult, people are unable to reliably identify which one is the real photo.’

Spitting image: Here, real photos of a child (right in each pair) are compared to images that used the software (left in each pair) to generate an aged face, with surprisingly accurate results. As the software only deals with faces, however, hair and other features like clothing are added artificially

Real-life photos of children are difficult to age-progress, partly due to variable lighting, shadows, funny expressions and even milk moustaches.

To compensate for these effects, the algorithm first automatically corrects for tilted faces, turned heads and inconsistent lighting, then applies the computed shape and appearance changes to the new child's face.

Perhaps the most common application of age progression work is for rendering older versions of missing children.

These renderings usually are created manually by an artist who uses photos of the child as well as family members, and editing software to account for common changes to a child's face as it ages, including vertical stretching, wrinkles and a longer nose.

But this process takes time, and it's significantly harder to produce an accurate image for children younger than age five, when facial features more closely resemble that of a baby.

Using the software, parents could discover what their children will look like when they are older

In each pair of these images showing babies growing up, the rendered image is on the left and a real photo of the same age is on the right (again, hair and clothing are artificially added)

Can you tell which is which? In tests, people were unable to discern between real and rendered images

Through the ages: The software scans thousands of Internet pictures to create an 'average face' before applying its aging algorithm

The automatic age-progression software can run on a standard computer and takes about 30 seconds to generate results for one face. It is not yet available to the public, however.

While this method considered gender and age, the research team also hopes to incorporate other identifiers such as ethnicity, and cosmetic factors such as hair whitening and wrinkles, to build a robust enough method for representing every human face.

‘I'm really interested in trying to find some representation of everyone in the world by leveraging the massive amounts of captured face photos,’ Kemelmacher-Shlizerman said.

‘The aging process is one of many dimensions to consider.’

The company says they will soon have a mobile app and website tool where people can try the technology by uploading their own photos.

@highlight

Researchers have developed software that can predict aging

@highlight

It shows how a baby will look from birth up until age 80

@highlight

An algorithm scans thousands of Internet photos to get an 'average face'

@highlight

It can then apply what it learns to a new baby's face

@highlight

People could not tell the difference between real and rendered images