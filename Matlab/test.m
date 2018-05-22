% date = datetime('today');
% date_matrix = clock();
date = strftime ("%Y_%m_%d_%H_%M_%S", localtime (time ()));
dat = 1;

printf(date);
printf("save image to %o", dat);

% key = get(gcf,'CurrentCharacter');
key = getkey ;

printf("%c",key);

% C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\%o.png
% C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild4.png