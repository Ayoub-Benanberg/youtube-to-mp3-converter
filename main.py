from tkinter import Tk, Label, Entry, Button, messagebox
from pytube import YouTube

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        title = yt.title.replace(" ", "_")  # Replace spaces with underscores
        audio_stream.download(output_path=output_path, filename=title+".mp3")  # Use video title as filename
        return f"{output_path}/{title}.mp3"  # Return the path to the downloaded audio file
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def convert():
    url = url_entry.get()
    output_path = output_entry.get()

    audio_file = download_audio(url, output_path)
    if audio_file:
        messagebox.showinfo("Success", f"MP3 file saved as {audio_file}")

root = Tk()
root.title("YouTube to MP3 Converter")

url_label = Label(root, text="YouTube URL:")
url_label.grid(row=0, column=0)

url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2)

output_label = Label(root, text="Output Directory:")
output_label.grid(row=1, column=0)

output_entry = Entry(root, width=50)
output_entry.grid(row=1, column=1)

convert_button = Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, pady=10)

root.mainloop()
