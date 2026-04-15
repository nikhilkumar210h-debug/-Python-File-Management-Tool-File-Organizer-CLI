import os

path = input("Enter your path: ")

def rename():
    pn = 1
    j = 1
    t = 1
    pd = 1
    mp4 = 1
    mp3 = 1
    docx = 1
    webp = 1
    try:
        files = sorted(os.listdir(path))

        for i in files:
            if i.lower().endswith(".png"):
                os.rename(os.path.join(path, i), os.path.join(path, f"png {pn}.png"))
                pn += 1

            elif i.lower().endswith(".jpg"):
                os.rename(os.path.join(path, i), os.path.join(path, f"img {j}.jpg"))
                j += 1

            elif i.lower().endswith(".pdf"):
                os.rename(os.path.join(path, i), os.path.join(path, f"pdf {pd}.pdf"))
                pd += 1

            elif i.lower().endswith(".txt"):
                os.rename(os.path.join(path, i), os.path.join(path, f"textfile {t}.txt"))
                t += 1

            elif i.lower().endswith(".mp4"):
                os.rename(os.path.join(path, i), os.path.join(path, f"video {mp4}.mp4"))
                mp4 += 1
            elif i.lower().endswith(".mp3"):
                os.rename(os.path.join(path, i), os.path.join(path, f"audio {mp3}.mp3"))
                mp3 += 1
            elif i.lower().endswith(".docx"):
                os.rename(os.path.join(path, i), os.path.join(path, f"document {docx}.docx"))
                docx += 1
            elif i.lower().endswith(".webp"):
                os.rename(os.path.join(path, i), os.path.join(path, f"image {webp}.webp"))
                webp += 1


        print("Renaming done ✅")

    except Exception as e:
        print("Error:", e)

rename()