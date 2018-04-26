use v5.22.1;
use warnings;
use strict;
use Term::ReadKey;
use Switch;

my $x = 0;
my $y = 3;
my $z = 0;
my $wait = 3;
my $mode;

say "choose the right mode:";
say "press 1 for the automatically mode";
say "press 2 for the coordinate mode";
say "press 3 for the navigation mode";

local ($| ) = (1);        #sorgt dafuer,dass alles davor auch zuerst ausgefuehrt wird

# wait for event, keyboard entry
ReadMode 4;
while(not defined ($mode = ReadKey(- 1))){
}
ReadKey(-1);                #sonst kann man nicht in navigate von der Tastatur lesen
print "You choose mode $mode\n";
ReadMode 0;

switch ($mode){
    case 1 {&automatic;}
    case 2 {&coordinaten;}
    case 3 {&navigate;}
    else {print "undefinded key pressed\n"; exit;}
}

sub automatic{
    say "class automatic";
}

sub coordinaten{
    say "class coordinate";
    say "x coordinate:";
    $x = <STDIN>;
    say "y coordinate:";
    $y = <STDIN>;
    say "z coordinate:";
    $z = <STDIN>;
    say "time to wait:";
    $wait = <STDIN>;
    say $x;
    say $y;
    say $z;
    say $wait;
    &printScript;
    &saveCoordinaten;
}

# Verbesserungen: mehrmals eine Taste druecken zu koennen -> mehrere Schritte auf einmal machen können
sub navigate{
    say "class navigate";
    my $key;

    # wait for event, keyboard entry
    ReadMode 4;
    while(not defined ($key = ReadKey(- 1))){

    }
    print "Get key $key\n";
    ReadMode 0;

    # read entry
    switch ($key){
        case "l" {
            say "moved to the right side\n";
            $x++
        }
        case "k" {say "moved down\n"}
        case "j" {say "moved to the left side\n"}
        case "i" {say "moved up\n"}
        else { print "undefinded key pressed\n"; exit;}
        # press l to move to the right side\npress k to move down\npress i to move up\n\n
    }

    if ($key eq 'l') {
        say "moved to the right side\n";
        $x++;                           # nur als Bsp
    }
    elsif ($key eq 'j') {
        say "moved to the left side\n";
    }
    elsif ($key eq 'k') {
        say "moved down\n";
    }
    elsif ($key eq 'i') {
        say "moved up\n";
    }
    else {
        say "undefinded key pressed!";
        say "press l to move to the right side";
        say "press k to move down";
        say "press j to move to the left side";
        say "press i to move up\n";
    }
    &printScript;
    &saveCoordinaten;
}

sub printScript{
    # write .mcs script for controller
    my $filename = 'script.mcs';
    open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
    print $fh ("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n
SetAngle($x,$y,$z); # sets pitch, roll, yaw, in degrees
Wait( '$wait' );          # waits 3 seconds \n
DoCamera( 'Shutter' );  # ??? \n
RecenterCamera();       # recenters all three axes
TextOut( 'End' );       # eigentlich: TextOut( 'End !mit Umbruch!' );");
    close $fh;
    print "done\n";
}

sub saveCoordinaten{
    my $filename = 'coordinaten.txt';
    open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
    print $fh "$x";
    print $fh "$y";
    print $fh "$z";
    close $fh;
    print "saved coordinaten\n";
}

#TODO:
#alte Koordinaten aus script.mcs lesen und wieder verwenden
#Zeilenumbrueche nach Variablen im .msc entfernen
#Beschreinung fuer Tasten in navigation
#umbrueche bei naviagte in script.mcs verbessern
