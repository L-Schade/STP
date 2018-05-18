vid = videoinput('gentl', 1, 'Mono8');  %Mono12Packed, Mono16
src = getselectedsource(vid);

vid.FramesPerTrigger = 1;

preview(vid);

i = 0;
while i<1000000000
   i=i+1;
end
stoppreview(vid);
% while true
%     w = waitforbuttonpress;
%     if w == 0
%         stoppreview(vid);
%     end
% end

%export image-file
start (vid)
imwrite(getdata(vid), 'C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild3.j2c');

%export matlab-file
% preview(vid);

%start(vid);

%stoppreview(vid);

%test = getdata(vid);
%save('C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild.png', 'test');
%clear test;