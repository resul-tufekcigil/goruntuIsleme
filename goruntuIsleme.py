#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:17:19 2022

@author: Resul Tüfekcigil
"""
import sys,getopt
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
def main(argv):
   image_path = ""
   def filtrele(img, filtre):

       if len(img.shape) == 3:
           img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       imgSatir, imgSutun = img.shape
       filtreSatir, filtreSutun = filtre.shape

       kenarlar = np.zeros(img.shape)

       pad_height = int((filtreSatir - 1) / 2)
       pad_width = int((filtreSutun - 1) / 2)

       filtreli = np.zeros((imgSatir + (2 * pad_height), imgSutun + (2 * pad_width)))

       filtreli[pad_height:filtreli.shape[0] - pad_height, pad_width:filtreli.shape[1] - pad_width] = img

       for satir in range(imgSatir):
           for sutun in range(imgSutun):
               kenarlar[satir, sutun] = np.sum(filtre * filtreli[satir:satir + filtreSatir, sutun:sutun + filtreSutun])
               
       return kenarlar
   
   def gamaDonusun(img, gama):
       Gama = 1 / gama

       table = [((i / 255) ** Gama) * 255 for i in range(256)]
       table = np.array(table, np.uint8)

       return cv2.LUT(img, table)
   def boyutlandir(img):
       boyut = img.astype(float)
       boyut -= np.min(boyut)
       boyut /= np.max(boyut)
       return (boyut*255).astype(np.uint8)




   def bitDonustur(img, duzlem):
        katman_img = np.full_like(img, duzlem)
        return np.bitwise_and(img, katman_img)

       
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","options="])
   except getopt.GetoptError:
      print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
      sys.exit(1)
   for opt, arg in opts:
      if opt == '-h':
         print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
         sys.exit(1)
      elif opt in ("-i","--ifile"):
          image_path=arg
      elif opt in ("-o", "--options"):
          if arg=='gama':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)
                  img3=gamaDonusun(img, 3.0)
                  img4=gamaDonusun(img, 4.0)
                  img5=gamaDonusun(img, 5.0)
                  dikey = np.vstack((img3,img4,img5))
                  plt.imshow(dikey,cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='logaritmik':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)
                  log = (np.log(img+1)/(np.log(1+np.max(img))))*255
                  log = np.array(log,dtype=np.uint8)
                  plt.imshow(log,cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='negatif':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path)
                  imgp=img
                  imgn = cv2.bitwise_not(img)
                  dikey = np.vstack((imgp,imgn))
                  plt.imshow(cv2.cvtColor(dikey, cv2.COLOR_BGR2RGB), vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='metin':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)
                  __, esikDeger = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)    
                  tam = np.hstack((img, esikDeger))
                  plt.imshow(tam, cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='bit_slicing':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)

                  bit = bitDonustur(img, 8)
                  bit2 = boyutlandir(bit)
                  img8=bit2
                  
                  bit = bitDonustur(img, 16)
                  bit2 = boyutlandir(bit)
                  img16=bit2
                  
                  bit = bitDonustur(img, 24)
                  bit2 = boyutlandir(bit)
                  img24=bit2
                  
                  yatay1 = np.hstack((img,img8))
                  yatay2 = np.hstack((img16,img24))
                  
                  tam = np.vstack((yatay1, yatay2))
                  plt.imshow(tam, cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='kenar':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)
                  
                  sobelFilitreD = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
                  sobelFilitreY = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
                  
                  prewittFilitreD = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
                  prewittFilitreY = np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])
                  
                  rcrossFilitreD = np.array([[1, 0],[0, -1]])
                  rcrossFilitreY = np.array([[0, 1],[-1, 0]])
                  
                  SimgD = filtrele(img,sobelFilitreD)
                  SimgY = filtrele(img,sobelFilitreY)
                  
                  PimgD = filtrele(img,prewittFilitreD)
                  PimgY = filtrele(img,prewittFilitreY)
                  
                  CimgD = filtrele(img,rcrossFilitreD)
                  CimgY = filtrele(img,rcrossFilitreY)
                  
                  yatay1=np.hstack((img,img))
                  yatay2=np.hstack((SimgD,SimgY))
                  yatay3=np.hstack((PimgD,PimgY))
                  yatay4=np.hstack((CimgD,CimgY))
                  tam=np.vstack((yatay1,yatay2,yatay3,yatay4))
                  plt.imshow(tam, cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
          elif arg=='addNoise':
              if image_path=="":
                  print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')
                  sys.exit(1)
              else:
                  img = cv2.imread(image_path,0)
                  tuz=np.random.randint(0,2,size=img.shape[:2])
                  tuz=tuz*255
                  karabiber=np.random.randint(0,2,size=img.shape[:2])
                  karabiber=tuz*0
                  img2=img+tuz+karabiber
                  tam=np.hstack((img, img2))
                  plt.imshow(tam,cmap='gray', vmin=0, vmax=255)
                  plt.axis("off")
                  plt.show()
      else:
         print ('usage:\n -i image_path \n -o options\n\t gama\n\t logaritmik\n\t negatif\n\t metin\n\t bit_slicing\n\t kenar \n\t addNoise')

if __name__ == "__main__":
   main(sys.argv[1:])
