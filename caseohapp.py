# imports
import sys, os, ctypes
import pyautogui
from datetime import datetime, date
from OpenGL.GLUT import *
from OpenGL.GL import *
from PIL import Image
import pygame

#vars
bday_case = "2027-5-9" #bday
case_target = datetime.strptime(bday_case, "%Y-%m-%d").date() #targ
days_until = (case_target - date.today()).days #until
print(days_until) #debug
w, h = pyautogui.size() #get screen size
#vars end

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


#song (strawberry cheesecaaaaaæaaaaaaæaaæææaaaaaàaaaaaaaake)
def init_audio():
    pygame.mixer.init()
    
    pygame.mixer.music.load(resource_path("strawberry-cheesecake.mp3"))
    
    pygame.mixer.music.play(-1)


#caseoh
def img():
    try:
        raw_img = Image.open(resource_path("caseoh.png")).transpose(Image.FLIP_TOP_BOTTOM)
        img_w, img_h = raw_img.size 
        data = raw_img.convert("RGBA").tobytes("raw", "RGBA")
    except Exception as e:
        print(f"failure: {e}")
        return

    tex_id = glGenTextures(1)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_w, img_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

    glColor4f(1.0, 1.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex2f(-1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex2f(1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex2f(1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex2f(-1.0, 1.0)
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
    glDeleteTextures([tex_id])

#literally what it's named
def dummy_display():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    img() 

    glutSwapBuffers()

#escape
def keyboard_func(key, x, y):
    if key == b'\x1b': #escape
        if bool(glutLeaveMainLoop):
            glutLeaveMainLoop()
        else:
            os._exit(0)

#main
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 400)
    glutInitWindowPosition((w - 600) // 2, (h - 400) // 2)
    
    title = f"{days_until} more days 'til CaseOh's birthday, he gonna be 29 years old! (unc)" #absolute UNC!
    mwin = glutCreateWindow(title.encode("utf-8"))

    init_audio()

    if bool(glutSetOption):
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)

    glutDisplayFunc(dummy_display)
    glutKeyboardFunc(keyboard_func)
    glutMainLoop()

# if __name__ == '__main__': main()
if __name__ == '__main__':
    main()
