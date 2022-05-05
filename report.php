<?php>
    $name= $_POST['firstname']. ' '. $_POST['lastname'];
    $when_it_happened= $_POST['whenithappened'];
    $how_long= $_POST['howlong'];
    $how_many= $_POST['howmany'];
    $alien_description= $_POST['aliendescription'];
    $what_they_did= $_POST['whattheydid'];
    $fang_spotted= $_POST['fangspotted'];
    $email= $_POST['email'];
    $other= $_POST['other'];

    $to='owen@aliensabductedme.com';
    $subject='Aliens Abducted me- Abduction Report';
    $msg= "$name was abducted $when_it_happened and was gone for $how_long .\n "
    "Number of aliens: $how_many\n" .
    "Alien description: $alien_description\n" .
    "What they did: $what_they_did\n" .
    "Fang spotted: $fang_spotted\n" .
    "Other comments: $other\n" ;

    mail($to, $subject, $msg, 'From:', . $email, );
    // "From: " . $from . "\r\nCc: " . $cc; is used for Cc or Bcc in emails


    echo 'Thanks for submitting the form. <br />';
    echo 'Your name is: ' . $name . '<br />';
    echo 'You were abducted ' . $when_it_happened;
    echo ' and were gone for ' . $how_long . '<br />';
    echo 'How many were they? ' . $how_many . '<br />';
    echo 'Describe them: ' . $alien_description . '<br />';
    echo 'What did they do to you? ' . $what_they_did . '<br />';
    echo 'Was Fang there? ' . $fang_spotted . '<br />';
    echo 'Your email address is ' . $email . '<br />';
    echo 'Anything else you would like to add: ' . $other . '<br />';


?>