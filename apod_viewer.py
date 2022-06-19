# apod_viewer 
import tkinter, requests, webbrowser
from tkinter import filedialog
from tkcalendar import DateEntry # To use with auto-py-to-exe, add hidden imports of module 'babel.numbers' (without quotes)
from PIL import ImageTk, Image
from io import BytesIO


#Define window
root = tkinter.Tk()
root.title('APOD Photo Viewer')
root.iconbitmap('rocket.ico')

#Define fonts and colors
text_font = ('Times New Roman', 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"
root.config(bg=nasa_blue)

#Define functions
def get_request():
    """Get request data from NASA APOD API"""
    global response

    #Set the parameters for the request
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'DEMO_KEY' #USE YOUR OWN API KEY!!!!
    date = calander.get_date()
    querystring = {'api_key':api_key, 'date':date}

    #Call the request and turn it into a python usable format
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    #print(response)
    #Update output labels
    set_info()


def set_info():
    """Update output labels based on API call"""
    #Example response
    '''{
        'copyright': 'John Kraus', 
        'date': '2021-02-22', 
        'explanation': "What's that on either side of the Moon? Starships. Specifically, they are launch-and-return reusable rockets being developed by SpaceX
        to lift cargo and eventually humans from the Earth's surface into space.  The two rockets pictured are SN9 (Serial Number 9) and SN10 which were 
        captured near their Boca Chica, Texas launchpad last month posing below January's full Wolf Moon. The Starships house liquid-methane engines inside 
        rugged stainless-steel shells. SN9 was test-launched earlier this month and did well with the exception of one internal rocket that failed to relight 
        during powered descent.  SN10 continues to undergo ground tests and may be test-launched later this month.", 
        'hdurl': 'https://apod.nasa.gov/apod/image/2102/StarshipsMoon_Kraus_2048.jpg', 
        'media_type': 'image', 
        'service_version': 'v1', 
        'title': 'Moon Rising Between Starships', 
        'url': 'https://apod.nasa.gov/apod/image/2102/StarshipsMoon_Kraus_1080.jpg'}'''

    #Update the picture date and explanation
    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'])

    #We need to use 3 images in other functions; an img, a thumb, and a full_img
    global img 
    global thumb
    global full_img

    url = response['url']

    if response['media_type'] == 'image':
        #Grab the photo that is stored in our response.
        img_response = requests.get(url, stream=True)

        #Get the content of the response and use BytesIO to open it as an an image
        #Kepp a reference to this img as this is what we can use to save the image (Image not PhotoImage)
        #Create the full screen image for a second window 
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))

        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,200))
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumbnail image
        picture_label.config(image=thumb)
    elif response['media_type'] == 'video':
        picture_label.config(text=url, image='')
        webbrowser.open(url)


def full_photo():
    """Open the full size photo in a new window"""
    top = tkinter.Toplevel()
    top.title('Full APOD Photo')
    top.iconbitmap('rocket.ico')

    #Load the full image to the top window
    img_label = tkinter.Label(top, image=full_img)
    img_label.pack()


def save_photo():
    """Save the desired photo"""
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Image", filetypes=(("JPEG", "*.jpg"), ("All Files", "*.*")))
    img.save(save_name + ".jpg")



#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for the input frame
calander = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = tkinter.Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = tkinter.Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = tkinter.Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)

calander.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Layout for the output frame
picture_explanation = tkinter.Label(output_frame, font=text_font, bg=nasa_white, wraplength=600)
picture_label = tkinter.Label(output_frame)
picture_date = tkinter.Label(output_frame, font=text_font, bg=nasa_white)

picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)
picture_date.grid(row=1, column=1, padx=10)

#Get today's photo to start with
get_request()

#Run the root window's main loop
root.mainloop()