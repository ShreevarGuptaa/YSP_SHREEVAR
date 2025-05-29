## Visual Encodings

### Difficulty Level: Easy

### Instructions
Look up what Steganography is and think about how it is different from encryption. Share your thoughts. Play with this [site](https://stylesuxx.github.io/steganography/) and share your understanding of what's happening. 

1. How does the information get encrypted in a file? Can we use any file format? Try with all that you can.
2. How does it get decrypted?
3. What does the binary representation of a message mean? Why are you provided with it?

##################################################################################################################################

SHREEVAR'S RESEARCH:
I played around with the website a bit and  this is what I understood so far. The more text we want to hide, the larger the image has to be. I saw that my text was converted to a binary format and hidden in the image I uploaded. I downloaded both of them and noticed that the image with the hidden message was slightly larger than the original image.

## ANSWER 1:
Information in a file gets encrypted by applying a cryptographic algorithm that transforms readable data into unreadable data using a specific key. This encryption can be done using symmetric algorithms like AES or asymmetric algorithms like RSA, depending on the use case. The file's content—whether it's text, image, audio, or video—is first read in its raw binary form and then encrypted. You can encrypt virtually any file format because encryption operates on the file's data, not its type. Common file formats like .txt, .pdf, .jpg, .mp3, .docx, and even .exe can all be encrypted. However, once encrypted, the file is no longer usable in its normal application.

## ANSWER 2:
Decryption involves taking the encrypted file and applying a decryption algorithm with the correct key to restore the original readable data. In symmetric encryption, the same key used to encrypt is used to decrypt. In asymmetric encryption, a private key is used to decrypt the message that was encrypted with the corresponding public key. The decrypted content must be saved or interpreted properly to return to its original format and functionality, such as displaying an image, playing audio, or opening a document.

## ANSWER 3:
The binary representation of a message is the conversion of each character in the message into its binary equivalent, typically using an encoding standard like ASCII. For eg, "A" is 65 in ASCII. This form is essential in computing and especially in techniques like steganography, where the individual bits of a message are embedded into the least significant bits of image pixels. You're provided with the binary representation so you can understand how your message is being processed and embedded at the bit level. It also helps in verifying or troubleshooting the encoding process, especially when using tools that manipulate data at the binary layer, such as the steganography demo site you explored.

SOURCES: https://deviceauthority.com/symmetric-encryption-vs-asymmetric-encryption/
         https://www.geeksforgeeks.org/image-based-steganography-using-python/