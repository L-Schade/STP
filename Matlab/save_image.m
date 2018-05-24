%wichtig
vid = videoinput('gentl', 1, 'Mono8');  %Mono8(default), Mono12Packed, Mono16
src = getselectedsource(vid);
vid.FramesPerTrigger = 1;
%

% Abfrage
while true
    preview(vid);   % wichtig
    
    w = waitforbuttonpress;
	key = get(gcf,'CurrentCharacter'); % noch abhaengig vom Bild/ Video machen, nicht vom extra Fenster

    if (strcmp(key,'s'))
        %wichtig
        start(vid);    
        stoppreview(vid);   
        %
        
        close; % schlieﬂt figur
        
        % char date = 'datetime('today')';
        date = datestr(now,'yyyy_mm_dd_HH_MM_SS_FFF');
        % date = char(date);
        fprintf('%s\n',date);
        % char dat = '1';

        % imwrite(getdata(vid), 'C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild4.png');    %wichtig
        % fprintf('C:%sDokumente und Einstellungen%sDoer-se-proj%sEigene Dateien%sMATLAB%sBilder%s%s.png','\','\','\','\','\','\',date);
         dest = ['C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\Bilder\',date,'.png'];
        imwrite(getdata(vid), char(dest));
        
        % preview(vid);   %neues Bild/ Video starten
        % break;
    elseif key == 'q'   
        close;
        stoppreview(vid); 
        % close(vid);
        fprintf('beendet\n');
        break;
    end;
end;
