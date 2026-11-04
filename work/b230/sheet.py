import cairosvg,glob,sys,io
from PIL import Image,ImageDraw
files=sorted(glob.glob(sys.argv[1]))
ims=[]
for f in files:
    png=cairosvg.svg2png(url=f,output_width=500,background_color='white')
    im=Image.open(io.BytesIO(png)).convert('RGB');im.thumbnail((500,400))
    ims.append((f,im))
cols=3;W=520;H=440
rows=(len(ims)+cols-1)//cols
sheet=Image.new('RGB',(cols*W,rows*H),'white');d=ImageDraw.Draw(sheet)
for k,(f,im) in enumerate(ims):
    x=(k%cols)*W;y=(k//cols)*H
    sheet.paste(im,(x+10,y+30));d.text((x+10,y+5),f.split('/')[-1],fill='red')
sheet.save(sys.argv[2]);print(sys.argv[2],len(ims))
