from PIL import Image
from numpy import *
from scipy.ndimage import filters
import sys
import imageio
import math

# calculate "Edge strength map" of an image                                                                                                                                      
def edge_strength(input_image):
    grayscale = array(input_image.convert('L'))
    filtered_y = zeros(grayscale.shape)
    filters.sobel(grayscale,0,filtered_y)
    return sqrt(filtered_y**2)

# draw a "line" on an image (actually just plot the given y-coordinates
#  for each x-coordinate)
# - image is the image to draw on
# - y_coordinates is a list, containing the y-coordinates and length equal to the x dimension size
#   of the image
# - color is a (red, green, blue) color triple (e.g. (255, 0, 0) would be pure red
# - thickness is thickness of line in pixels
#
def draw_boundary(image, y_coordinates, color, thickness):
    for (x, y) in enumerate(y_coordinates):
        for t in range( int(max(y-int(thickness/2), 0)), int(min(y+int(thickness/2), image.size[1]-1 )) ):
            image.putpixel((x, t), color)
    return image

def draw_asterisk(image, pt, color, thickness):
    for (x, y) in [ (pt[0]+dx, pt[1]+dy) for dx in range(-3, 4) for dy in range(-2, 3) if dx == 0 or dy == 0 or abs(dx) == abs(dy) ]:
        if 0 <= x < image.size[0] and 0 <= y < image.size[1]:
            image.putpixel((x, y), color)
    return image


# Save an image that superimposes three lines (simple, hmm, feedback) in three different colors 
# (yellow, blue, red) to the filename
def write_output_image(filename, image, simple, hmm, feedback, feedback_pt):
    new_image = draw_boundary(image, simple, (255, 255, 0), 2)
    new_image = draw_boundary(new_image, hmm, (0, 0, 255), 2)
    new_image = draw_boundary(new_image, feedback, (255, 0, 0), 2)
    new_image = draw_asterisk(new_image, feedback_pt, (255, 0, 0), 2)
    imageio.imwrite(filename, new_image)



# main program
#
if __name__ == "__main__":

    if len(sys.argv) != 6:
        raise Exception("Program needs 5 parameters: input_file airice_row_coord airice_col_coord icerock_row_coord icerock_col_coord")

    input_filename = sys.argv[1]
    gt_airice = [ int(i) for i in sys.argv[2:4] ]
    gt_icerock = [ int(i) for i in sys.argv[4:6] ]

    # load in image 
    input_image = Image.open(input_filename).convert('RGB')
    image_array = array(input_image.convert('L'))

    # compute edge strength mask -- in case it's helpful. Feel free to use this.
    edge_strength = edge_strength(input_image)
#     print(edge_strength[0],edge_strength[1])
    col=len(edge_strength[0])
    row=len(edge_strength)
    imageio.imwrite('edges.png', uint8(255 * edge_strength / (amax(edge_strength))))
#     image = Image.open('edges.png')
#     image.show()
    # You'll need to add code here to figure out the results! For now,
    # just create some random lines.
#     airice_simple = [ image_array.shape[0]*0.25 ] * image_array.shape[1]
#     air_simple={}
    airice_simple=zeros(col)
#     print(airice_simple)
    for i in range(col):
        min_len=edge_strength[1][i]
        mini=0
        for j in range(row-10):
            if min_len<edge_strength[j][i]:
                min_len=edge_strength[j][i]
                mini=j
        airice_simple[i]=mini
#     print(airice_simple,'air')
#     airice_hmm = [ image_array.shape[0]*0.5 ] * image_array.shape[1]
    airice_hmm=zeros(col)
    airhmm={}
    for i in range(row-10):
        airhmm[str(i)]=math.log(edge_strength[i][0]+10)
#     print(airhmm,'ini')
    for i in range(1,col):
        air_list=list(airhmm.keys())
#         print(air_list,'list')
        for j in air_list:
            x=(j.split(','))
#             print(int(x[-1]),'x')
#             x=int(x)
            min_prob=airhmm[j]+math.log(row-int(x[-1]))*10+math.log(edge_strength[0][i]+10)
#             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
            mini=0
            for k in range(1,row-10):
#                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                if min_prob<=airhmm[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10):
                    min_prob=airhmm[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10)
                    mini=k
            airhmm[j+','+str(mini)]=airhmm.pop(j)
            airhmm[j+','+str(mini)]=min_prob
#     print(airhmm,'airhmm')
    val=max(airhmm.values())
    for k,v in airhmm.items():
#     print(k,v)
        if v==val:
#             print(k,'string')
            airice_hmm=k.split(',')
            break
    for i in range(len(airice_hmm)):
        airice_hmm[i]=int(airice_hmm[i])
