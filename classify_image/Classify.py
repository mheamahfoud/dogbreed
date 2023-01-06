from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from PIL import Image
from django.conf import settings
import os
from skimage.io import imread


def get_model():
        model = load_model(os.path.join(settings.MEDIA_ROOT, 'Model/my_model.h5'))
        return model 
        
def predict(image):
        loaded_model = get_model()
        img = Image.open(image);#load_img(image, target_size=(224, 224), color_mode = "rgb")
        img = img.convert('RGB')
        img = img.resize((224, 224))
        img.save(os.path.join(settings.MEDIA_ROOT, 'Model/test.jpg'))
        img=imread(os.path.join(settings.MEDIA_ROOT, 'Model/test.jpg'))
        img = preprocess_input(img)
        probs = loaded_model.predict(np.expand_dims(img, axis=0))
        return probs



label_maps_rev={
         0: 'n02109525-Saint_Bernard',
         1: 'n02099429-curly-coated_retriever',
         2: 'n02097474-Tibetan_terrier',
         3: 'n02104365-schipperke',
         4:'n02104029-kuvasz',
         5: 'n02105056-groenendael',
         6: 'n02107312-miniature_pinscher',
         7: 'n02115641-dingo',
         8: 'n02099849-Chesapeake_Bay_retriever',
         9: 'n02093991-Irish_terrier',
         10: 'n02115913-dhole',
         11: 'n02098105-soft-coated_wheaten_terrier',
         12: 'n02094114-Norfolk_terrier',
         13: 'n02088632-bluetick',
         14: 'n02089867-Walker_hound',
         15: 'n02085620-Chihuahua',
         16: 'n02090379-redbone',
         17: 'n02106166-Border_collie',
         18: 'n02105855-Shetland_sheepdog',
         19: 'n02089078-black-and-tan_coonhound',
         20: 'n02110806-basenji',
         21: 'n02108000-EntleBucher',
         22: 'n02111129-Leonberg',
         23: 'n02110958-pug',
         24: 'n02098286-West_Highland_white_terrier',
         25: 'n02086646-Blenheim_spaniel',
         26: 'n02102318-cocker_spaniel',
         27: 'n02091635-otterhound',
         28: 'n02105641-Old_English_sheepdog',
         29: 'n02108915-French_bulldog',
         30: 'n02112018-Pomeranian',
         31: 'n02085782-Japanese_spaniel',
         32: 'n02097130-giant_schnauzer',
         33: 'n02091467-Norwegian_elkhound',
         34: 'n02105505-komondor',
         35: 'n02090721-Irish_wolfhound',
         36: 'n02097209-standard_schnauzer',
         37: 'n02096177-cairn',
         38: 'n02105162-malinois',
         39: 'n02094258-Norwich_terrier',
         40: 'n02100583-vizsla',
         41: 'n02093754-Border_terrier',
         42: 'n02113978-Mexican_hairless',
         43: 'n02093256-Staffordshire_bullterrier',
         44: 'n02102040-English_springer',
         45: 'n02091134-whippet',
         46: 'n02092339-Weimaraner',
         47: 'n02107683-Bernese_mountain_dog',
         48: 'n02088094-Afghan_hound',
         49: 'n02096294-Australian_terrier',
         50: 'n02107142-Doberman',
         51: 'n02086910-papillon',
         52: 'n02090622-borzoi',
         53: 'n02097658-silky_terrier',
         54: 'n02106550-Rottweiler',
         55: 'n02106382-Bouvier_des_Flandres',
         56: 'n02096437-Dandie_Dinmont',
         57: 'n02088466-bloodhound',
         58: 'n02091831-Saluki',
         59: 'n02087394-Rhodesian_ridgeback',
         60: 'n02116738-African_hunting_dog',
         61: 'n02102480-Sussex_spaniel',
         62: 'n02099712-Labrador_retriever',
         63: 'n02107574-Greater_Swiss_Mountain_dog',
         64: 'n02100236-German_short-haired_pointer',
         65: 'n02113186-Cardigan',
         66: 'n02113799-standard_poodle',
         67: 'n02107908-Appenzeller',
         68: 'n02113624-toy_poodle',
         69: 'n02085936-Maltese_dog',
         70: 'n02111500-Great_Pyrenees',
         71: 'n02108422-bull_mastiff',
         72: 'n02095314-wire-haired_fox_terrier',
         73: 'n02086079-Pekinese',
         74: 'n02101556-clumber',
         75: 'n02106030-collie',
         76: 'n02096585-Boston_bull',
         77: 'n02092002-Scottish_deerhound',
         78: 'n02093428-American_Staffordshire_terrier',
         79: 'n02091244-Ibizan_hound',
         80: 'n02089973-English_foxhound',
         81: 'n02099267-flat-coated_retriever',
         82: 'n02097298-Scotch_terrier',
         83: 'n02112137-chow',
         84: 'n02096051-Airedale',
         85: 'n02112350-keeshond',
         86: 'n02111277-Newfoundland',
         87: 'n02095570-Lakeland_terrier',
         88: 'n02087046-toy_terrier',
         89: 'n02101388-Brittany_spaniel',
         90: 'n02097047-miniature_schnauzer',
         91: 'n02106662-German_shepherd',
         92: 'n02105412-kelpie',
         93: 'n02109961-Eskimo_dog',
         94: 'n02108551-Tibetan_mastiff',
         95: 'n02095889-Sealyham_terrier',
         96: 'n02091032-Italian_greyhound',
         97: 'n02093859-Kerry_blue_terrier',
         98: 'n02110185-Siberian_husky',
         99: 'n02110063-malamute',
         100: 'n02113712-miniature_poodle',
         101: 'n02102177-Welsh_springer_spaniel',
         102: 'n02111889-Samoyed',
         103: 'n02088238-basset',
         104: 'n02086240-Shih-Tzu',
         105: 'n02098413-Lhasa',
         106: 'n02113023-Pembroke',
         107: 'n02093647-Bedlington_terrier',
         108: 'n02102973-Irish_water_spaniel',
         109: 'n02094433-Yorkshire_terrier',
         110: 'n02110627-affenpinscher',
         111: 'n02100877-Irish_setter',
         112: 'n02100735-English_setter',
         113: 'n02099601-golden_retriever',
         114: 'n02112706-Brabancon_griffon',
         115: 'n02101006-Gordon_setter',
         116: 'n02108089-boxer',
         117: 'n02109047-Great_Dane',
         118: 'n02105251-briard',
         119: 'n02088364-beagle'}