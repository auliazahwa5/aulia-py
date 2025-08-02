# import library pygame dan sys
import pygame
import sys

#inisialisasi pygame
pygame.init()

#Warna yang akan digunakan
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

# ukuran layar kalkulator
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kalkulator Pygame")

# font untuk angka dan hasil
font = pygame.font.SysFont(None, 40)
display_font = pygame.font.SysFont(None, 60)


#daftar tombol kalkulator
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'], 
    ['0', 'C', '=', '+']
]

#ukuran setiap tombol
button_width = WIDTH // 4
button_height = (HEIGHT - 100) // 4

# variabel untuk menyimpan input pengguna
input_str = ""

# fungsi untuk menggambar tombol-tombol kalkulator
def draw_buttons():
    for i in range(4): # baris tombol
        for j in range(4): #kolom
            #membuat kotak tombol
            rect = pygame.Rect(j * button_width, 100 + i * button_height, button_width, button_height)
            pygame.draw.rect(screen, GRAY, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 2)

            #menampilkan teks tombol
            text = font.render(buttons[i][j], True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

#fungsi untuk menggambar layar atas
def draw_display():
    rect = pygame.Rect(0, 0, WIDTH, 100)
    pygame.draw.rect(screen, LIGHT_GRAY, rect)

# menampilkan teks input atau hasil di layar atas
    text = display_font.render(input_str, True, BLACK)
    text_rect = text.get_rect(right=WIDTH - 10, centery=50)
    screen.blit(text, text_rect)

running = True
while running:
    screen.fill(WHITE) #membersihkan layar setiap frame
    draw_display() #menampilkan input/hitung di atas
    draw_buttons() #menampilkan tombol

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #logika tombol
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y > 100:
                row = (y - 100) // button_height
                col = x // button_width
                button = buttons[row][col]

                if button == 'C':
                    input_str = ""
                elif button == '=':
                    try:
                        input_str = str(eval(input_str))
                    except:
                        input_str = "Error"
                else:
                    input_str += button

    pygame.display.flip()

pygame.quit()
sys.exit()