#         airice_hmm[i]+=1
    
#     print(airice_hmm-airice_simple,'asdasd')
#     print(edge_strength[8][2])
#     print(edge_strength[20][2])
#             for k in range(row)
#     airice_hmm[0]=airice_simple[0]
#     for i in range(1,col):
#         min_prob=edge_strength[0][i]*(abs(airice_simple[i-1]))
#         mini=0
#         for j in range(row-10):
#             if min_prob>edge_strength[j][i]*(abs(airice_simple[i-1]-j)):
#                 min_prob>edge_strength[j][i]*(abs(airice_simple[i-1]-j))
#                 min_prob
    airice_feedback=zeros(col)
    airfeed={}
    airice_feedback[gt_airice[1]]=gt_airice[0]
    for i in range(row-10):
        if gt_airice[1]<=0:
            break
        airfeed[str(i)+','+str(gt_airice[0])]=math.log(edge_strength[i][gt_airice[1]-1]+10)+math.log(row-abs(gt_airice[0]-i))*10
#     print(airhmm,'ini')
    if gt_airice[1]==0:
        for i in range(row-10):
            airfeed[str(gt_airice[0])+','+str(i)]=math.log(edge_strength[i][1]+10)+math.log(row-abs(gt_airice[0]-i))*10
    for i in range(gt_airice[1]-2,-1,-1):
        air_list=list(airfeed.keys())
#         print(air_list,'list')
        for j in air_list:
            x=(j.split(','))
#             print(int(x[-1]),'x')
#             x=int(x)
            min_prob=airfeed[j]+math.log(row-int(x[0]))*10+math.log(edge_strength[0][i]+10)
#             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
            mini=0
            for k in range(1,row-10):
#                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                if min_prob<=airfeed[j]+math.log(row-abs(int(x[0])-k))*10+math.log(edge_strength[k][i]+10):
                    min_prob=airfeed[j]+math.log(row-abs(int(x[0])-k))*10+math.log(edge_strength[k][i]+10)
                    mini=k
            airfeed[str(mini)+','+j]=airfeed.pop(j)
            airfeed[str(mini)+','+j]=min_prob
#     print(airhmm,'airhmm')
    for i in range(gt_airice[1]+1,col):
        if i!=1:            
            air_list=list(airfeed.keys())
    #         print(air_list,'list')
            for j in air_list:
                x=(j.split(','))
    #             print(int(x[-1]),'x')
    #             x=int(x)
                min_prob=airfeed[j]+math.log(row-int(x[-1]))*10+math.log(edge_strength[0][i]+10)
    #             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
                mini=0
                for k in range(1,row-10):
    #                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                    if min_prob<=airfeed[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10):
                        min_prob=airfeed[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10)
                        mini=k
                airfeed[j+','+str(mini)]=airfeed.pop(j)
                airfeed[j+','+str(mini)]=min_prob
    val=max(airfeed.values())
    for k,v in airfeed.items():
#     print(k,v)
        if v==val:
#             print(k,'string')
            airice_feedback=k.split(',')
            break
    for i in range(len(airice_feedback)):
        airice_feedback[i]=int(airice_feedback[i])
#     airice_feedback= [ image_array.shape[0]*0.75 ] * image_array.shape[1]
    
    icerock_simple = zeros(col)
    for i in range(col):
        min_len=edge_strength[int(airice_simple[i])+10][i]
        mini=airice_simple[i]+10
        for j in range(int(airice_simple[i])+10,row):
            if min_len<edge_strength[j][i]:
                min_len=edge_strength[j][i]
                mini=j
        icerock_simple[i]=mini
        
    icerock_hmm=zeros(col)
    rockhmm={}
    for j in range(airice_hmm[0]+10,row):
            rockhmm[str(j)]=math.log(edge_strength[j][0]+10)
#     print(airhmm)
    for i in range(1,col):
        rock_list=list(rockhmm.keys())
#         print(air_list,'list')
        for j in rock_list:
            x=(j.split(','))
#             x=int(x)
            min_prob=rockhmm[j]+math.log(row-abs(int(x[-1])-(airice_hmm[i]+10)))*10+math.log(edge_strength[airice_hmm[i]+10][i]+10)
#             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
            mini=airice_hmm[i]+10
            for k in range(airice_hmm[i]+11,row):
#                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                if min_prob<rockhmm[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10):
                    min_prob=rockhmm[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10)
                    mini=k
            rockhmm[j+','+str(mini)]=rockhmm.pop(j)
            rockhmm[j+','+str(mini)]=min_prob
