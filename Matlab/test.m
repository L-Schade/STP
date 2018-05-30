% fprintf('\n Press any key:');
% ch = getkey;
% fprintf('ds');
% if(strcmp(getkey,'s'));
%     fprintf('test');
% end;

% k = waitforbuttonpress;
% value = get(gcf,'CurrentCharacter');
% fprintf(value);

dt = datestr(now,'yyyy_mm_dd_HH:MM:SS.FFF');
fprintf('%s\n',dt);

fprintf('C:%sDokumente und Einstellungen%sDoer-se-proj%sEigene Dateien%sMATLAB%sBilder%s%s.png\n','\','\','\','\','\','\',dt);