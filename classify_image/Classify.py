from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from PIL import Image
from django.conf import settings
import os
from skimage.io import imread


# def get_model():
#         model = load_model(os.path.join(settings.MEDIA_ROOT, 'Model/my_model.h5'))
#         dogchecker = tf.keras.Model(model.input,model.layers[-2].output)
#         return model,dogchecker
        
def predict(image,loaded_model,dogchecker):
        img = Image.open(image);#load_img(image, target_size=(224, 224), color_mode = "rgb")
        img = img.convert('RGB')
        img = img.resize((224, 224))
        img.save(os.path.join(settings.MEDIA_ROOT, 'Model/test.jpg'))
        img=imread(os.path.join(settings.MEDIA_ROOT, 'Model/test.jpg'))
        img = preprocess_input(img)
        probs_dogs = dogchecker.predict(np.expand_dims(img, axis=0))
        prediction  = np.argmax(probs_dogs)
        dog_image=1
        if ((prediction <= 268) & (prediction >= 151)):
                dog_image = 1
        else:
                dog_image = 0
        probs = loaded_model.predict(np.expand_dims(img, axis=0))
        print(probs[0,:].argsort()[-5:])
        return probs,dog_image



label_maps_rev={0: 'n02113799-Standard Poodle', 1: 'n02102318-Cocker Spaniel', 2: 'n02088466-Bloodhound', 3: 'n02112018-Pomeranian', 4: 'n02110958-pug', 5: 'n02113023-Pembroke Welsh Corgi', 6: 'n02099849-Chesapeake Bay Retriever', 7: 'n02101388-Brittany spaniel', 8: 'n02104365-Schipperke', 9: 'n02097298-Scotch Terrier', 10: 'n02086646-Blenheim Spaniel', 
11: 'n02106166-Border Collie', 12: 'n02088364-Beagle', 13: 'n02109525-Saint Bernard', 14: 'n02112137-Chow Chow', 15: 'n02098286-West Highland White Terrier', 16: 'n02091244-Ibizan Hound', 17: 'n02088094-Afghan Hound', 18: 'n02099267-Flat Coated Retriever', 19: 'n02091467-Norwegian Elkhound', 20: 'n02086240-Shih Tzu',
 21: 'n02105251-Briard', 22: 'n02111129-Leonberger', 23: 'n02106030-Collie', 24: 'n02094258-Norwich Terrier', 25: 'n02094114-Norfolk Terrier', 26: 'n02111889-Samoyed', 27: 'n02107574-Greater Swiss Mountain Dog', 28: 'n02113186-Cardigan Welsh Corgi', 29: 'n02093859-Kerry Blue Terrier', 30: 'n02100877-Irish Setter',
31: 'n02107142-Doberman', 32: 'n02087046-Toy Terrier', 33: 'n02085936-Maltese', 34: 'n02089078-Black And Tan Coonhound', 35: 'n02100735-English_setter', 36: 'n02091032-Italian Greyhound', 37: 'n02094433-Yorkshire Terrier', 38: 'n02105056-Belgian Sheepdog', 39: 'n02108089-Boxer', 40: 'n02102040-English Springer', 
41: 'n02113624-Toy Poodle', 42: 'n02086910-Papillon', 43: 'n02116738-African Hunting Dog', 44: 'n02105162-Malinois', 45: 'n02112350-Keeshond', 46: 'n02108422-Bull Mastiff', 47: 'n02110063-Malamute', 48: 'n02086079-Pekingese', 49: 'n02090379-Redbone Coonhound', 50: 'n02087394-Rhodesian Ridgeback',
51: 'n02091831-Saluki', 52: 'n02085620-Chihuahua', 53: 'n02092002-Scottish Deerhound', 54: 'n02099601-Golden Retriever', 55: 'n02105855-Shetland Sheepdog', 56: 'n02097047-Miniature Schnauzer', 57: 'n02096051-Airedale', 58: 'n02106662-German Shepherd', 59: 'n02101556-Clumber Spaniel', 60: 'n02102177-Welsh Springer Spaniel',
61: 'n02113712-Miniature Poodle', 62: 'n02112706-Brabancon Griffon', 63: 'n02089973-English Foxhound', 64: 'n02099712-Labrador Retriever', 65: 'n02093991-Irish Terrier', 66: 'n02106550-Rottweiler', 67: 'n02109961-Eskimo Dog', 68: 'n02091635-Otterhound', 69: 'n02096294-Australian Terrier', 70: 'n02110806-basenji',
71: 'n02096437-Dandie Dinmont Terrier', 72: 'n02091134-Whippet', 73: 'n02098413-Lhasa Apso', 74: 'n02104029-Kuvasz', 75: 'n02115641-Dingo', 76: 'n02108000-Entlebucher Mountain Dog', 77: 'n02111500-Great Pyrenees', 78: 'n02100236-German Short Haired Pointer', 79: 'n02115913-dhole', 80: 'n02097658-Silky Terrier',
81: 'n02107908-Appenzeller', 82: 'n02097474-Tibetan terrier', 83: 'n02106382-Bouvier Des Flandres', 84: 'n02107683-Bernese Mountain Dog', 85: 'n02105641-Old English Sheepdog', 86: 'n02109047-Great Dane', 87: 'n02097209-Standard Schnauzer', 88: 'n02093256-Staffordshire Bullterrier', 89: 'n02090622-Borzoi', 90: 'n02108915-French Bulldog',
91: 'n02096177-Cairn Terrier', 92: 'n02101006-Gordon Setter', 93: 'n02095314-Wire Haired Fox Terrier', 94: 'n02111277-Newfoundland', 95: 'n02110185-Siberian Husky', 96: 'n02090721-Irish Wolfhound', 97: 'n02092339-Weimaraner', 98: 'n02102480-Sussex_spaniel', 99: 'n02088632-Bluetick', 100: 'n02096585-Boston Bull', 
101: 'n02100583-Vizsla', 102: 'n02093754-Border Terrier', 103: 'n02093428-American Staffordshire Terrier', 104: 'n02098105-Soft Coated Wheaten Terrier', 105: 'n02110627-Affenpinscher', 106: 'n02097130-Giant Schnauzer', 107: 'n02095570-Lakeland Terrier', 108: 'n02089867-Treeing Walker Coonhound', 109: 'n02085782-Japanese Spaniel', 110: 'n02113978-Mexican Hairless',
111: 'n02102973-Irish Water Spaniel', 112: 'n02088238-Basset Hound', 113: 'n02105505-komondor', 114: 'n02095889-Sealyham Terrier', 115: 'n02105412-Kelpie', 116: 'n02093647-Bedlington Terrier', 117: 'n02107312-Miniature Pinscher', 118: 'n02108551-Tibetan Mastiff', 119: 'n02099429-Curly Coated Retriever'}