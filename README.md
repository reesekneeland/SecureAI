# SecureAI
![image](https://user-images.githubusercontent.com/77468346/153016635-d579647c-807b-4891-8793-88d93bdc9acf.png)

### Harness the power of machine learning to test the strength of your passwords, and generate an encrypted piece of digital art depicting the keys to your digital world. Compete against your friends!
A code repository for the SecureAI project created during Minnehack 2022, under the prompt "Write a piece of software that helps make digital privacy accessible". Clip guided diffusion code provided by Clay Mullis, which you can find here: https://github.com/afiaka87/clip-guided-diffusion.

**PROJECT IS NO LONGER LIVE FOR NEW SUBMISSIONS AND VOTING.**

![00_00](https://user-images.githubusercontent.com/77468346/153016497-4f2172ad-ebde-41fa-a3a4-0d770308335d.gif)

## Inspiration
Our project was inspired by a creative interpretation of the prompt. Digital privacy is the protection of a human’s identity when accessing the web to manage businesses, communicate with each other, and to gather useful information that is inaccessible through human interaction. However, your digital identity is vulnerable to many kind of internet attacks, which could affect one’s lifestyle and well-being, the most vulnerable piece of which is the password.
The traditional digital security model has us hiding our passwords, the key to our digital privacy, behind walls of encryption and in isolation. What if we could build a tool that leverages AI to securely bring your password into the open? By analyzing a password’s strength, generating a secure encrypted image from it, and pit user’s best passwords against each other in a digital artwork contest, we plan to do just that. Our group’s love of CUDA leveraged AI generation techniques, scratch built web design, digital artwork, and raw competition inspired us to create this unique piece of software.

![Screenshot from 2022-01-23 15-44-33](https://user-images.githubusercontent.com/77468346/153016721-7dd2bffe-fff0-4215-8ddd-8bf1e921b607.png)

## What it does
The application we built takes in a password as a text input from the user, and runs a data driven password analytics engine to give the provided password a score between 0-100. This feature allows the user the ability to test their password strength, and ensure that the passwords they sign up to their digital services with are secure. Our application then uses that score to configure and train a guided diffusion image generation algorithm running on pytorch machine learning frameworks to generate a 256x256 image from the users password. This CUDA powered tool has a small amount of inherent randomness built in to create completely unique images for every submission, these images are then posted to the public gallery, where the password score and (optionally) the user who submitted it are visible to the public, keeping the original password secure. The digital artworks posted to the gallery can then be voted on by users, with the most liked images rising to the top. This presents a unique opportunity to try and out-password your friends! The complexity of the images rises with the complexity of the provided password, so the more interesting passwords generate more interesting images. Can you make a password creative enough to out-generate your friends? Go ahead and find out!

![Screenshot from 2022-01-23 14-07-14](https://user-images.githubusercontent.com/77468346/153016280-326f2afb-4782-467a-84e0-30782b3c4714.png)

## How we built it
The web interface was coded from scratch in Node.js, and is hosted locally on a pc using a 3080ti to run the image generation algorithm, which utilizes a pytorch framework and some ImageNet training data to generate an image based on the provided text. The image is then fed back into our web interface and displayed alongside the number of likes it has and the password strength score displayed underneath it.
## Challenges we ran into
We initially tried hosting our application inside a flask container, but ran into a multitude of issues with the library setup and eventually abandoned it to create our own website from scratch . We also put a lot of effort into getting the machine learning libraries to behave the way we wanted, with the majority of our time was spend debugging and configuring our image generation software to the parameters we wanted.
## Accomplishments that we're proud of
We have a working custom web service that leverages some advanced machine learning functionality to create unique digital art and encourage people to step up their password security. We think our project is as creative as they come and are proud of the finished product.
## What we learned
We learned a tremendous amount about front end web design, and pytorch libraries throughout this process, these fields are so deep that there is always more to learn.
## What's next for SecureAI
Our project serves mostly as a proof of concept, there is so much more we could do with this idea, from integrating password managers to provide a collage of your digital logins, to wider social features creating head to head competition scores and public leaderboards. There is always room to improve the finer aspects of the image generation and many many other areas.

## Developer Credits
Reese Kneeland
Jordyn Ojeda
Jovan Petrovic
Skylan Recana
