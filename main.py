import random
import cv2


def neg(img):
    height, width, _ = img.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pix = img[i, j]
            pix[0] = 255 - pix[0]
            pix[1] = 255 - pix[1]
            pix[2] = 255 - pix[2]
            img[i, j] = pix

    return img


def noise(img):
    height, width, _ = img.shape

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            noise_kf = random.randint(-25, 25)
            pix = img[i, j]

            pix[2] = pix[2] + noise_kf
            if pix[2] < 0:
                pix[2] = 0
            if pix[2] > 255:
                pix[2] = 255

            pix[1] = pix[1] + noise_kf
            if pix[1] < 0:
                pix[1] = 0
            if pix[1] > 255:
                pix[1] = 255

            pix[0] = pix[0] + noise_kf
            if pix[0] < 0:
                pix[0] = 0
            if pix[0] > 255:
                pix[0] = 255

            img[i, j] = pix

    return img


img = cv2.imread('trip.jpg')
img = cv2.resize(img, (500, 700))
cv2.imshow("original", img)

img = neg(img)
cv2.imshow("Output negative", img)

img = noise(img)
cv2.imshow("Noise Output", img)
cv2.imwrite("trip_noise_neg.jpg", img)

img = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("denoised Output", img)
cv2.imwrite("trip_noise_neg_denoise.jpg", img)

img = cv2.Canny(img, 100, 200)
cv2.imshow("denoised vector output Output", img)
cv2.imwrite("trip_noise_neg_vector.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
