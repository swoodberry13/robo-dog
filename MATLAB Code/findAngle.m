function [theta1 , theta2] = findAngle(x,y,l1,l2)
% inverse kinematics function 
% converts x and y coordinates to theta1 and theta2 angles (in degrees) for 
% a two segment arm
% x and y are the coordinates to be converted 
% l1 is the length of the first segment of the arm (whose base sits on the
% origin)

r1 = sqrt(x.^2 + y.^2); 
b1 = (l2^2-l1^2-r1.^2)./(-2*l1*r1);
a1 = atan2(sqrt(1-b1.^2),b1);
a3 = atan2(y,x);
theta1 = rad2deg(a3-a1);

b2 = (r1.^2-l1^2-l2^2)/(-2*l1*l2);
a2 = atan2(sqrt(1-b2.^2),b2);
theta2 = 180 - rad2deg(a2);
end