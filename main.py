import tkinter as tk
import time
import pyaudio
import numpy as np
import threading as th

SAMPLE_RATE = 44100

def play( s: pyaudio.Stream, freq: float, duration: float ):
    
    samples = np.sin( np.arange( int( duration * SAMPLE_RATE ) ) * freq * np.pi * 2 / SAMPLE_RATE )
    
    s.write( samples.astype( np.float32 ).tostring() )

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=SAMPLE_RATE,
    frames_per_buffer=1024,
    output=True,
)

speed = ""

CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.' , ' ': 's'
}

def thread_morse_code_encrypt( text ):
    th.Thread( target=morse_code_encrypt, args=( text, ) ).start()

def morse_code_encrypt(st):
    codes = [ CODE[s] for s in st if s in CODE ]
    play_sound( ' '.join( codes ) )

def conf_font( font_size ):
    return ( "Times New Roman", font_size )

def change_speed( slide_value ):
    global speed
    speed = slide_value

def play_sound( text ):
    global speed
    if speed == "":
        speed = 50
    morse_datas = text.split( " " )
    for morse in morse_datas:
        for one_morse in morse:
            if one_morse == ".":
                play( stream, 800, 0.5 / 10 + ( 10 / int( speed ) ) )
            elif one_morse == "-":
                play( stream, 800, 1.5 / 10 + ( 10 / int( speed ) ) )
            # 線と点間の間隔
            time.sleep( 0.5 / 10 + ( 10 / int( speed ) ) )
        # 一語の間隔
        time.sleep( 0.5 / 10 + ( 10 / int( speed ) ) )

root = tk.Tk()

root.geometry( "450x600" )
root.resizable( width=False, height=False )

var_slide = tk.StringVar( root )

label_title = tk.Label( root, text="モールスリスナー", bg="black", fg="white", font=conf_font( 30 ) )
label_title.pack( fill=tk.BOTH, ipady=20 )

frame_text = tk.LabelFrame( root, text="convert from", font=conf_font( 25 ) )
frame_text.pack( fill=tk.BOTH, padx=20, pady=20 )

text_area = tk.Text( frame_text, height=10 )
text_area.pack()

frame_speed_slide = tk.LabelFrame( root, text="スピード", font=conf_font( 25 ) )
frame_speed_slide.pack( fill=tk.BOTH, padx=20 )

slide_speed = tk.Scale( frame_speed_slide, orient="horizontal", variable=var_slide, from_=50, to=250, command=lambda e: change_speed( var_slide.get() ) )
slide_speed.pack( fill=tk.BOTH, pady=( 0, 30 ), padx=20 )

button_play = tk.Button( root, text="再生", font=conf_font( 30 ), command=lambda: thread_morse_code_encrypt( text_area.get( "1.0", "end" ).upper() ) )
button_play.pack( pady=( 30, 0 ) )



if __name__ == "__main__":
    root.mainloop()
    