#     print(airhmm,'airhmm')
    val=max(rockhmm.values())
    for k,v in rockhmm.items():
#     print(k,v)
        if v==val:
#             print(k,'string')
            icerock_hmm=k.split(',')
            break
    for i in range(len(icerock_hmm)):
        icerock_hmm[i]=int(icerock_hmm[i])
#     for i in range(len(airice_hmm)):
#         airice_hmm[i]+=2
#     print(icerock_hmm)
#     print(min(icerock_simple-airice_simple),'ice')
#     icerock_hmm = [ image_array.shape[0]*0.5 ] * image_array.shape[1]
    icerock_feedback=zeros(col)
    rockfeed={}
    icerock_feedback[gt_icerock[1]]=gt_icerock[0]
    if gt_icerock[1]>0:
        for i in range(airice_feedback[gt_icerock[1]-1]+10,row):
            rockfeed[str(i)+','+str(gt_icerock[0])]=math.log(edge_strength[i][gt_icerock[1]-1]+10)+math.log(row-abs(gt_icerock[0]-i))*10
#     print(airhmm,'ini')
    if gt_icerock[1]==0:
        for i in range(airice_feedback[1]+10,row):
            rockfeed[str(gt_icerock[0])+','+str(i)]=math.log(edge_strength[i][1]+10)+math.log(row-abs(gt_icerock[0]-i))*10
    for i in range(gt_icerock[1]-2,-1,-1):
        rock_list=list(rockfeed.keys())
#         print(air_list,'list')
        for j in rock_list:
            x=(j.split(','))
#             print(int(x[-1]),'x')
#             x=int(x)
            min_prob=rockfeed[j]+math.log(row-abs(int(x[0])-(airice_feedback[i]+10)))*10+math.log(edge_strength[airice_feedback[i]+10][i]+10)
#             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
            mini=airice_feedback[i]+10
            for k in range(airice_feedback[i]+11,row):
#                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                if min_prob<=rockfeed[j]+math.log(row-abs(int(x[0])-k))*10+math.log(edge_strength[k][i]+10):
                    min_prob=rockfeed[j]+math.log(row-abs(int(x[0])-k))*10+math.log(edge_strength[k][i]+10)
                    mini=k
            rockfeed[str(mini)+','+j]=rockfeed.pop(j)
            rockfeed[str(mini)+','+j]=min_prob
#     print(airhmm,'airhmm')
    for i in range(gt_icerock[1]+1,col):
        if i!=1:
            rock_list=list(rockfeed.keys())
    #         print(air_list,'list')
            for j in rock_list:
                x=(j.split(','))
    #             print(int(x[-1]),'x')
    #             x=int(x)
                min_prob=rockfeed[j]+math.log(row-abs(int(x[-1])-(airice_feedback[i]+10)))*10+math.log(edge_strength[airice_feedback[i]+10][i]+10)
    #             print(airhmm[j],math.log(row+int(j[-1])),j,'0')
                mini=airice_feedback[i]+10
                for k in range(airice_feedback[i]+11,row):
    #                 print(airhmm[j],math.log(row+abs(int(j[-1])-k)),j,k)
                    if min_prob<=rockfeed[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10):
                        min_prob=rockfeed[j]+math.log(row-abs(int(x[-1])-k))*10+math.log(edge_strength[k][i]+10)
                        mini=k
                rockfeed[j+','+str(mini)]=rockfeed.pop(j)
                rockfeed[j+','+str(mini)]=min_prob
    val=max(rockfeed.values())
    for k,v in rockfeed.items():
#     print(k,v)
        if v==val:
#             print(k,'string')
            icerock_feedback=k.split(',')
            break
    for i in range(len(icerock_feedback)):
        icerock_feedback[i]=int(icerock_feedback[i])
    for i in range(len(airice_simple)):
        airice_simple[i]+=1
        airice_hmm[i]+=1
        airice_feedback[i]+=1
        icerock_simple[i]+=1
        icerock_hmm[i]+=1
        icerock_feedback[i]+=1
    # Now write out the results as images and a text file
    write_output_image("air_ice_output.png", input_image, airice_simple, airice_hmm, airice_feedback, gt_airice)
    # image = Image.open('air_ice_output.png')
    # image.show()
    write_output_image("ice_rock_output.png", input_image, icerock_simple, icerock_hmm, icerock_feedback, gt_icerock)
    # imag = Image.open('ice_rock_output.png')
    # imag.show()
    with open("layers_output.txt", "w") as fp:
        for i in (airice_simple, airice_hmm, airice_feedback, icerock_simple, icerock_hmm, icerock_feedback):
            fp.write(str(i) + "\n")
