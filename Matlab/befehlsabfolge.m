vid = videoinput('gentl', 1, 'Mono8');
src = getselectedsource(vid);

vid.FramesPerTrigger = 1;

preview(vid);

start(vid);

stoppreview(vid);

imwrite(getdata(vid), 'C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild6.png');
