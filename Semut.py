
import pefile

print("--------------------------------------------------------------\n")

devby= "PT Media Pengembangan Teknologi Indonesia Jaya\n"
author= "Author: Ananda Rauf Maududi\n"
devdate= "11 September 2023\n"
nameprogram= "Semut(System Malware Mutation Analyst) \n"
version= "Version 1.0.0\n"

print(devby)
print(author)
print(devdate)
print(nameprogram)
print(version)
print("--------------------------------------------------------------\n")

class MenuSemut():
    def menu():
        print("Menu System Malware Mutation Analyst:\n")
        print
        print("1.Analyst file exe")
        print("2.Analyst file pdf")
        print("3.Analyst file jpg")
        print("4.Analyst file png")
        print("5.Analyst file apk")
        print("6.Exit")

class AnExe():
    def anexe(self):
        print("You choose analyst file exe")
        exfile = "nitro_pro10_x64.exe"
        detect = pefile.PE(exfile)
        print(detect)

class AnPdf():
    def anpdf(self):
        print("You choose analyst file pdf")
        pdffile = "Ananda Rauf Maududi_CV.pdf"
        detect = pefile.PE(pdffile)
        print(detect)

class AnJpg():
    def anjpg(self):
        print("You choose analyst file jpg")
        jpgfile = "yournamefile.jpg"
        detect = pefile.PE(jpgfile)
        print(detect)

class AnPng():
    def anpng(self):
        print("You choose analyst file png")
        pngfile = "Activity_diagram_Happy Care.png"
        detect = pefile.PE(pngfile)
        print(detect)

class AnApk():
    def anapk(self):
        print("You choose analyst file apk")
        apkfile = "Happy Care-Skripsi-V1-androidarm-release-debug.apk"
        detect = pefile.PE(apkfile)
        print(detect)

MenuSemut.menu()
chmenu = int(input("Please choose number on menu:"))

anlex = AnExe()
anlpdf = AnPdf()
anljpg = AnJpg()
anlpng = AnPng()
anlapk = AnApk()

if chmenu== 1:
    anlex.anexe()

elif chmenu== 2:
    anlpdf.anpdf()

elif chmenu== 3:
    anljpg.anjpg()

elif chmenu== 4:
    anlpng.anpng()

elif chmenu== 5:
    anlapk.anapk()

elif chmenu== 6:
    print("Thanks for using ^-^\n")
    print("Dont forget share and give star ^-^")
    exit

else:
    print("Not found, sorry!")
    print("Please try again!") 

MenuSemut.menu()
chmenu = int(input("Please choose number on menu:"))




    
