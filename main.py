import customtkinter
import tkinter
from translator import Translator
from countries import country_codes



# imports and defining variables for future use, as well as instantialising class objs, setting up attribs, etc.

selected_language_from = ""
selected_language_to = ""

language_names = list(country_codes.keys())
language_codes = list(country_codes.values())

tk = customtkinter

root_tk = customtkinter.CTk()
root_tk.geometry("1200x750")
root_tk.resizable(width=0, height=0)
root_tk.title("translat0r")
customtkinter.set_appearance_mode("Dark")


translat0r = Translator()




# setting up functions

def translate_from(lang_name: str): # takes language name as a param, sets the caption of the "translate from: " button to the according name, returns said name
    global selected_language_from
    selected_language_from = lang_name
    translate_from_language_buttom.configure(text=f"FROM: {lang_name}")
    language_from_translate = lang_name

    return language_from_translate
   

def translate_to(lang_name: str): # takes language name as a param, sets the caption of the "translate to" button to the according name, returns said name
    global selected_language_to
    selected_language_to = lang_name
    
    translate_to_language_button.configure(text=f"TO: {lang_name}")
    language_to_translate = lang_name

    return language_to_translate

def set_up_translation(selected_language_from: str, selected_language_to: str, translator: Translator):
    lang_from_code = country_codes[selected_language_from].split("-")[0]
    lang_to_code = country_codes[selected_language_to].split("-")[0]
    input_text = text_input_field.get()
    translation = translator.translate(input_text, lang_from_code, lang_to_code)
    text_output_field.configure(text=translation)




def hide_frame(frame): # lazy workaround to destroy a frame
    frame.pack_forget()


def language_menu_from(): # create a scrollable frame, embed buttons into said frame, additional function to destroy (hide) said frame. (if better thing exists - pls forgive me, i'm noob)
    def close_frame():
        scroll_frame.pack_forget()
    
    scroll_frame = customtkinter.CTkScrollableFrame(root_tk, width=200, height=200)
    scroll_frame.pack()
    
    close_button = customtkinter.CTkButton(scroll_frame,  border_width=1, width=25, height=25,  text="x", command=close_frame)
    close_button.pack(anchor="ne") # Position close_button in the top-right corner

    current_lang_label = customtkinter.CTkLabel(scroll_frame,
        width=200,
        height=25,
        fg_color = "transparent",
        text = f"TRANSLATE FROM: ")
    current_lang_label.pack(anchor="n", side="top")
        
    for lang_name in language_names:
        new_lang_button = customtkinter.CTkButton(scroll_frame,
            width=200,
            height=25,
            corner_radius=0,
            text=f"{lang_name}",
            command=lambda ln = lang_name: (hide_frame(scroll_frame),translate_from(ln)))
                
            
            
        new_lang_button.pack()

def language_menu_to(): # same as line 56
    def close_frame():
        scroll_frame.pack_forget()
    
    scroll_frame = customtkinter.CTkScrollableFrame(root_tk, width=200, height=200)
    scroll_frame.pack()
    
    close_button = customtkinter.CTkButton(scroll_frame,  border_width=1, width=25, height=25,  text="x", command=close_frame)
    close_button.pack(anchor="ne") # Position close_button in the top-right (north-east) corner


    current_lang_label = customtkinter.CTkLabel(scroll_frame,
        width=200,
        height=25,
        fg_color = "transparent",
        text = f"TRANSLATE TO: ")
    current_lang_label.pack()
        
    for lang_name in language_names:
        new_lang_button = customtkinter.CTkButton(scroll_frame,
            width=200,
            height=25,
            corner_radius=0,
            text=f"{lang_name}",
            command=lambda ln = lang_name: (hide_frame(scroll_frame),translate_to(ln)))
                
            
            
        new_lang_button.pack()


# setting up various labels and buttons

text_label = customtkinter.CTkLabel(master=root_tk, 
text="translat0r", width=5, height=1, bg_color="transparent", font=("Roboto-light", 32)).place(relx=0.5, y=20, anchor="center")

text_input_field = customtkinter.CTkEntry(root_tk, height=500, width=350, 
fg_color="grey", border_width=1, border_color="white", font=("Roboto", 14), justify="left")
text_input_field.insert(customtkinter.END, "Input your text...")
text_input_field.place(x=1, y=40)
input_field_width = text_input_field.winfo_width()


text_output_field = customtkinter.CTkLabel(root_tk, height=500, width=350,
 fg_color="grey", font=("Roboto", 14))
text_output_field.configure(text="Translated Text: ")
text_output_field.place(x=849, y=40)


translate_from_language_buttom = customtkinter.CTkButton(root_tk,
    width=350,
    height=50,
    text="TRANSLATE FROM: ",
    command= language_menu_from,
    border_color = "white",
    font = ("Roboto", 32) )
translate_from_language_buttom.place(x=1, y=545)


translate_to_language_button = customtkinter.CTkButton(root_tk, 
    width=350,
    height=50,
    text="TRANSLATE TO: ",
    border_color = "white",
    font = ("Roboto", 32),
    command = language_menu_to)
translate_to_language_button.place(x=849, y=545)


translate_button = customtkinter.CTkButton(root_tk, width=220, height=50,
    border_width=1, corner_radius=5, text="Translate!", font=("Roboto", 32),
    command=lambda: ( set_up_translation( selected_language_from, selected_language_to, translat0r)) 
) 

translate_button.place(relx=0.5, y=725, anchor="s", x=-input_field_width / 2) 

# starting the main loop for UI 

root_tk.mainloop()

