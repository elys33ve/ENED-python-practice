% MATLAB 4: 2D Arrays

clc; clear;

%%% GET JPG
pic = imread('Arm_Fracture.jpg');
s = size(pic);
%figure(1); imshow(pic);
pic_light = pic + 50;
%figure(2); imshow(pic_light);
pic_dark = pic / 2;
%figure(3); imshow(pic_dark);
