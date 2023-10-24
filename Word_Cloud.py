from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt 
import PIL

text = "aravind aravind aravind aravind aadhil aadhil ashique anas anas agnivesh \
adithyan abijith bestin bestin bibin amith aswin abhishek pranav \
aiswarya anjaly anjana Nandhana \
Varada Elza alona devika amritha ".title()
 
mask = np.array(PIL.Image.open("assets/heart.png"))
wc = WordCloud(mask=mask,background_color="white").generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()