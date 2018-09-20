%wichtig
vid = videoinput('gentl', 1, 'Mono8');  %Mono8(default), Mono12Packed, Mono16
src = getselectedsource(vid);
vid.FramesPerTrigger = 1;
%

% Abfrage
while true
    figure;  %    figure;
    preview(vid);   % wichtig
    
    w = waitforbuttonpress;
	key = get(gcf,'CurrentCharacter'); % noch abhaengig vom Bild/ Video machen, nicht vom extra Fenster
    % key = get(groot,'CurrentCharacter');      % funlktioniert nicht
    % key = get(vid,'CurrentCharacter');        % funktioniert auf jeden
    % fall nicht

    if (strcmp(key,'s'))
        %wichtig
        start(vid);    
        stoppreview(vid);   
        %
        
        close; % schlieﬂt figur, Tastenabfrage h‰ngt davon ab!
        
        % char date = 'datetime('today')';
        date = datestr(now,'yyyy_mm_dd_HH_MM_SS_FFF');
        % date = char(date);
        fprintf('%s\n',date);
        % char dat = '1';

        % imwrite(getdata(vid), 'C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\bild4.png');    %wichtig
        % fprintf('C:%sDokumente und Einstellungen%sDoer-se-proj%sEigene Dateien%sMATLAB%sBilder%s%s.png','\','\','\','\','\','\',date);
        % dest = ['C:\Dokumente und Einstellungen\Doer-se-proj\Eigene Dateien\MATLAB\Bilder\',date,'.png'];
        dest = ['C:\MatLab-Bilder\',date,'.png'];
        imwrite(getdata(vid), char(dest));
        
        % preview(vid);   %neues Bild/ Video starten
        % break;
    elseif key == 'q'   
        close;    % um extra Fenster zu schlieﬂen???
        % close(gcf)            alternativ mal testen !!!
        
        stoppreview(vid); 
        closepreview(vid); 
        
        fprintf('beendet\n');
        break;
    end;
end;
