function legAnimate(theta1,theta2,l1,l2,varargin)
% function takes in values stated above for a two segment leg 
% makes animation of the leg moving at specific angles based on the input
% lengths of the segments 
% the value n represents how many cycles are plotted in the animation
% note: angle inputs must be in degrees 

if nargin == 4
    n = 1;
else
    n = varargin{1};
end

xcomp1 = l1*cosd(theta1);
ycomp1 = l1*sind(theta1);

xcomp2 = l2*cosd(theta1+theta2);
ycomp2 = l2*sind(theta1+theta2);

xfoot = xcomp1 + xcomp2;
yfoot = ycomp1 + ycomp2; 


for m = 1:n
for k = 1:size(theta1)
    plot([0,xcomp1(k)],[0,ycomp1(k)],'-', ... 
        [xcomp1(k) xfoot(k)],[ycomp1(k) yfoot(k)],'-')
    xlim([-5 5])
    ylim([0 10])
    pause(0.01)
end
end
plot(xfoot,yfoot,'o')
end