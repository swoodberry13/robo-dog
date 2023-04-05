clear; clc; 

wayPoints = [8 -2.5; 8 0;...
    8 2.5; 7 2;... 
    6.5 1; 7 0;...
    6.5 -1; 7 -2;
    8 -2.5]; % XY loc of each waypoint


ts = 1; % time in s between each waypoint
posDiv = 100; % number of intervals on each segment 
height = size(wayPoints);
height = height(1); % number of waypoints 
timeLength = ts * height; % time from first to last waypoint
t = linspace(0,timeLength,4*posDiv); % time array 

% First Segment 
% coordinate vectors for the segment's waypoints
x1 = wayPoints([1:3],1); 
y1 = wayPoints([1:3],2); 

% coordinate vectors for all points in the segment
yy1 = linspace(y1(1),y1(3),posDiv); 
xx1 = spline(y1,x1,yy1); 

%Second Segment 
x2 = wayPoints([3:5],1); 
y2 = wayPoints([3:5],2); 

xx2 = linspace(x2(1),x2(3),posDiv); 
yy2 = spline(x2,y2,xx2);

% Third Segment 
x3 = wayPoints([5:7],1); 
y3 = wayPoints([5:7],2); 

yy3 = linspace(y3(1),y3(3),posDiv); 
xx3 = spline(y3',[0 x3' 0],yy3); 

% Fourth Segment 
x4 = wayPoints([7:9],1); 
y4 = wayPoints([7:9],2); 

xx4 = linspace(x4(1),x4(3),posDiv); 
yy4 = spline(x4,y4,xx4); 

% coordinate column vectors of path of LED (in order)
x = [xx1';xx2';xx3';xx4']; 
y = [yy1';yy2';yy3';yy4'];

% finding theta1 and theta2 at each point using inverse kinematics 
[theta1 , theta2] = findAngle(x,y,5,5); 

%plotting all of the 
figure 
hold on 
plot(xx1,yy1); 
plot(xx2,yy2); 
plot(xx3,yy3);
plot(xx4,yy4);
xlim([-16 16])
ylim([-20 1]);
hold off
%plot(x,y,'.')

% changing the initial position of the leg. 
s = find(floor(y) == 0); %might have to change the coeff of x 
s = s(1);

theta1 = [theta1; theta1(1:s-1)];
theta2 = [theta2; theta2(1:s-1)];

theta1 = theta1(s:end);
theta2 = theta2(s:end);

theta1 = flip(theta1);
theta2 = flip(theta2);

theta1 = theta1+90;
%theta2 = theta2+90;

figure
legAnimate(theta1,theta2,5,5)

% this script produces theta1 angles with respect to the x-axis but in
% reality the it is with respect to the y-axis so
% theta1 = theta1 + 90; 
% theta1 = -1*theta1;
% theta2 = -1*theta2;

% % create table from that array
data = array2table([theta1 theta2]); 
% 
% % save table as CSV file 
writetable(data,'legData.csv','Delimiter',',','QuoteStrings',true);
type 'legData.csv';