<link rel="stylesheet" href="main.css">

<h2>Réception des informations</h2>

<?php

echo "Bonjour ".$_POST['nom']." ".$_POST['prenom']."<br>";
echo "Mot de passe : ".$_POST['pass']."<br>";
echo "Votre sexe : ".$_POST['sexe']."<br>";
echo "Votre filière : ".$_POST['filiere']."<br>";

echo "<br>Commentaire : ".$_POST['commentaire'];

?>

<h3>Informations environnement</h3>

<?php

echo "Adresse IP : ".$_SERVER['REMOTE_ADDR']."<br>";
echo "Navigateur : ".$_SERVER['HTTP_USER_AGENT']."<br>";
echo "Fichier exécuté : ".$_SERVER['PHP_SELF']."<br>";
echo "Serveur : ".$_SERVER['SERVER_NAME']."<br>";
echo "Version PHP : ".phpversion()."<br>";

?>
<br>
<a href="ajouterEtudiant.php">Ajouter un étudiant</a>
