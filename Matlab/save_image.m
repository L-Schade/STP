preview(vid);   %wichtig

% Abfrage
while true
  key = getkey();
  printf("%c\n",key);

  if key == 's'
    date = datetime('today');
    printf("%c\n", date);
    
    start(vid);    %wichtig

    stoppreview(vid);    %wichtig

    % imwrite(getdata(vid), 'C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild4.png');    %wichtig
    imwrite(getdata(vid), ('C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\%c.png', date));
  elseif key == 'q'
    break;
  end;